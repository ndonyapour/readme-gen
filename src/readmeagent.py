#!/usr/bin/env python3

import os
import argparse
import glob
import instructor
from openai import AzureOpenAI
from typing import List, Dict, Optional
from pydantic import Field, BaseModel
from atomic_agents.lib.components.system_prompt_generator import SystemPromptGenerator
from atomic_agents.lib.components.agent_memory import AgentMemory
from atomic_agents.agents.base_agent import BaseAgent, BaseAgentConfig
from atomic_agents.lib.base.base_io_schema import BaseIOSchema

# Environment variables
AZURE_API_KEY = os.getenv("AZURE_API_KEY", "")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT", "https://ncatspolusaithena.openai.azure.com/")
AZURE_DEPLOYMENT = os.getenv("AZURE_DEPLOYMENT", "gpt4o")

# Input/Output Schemas
class ReadmeContent(BaseModel):
    """Content of a README file."""
    path: str
    content: str
    tool_name: Optional[str] = None

class RepositoryAnalysisInput(BaseIOSchema):
    """Input schema for repository analysis that processes README files."""
    repo_path: str = Field(..., description="Path to the repository.")
    readme_files: List[ReadmeContent] = Field(..., description="List of README files found in the repository.")

class ToolInfo(BaseModel):
    """Information about a tool in the repository."""
    name: str = Field(..., description="Name of the tool.")
    description: str = Field(..., description="Brief description of the tool.")
    key_features: List[str] = Field(..., description="Key features of the tool.")
    usage_example: Optional[str] = Field(None, description="Example of how to use the tool.")

class RepositoryAnalysisOutput(BaseIOSchema):
    """Output schema for repository analysis that generates unified documentation."""
    repo_name: str = Field(..., description="Name of the repository.")
    repo_description: str = Field(..., description="Brief description of the repository.")
    tools: List[ToolInfo] = Field(..., description="List of tools found in the repository.")
    unified_readme: str = Field(..., description="Unified README content for the repository.")

def find_readme_files(repo_path: str) -> List[ReadmeContent]:
    """Find all README files in the repository."""
    readme_files = []
    
    # Find all README files (case insensitive)
    for readme_path in glob.glob(f"{repo_path}/**/README*", recursive=True):
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extract tool name from path
            tool_name = os.path.basename(os.path.dirname(readme_path))
            
            readme_files.append(ReadmeContent(
                path=readme_path,
                content=content,
                tool_name=tool_name
            ))
        except Exception as e:
            print(f"Error reading {readme_path}: {e}")
    
    return readme_files

def create_repository_analyzer_agent():
    """Create an agent to analyze the repository and generate a unified README."""
    # Create system prompt
    system_prompt_generator = SystemPromptGenerator(
        background=[
            "You are an expert repository analyzer that helps create unified documentation.",
            "Your task is to analyze README files from different tools in a repository and create a unified README.",
            "The unified README should provide a clear overview of the repository and its tools."
        ],
        steps=[
            "Analyze each README file to understand the purpose and features of each tool.",
            "Identify common themes and relationships between the tools.",
            "Extract key information about each tool including name, description, key features, and usage examples.",
            "Create a unified README that provides a user-friendly overview of the entire repository."
        ],
        output_instructions=[
            "The unified README should be well-structured with clear headings and sections.",
            "Include an introduction to the repository as a whole.",
            "For each tool, provide a concise description and highlight key features.",
            "Include installation and usage instructions if applicable.",
            "The README should be informative but not excessively long.",
            "Use markdown formatting for better readability."
        ]
    )
    
    if not AZURE_API_KEY:
        raise ValueError("AZURE_API_KEY environment variable is not set")
    
    # Create Azure OpenAI client
    try:
        # Create Azure OpenAI client first
        base_client = AzureOpenAI(
            api_key=AZURE_API_KEY,
            api_version="2024-12-01-preview",
            azure_endpoint=AZURE_ENDPOINT
        )
        
        # Create a wrapper for the completion create function
        def azure_completion_create(**kwargs):
            # Define supported parameters for Azure OpenAI
            supported_params = {
                'messages',
                'functions',
                'function_call',
                'temperature',
                'top_p',
                'n',
                'stream',
                'stop',
                'max_tokens',
                'presence_penalty',
                'frequency_penalty',
                'logit_bias',
                'user',
                'seed'
            }
            
            # Only keep supported parameters
            cleaned_kwargs = {
                k: v for k, v in kwargs.items() 
                if k in supported_params
            }
            
            # Ensure we have the required parameters
            if 'messages' not in cleaned_kwargs:
                raise ValueError("messages parameter is required")
            
            # Call the original create function with Azure deployment
            try:
                response = base_client.chat.completions.create(
                    model=AZURE_DEPLOYMENT,
                    **cleaned_kwargs
                )
                
                # Convert the response to the format expected by instructor
                if hasattr(response, 'choices') and len(response.choices) > 0:
                    message = response.choices[0].message
                    
                    # If there's a function call, return it as is
                    if hasattr(message, 'function_call') and message.function_call:
                        return {
                            'id': response.id,
                            'choices': [{
                                'message': {
                                    'content': message.content,
                                    'role': message.role,
                                    'function_call': message.function_call
                                }
                            }]
                        }
                    
                    # If it's a content response, try to parse it as JSON for our schema
                    try:
                        import json
                        content = json.loads(message.content)
                        # Ensure all required fields are present
                        if isinstance(content, dict):
                            if 'repo_name' not in content:
                                content['repo_name'] = os.path.basename(os.path.dirname(kwargs['messages'][0]['content']))
                            if 'repo_description' not in content:
                                content['repo_description'] = "Repository analysis results"
                            if 'tools' not in content:
                                content['tools'] = []
                            if 'unified_readme' not in content:
                                content['unified_readme'] = message.content
                            
                            # Convert to RepositoryAnalysisOutput
                            return RepositoryAnalysisOutput(**content)
                    except:
                        # If parsing fails, wrap the entire response in our schema
                        return RepositoryAnalysisOutput(
                            repo_name=os.path.basename(os.path.dirname(kwargs['messages'][0]['content'])),
                            repo_description="Repository analysis results",
                            tools=[],
                            unified_readme=message.content
                        )
                
                return response
            except Exception as e:
                print(f"Azure OpenAI API call failed with parameters: {cleaned_kwargs}")
                raise e
        
        # Create instructor client with the wrapper
        client = instructor.Instructor(
            client=base_client,
            mode="functions",
            create=azure_completion_create
        )
        
    except Exception as e:
        raise ConnectionError(f"Failed to connect to Azure OpenAI API: {str(e)}")
    
    # Create agent
    agent = BaseAgent(
        config=BaseAgentConfig(
            client=client,
            model=AZURE_DEPLOYMENT,  # This model parameter will be removed by the wrapper
            system_prompt_generator=system_prompt_generator,
            memory=AgentMemory(),
            input_schema=RepositoryAnalysisInput,
            output_schema=RepositoryAnalysisOutput
        )
    )
    
    return agent

def main():
    """Main function to run the README generator."""
    parser = argparse.ArgumentParser(description="Generate a unified README for a repository.")
    parser.add_argument("repo_path", help="Path to the repository.")
    parser.add_argument("--output", "-o", default="UNIFIED_README.md", help="Output file path for the unified README.")
    args = parser.parse_args()
    
    # Validate repository path
    if not os.path.exists(args.repo_path):
        print(f"Error: Repository path '{args.repo_path}' does not exist.")
        return
    
    # Find README files
    print(f"Searching for README files in {args.repo_path}...")
    readme_files = find_readme_files(args.repo_path)
    print(f"Found {len(readme_files)} README files.")
    
    if not readme_files:
        print("No README files found. Exiting.")
        return
    
    try:
        # Create agent
        print("Creating repository analyzer agent...")
        agent = create_repository_analyzer_agent()
        
        # Analyze repository
        print("Analyzing repository and generating unified README...")
        input_data = RepositoryAnalysisInput(
            repo_path=args.repo_path,
            readme_files=readme_files
        )
        
        result = agent.run(input_data)
        
        # Save unified README
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(result.unified_readme)
        
        print(f"Unified README saved to {args.output}")
        print("\nRepository Analysis Summary:")
        print(f"Repository Name: {result.repo_name}")
        print(f"Repository Description: {result.repo_description}")
        print(f"Tools Found: {len(result.tools)}")
        for tool in result.tools:
            print(f"  - {tool.name}: {tool.description}")
            
    except ValueError as e:
        print(f"Configuration Error: {str(e)}")
    except ConnectionError as e:
        print(f"Connection Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        print("\nPlease check:")
        print(f"1. Azure deployment name (currently set to '{AZURE_DEPLOYMENT}')")
        print("2. Your Azure API key and endpoint")
        print("3. Available deployments in your Azure OpenAI service")

if __name__ == "__main__":
    main()
