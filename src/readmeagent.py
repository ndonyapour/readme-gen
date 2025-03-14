#!/usr/bin/env python3

import os
import argparse
import glob
import tempfile
import subprocess
import shutil
import instructor
import openai
from typing import List, Optional
from pydantic import Field, BaseModel
# from atomic_agents.lib.components.system_prompt_generator import SystemPromptGenerator
# from atomic_agents.lib.components.agent_memory import AgentMemory
# from atomic_agents.agents.base_agent import BaseAgent, BaseAgentConfig
from atomic_agents.lib.base.base_io_schema import BaseIOSchema

# Input/Output Schemas
class ReadmeContent(BaseModel):
    """Content of a README file."""
    path: str
    content: str
    tool_name: Optional[str] = None

class RepositoryAnalysisInput(BaseIOSchema):
    """Input schema for repository analysis that processes README files."""
    repo_url: str = Field(..., description="URL of the repository.")
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

def get_repository_path(repo_url_or_path: str, token: Optional[str] = None) -> tuple:
    """
    Get the repository path. If the input is a local path, use it directly.
    If it's a URL, clone it to a temporary directory.
    
    Returns:
        tuple: (repository_path, is_temp_dir)
    """
    # Check if the input is a local path
    if os.path.isdir(repo_url_or_path):
        print(f"Using existing local repository at {repo_url_or_path}")
        return repo_url_or_path, False
    
    # If token is provided, modify the repo URL to include authentication
    repo_url = repo_url_or_path
    if token:
        # Handle different URL formats
        if repo_url.startswith("https://github.com/"):
            # Format: https://TOKEN@github.com/owner/repo.git
            parts = repo_url.split("github.com/")
            repo_url = f"https://{token}@github.com/{parts[1]}"
        elif repo_url.startswith("git@github.com:"):
            # For SSH URLs, we need to convert to HTTPS
            parts = repo_url.split("git@github.com:")
            repo_url = f"https://{token}@github.com/{parts[1]}"
    
    # Clone the repository
    temp_dir = tempfile.mkdtemp()
    try:
        print(f"Cloning repository {repo_url} to {temp_dir}...")
        subprocess.run(
            ["git", "clone", "--depth=1", repo_url, temp_dir],
            check=True,
            capture_output=True,
            text=True
        )
        return temp_dir, True
    except subprocess.CalledProcessError as e:
        # Check if git is installed
        try:
            subprocess.run(["git", "--version"], check=True, capture_output=True)
            raise ValueError(f"Failed to clone repository: {e.stderr}")
        except FileNotFoundError:
            raise ValueError("Git is not installed or not in PATH. Please install Git to use this tool.")
        except Exception:
            raise ValueError(f"Failed to clone repository: {e.stderr}")

def find_readme_files(repo_path: str) -> List[ReadmeContent]:
    """Find all README files in the repository."""
    readme_files = []
    
    # Find all README files (case insensitive)
    for readme_path in glob.glob(f"{repo_path}/**/README*", recursive=True):
        try:
            # Skip .git directory
            if ".git" in readme_path:
                continue
                
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extract tool name from path (directory name)
            rel_path = os.path.relpath(readme_path, repo_path)
            path_parts = os.path.dirname(rel_path).split(os.path.sep)
            tool_name = path_parts[-1] if path_parts and path_parts[-1] else os.path.basename(repo_path)
            
            readme_files.append(ReadmeContent(
                path=rel_path,
                content=content,
                tool_name=tool_name
            ))
            print(f"Found README: {rel_path} (Tool: {tool_name})")
        except Exception as e:
            print(f"Error reading {readme_path}: {e}")
    
    return readme_files

def create_repository_analyzer_agent():
    """Create an agent to analyze the repository and generate a unified README."""
    # Create system prompt
    system_prompt = """You are an expert repository analyzer that helps create unified documentation.
Your task is to analyze README files from different tools in a repository and create a unified README.
The unified README should provide a clear overview of the repository and its tools.

Steps to follow:
1. Analyze each README file to understand the purpose and features of each tool.
2. Identify common themes and relationships between the tools.
3. Extract key information about each tool including name, description, key features, and usage examples.
4. Create a unified README that provides a user-friendly overview of the entire repository.

Output instructions:
- The unified README should be well-structured with clear headings and sections.
- Include an introduction to the repository as a whole.
- For each tool, provide a concise description and highlight key features.
- Include installation and usage instructions if applicable.
- The README should be informative but not excessively long.
- Use markdown formatting for better readability.

Your response should be a JSON object with the following structure:
{
  "repo_name": "Name of the repository",
  "repo_description": "Brief description of the repository",
  "tools": [
    {
      "name": "Tool name",
      "description": "Tool description",
      "key_features": ["Feature 1", "Feature 2", ...],
      "usage_example": "Example of how to use the tool (optional)"
    },
    ...
  ],
  "unified_readme": "The full markdown content of the unified README"
}
"""
    
    # Create OpenAI client with local endpoint
    try:
        # Create OpenAI client
        client = openai.OpenAI(base_url="http://localhost:4000/v1", api_key="sk-1212")
        
    except Exception as e:
        raise ConnectionError(f"Failed to connect to OpenAI API: {str(e)}")
    
    return client, system_prompt

def analyze_repository(client, system_prompt, input_data):
    """Analyze the repository using the OpenAI API directly."""
    # Prepare the messages
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Here are the README files from the repository {input_data.repo_url}:\n\n" + 
         "\n\n".join([f"File: {readme.path}\nTool: {readme.tool_name}\n\n{readme.content}" for readme in input_data.readme_files])}
    ]
    
    # Call the API
    print("Sending request to OpenAI API...")
    response = client.chat.completions.create(
        model="gpt4o",
        messages=messages,
        temperature=0.2
    )
    
    # Extract the content
    content = response.choices[0].message.content
    
    # Try to parse the JSON response
    try:
        import json
        result_json = json.loads(content)
        
        # Create the output object
        analysis = RepositoryAnalysisOutput(
            repo_name=result_json.get("repo_name", "Unknown Repository"),
            repo_description=result_json.get("repo_description", "No description provided"),
            tools=[ToolInfo(**tool) for tool in result_json.get("tools", [])],
            unified_readme=result_json.get("unified_readme", content)
        )
        
        # If the unified_readme is missing or too short, generate it from the analysis
        if not analysis.unified_readme or len(analysis.unified_readme) < 100:
            print("Generating markdown from analysis data...")
            analysis.unified_readme = generate_markdown_from_analysis(analysis)
        
        return analysis
    except json.JSONDecodeError:
        # If JSON parsing fails, use the raw content as the unified README
        print("Warning: Could not parse JSON response. Using raw content as unified README.")
        return RepositoryAnalysisOutput(
            repo_name=os.path.basename(input_data.repo_url),
            repo_description="Repository analysis results",
            tools=[],
            unified_readme=content
        )

def generate_markdown_from_analysis(analysis: RepositoryAnalysisOutput) -> str:
    """
    Generate a well-formatted markdown README from the repository analysis.
    
    Args:
        analysis: The repository analysis output
        
    Returns:
        str: Markdown content for the README
    """
    # Start with the title and description
    markdown = f"# {analysis.repo_name}\n\n"
    markdown += f"{analysis.repo_description}\n\n"
    
    # Add table of contents if there are multiple tools
    if len(analysis.tools) > 2:
        markdown += "## Table of Contents\n\n"
        markdown += "- [Overview](#overview)\n"
        for tool in analysis.tools:
            # Create anchor link from tool name
            anchor = tool.name.lower().replace(' ', '-').replace('_', '-')
            markdown += f"- [{tool.name}](#{anchor})\n"
        markdown += "- [Installation](#installation)\n"
        markdown += "- [Usage](#usage)\n"
        markdown += "\n"
    
    # Add overview section
    markdown += "## Overview\n\n"
    markdown += f"This repository contains {len(analysis.tools)} tools:\n\n"
    
    for tool in analysis.tools:
        markdown += f"- **{tool.name}**: {tool.description}\n"
    
    markdown += "\n"
    
    # Add detailed sections for each tool
    for tool in analysis.tools:
        # Create section header with tool name
        markdown += f"## {tool.name}\n\n"
        markdown += f"{tool.description}\n\n"
        
        # Add key features as a list
        if tool.key_features:
            markdown += "### Key Features\n\n"
            for feature in tool.key_features:
                markdown += f"- {feature}\n"
            markdown += "\n"
        
        # Add usage example if available
        if tool.usage_example:
            markdown += "### Usage Example\n\n"
            markdown += "```\n"
            markdown += f"{tool.usage_example}\n"
            markdown += "```\n\n"
    
    # Add installation section if we can extract it from the tools
    markdown += "## Installation\n\n"
    markdown += "To install and set up the tools in this repository:\n\n"
    markdown += "```bash\n"
    markdown += f"git clone https://github.com/username/{analysis.repo_name.lower().replace(' ', '-')}.git\n"
    markdown += f"cd {analysis.repo_name.lower().replace(' ', '-')}\n"
    markdown += "# Follow tool-specific installation instructions\n"
    markdown += "```\n\n"
    
    # Add usage section
    markdown += "## Usage\n\n"
    markdown += "Please refer to the individual tool sections for specific usage instructions.\n\n"
    
    return markdown

def main():
    """Main function to run the README generator."""
    parser = argparse.ArgumentParser(description="Generate a unified README for a repository.")
    parser.add_argument("repo", help="URL or local path of the Git repository to analyze.")
    parser.add_argument("--output", "-o", default="UNIFIED_README.md", help="Output file path for the unified README.")
    parser.add_argument("--token", "-t", help="GitHub personal access token for private repositories")
    parser.add_argument("--format", "-f", action="store_true", help="Force formatting of the README using the built-in formatter")
    args = parser.parse_args()
    
    repo_path = None
    is_temp_dir = False
    
    try:
        # Get repository path (either local or cloned)
        repo_path, is_temp_dir = get_repository_path(args.repo, args.token)
        
        # Find README files
        print(f"Searching for README files in the repository...")
        readme_files = find_readme_files(repo_path)
        print(f"Found {len(readme_files)} README files.")
        
        if not readme_files:
            print("No README files found. Exiting.")
            print("\nTips:")
            print("1. Make sure the repository URL or path is correct")
            print("2. For private repositories, provide a token with --token")
            print("3. Check if the repository has README files")
            return
        
        # Create agent
        print("Creating repository analyzer agent...")
        client, system_prompt = create_repository_analyzer_agent()
        
        # Analyze repository
        print("Analyzing repository and generating unified README...")
        input_data = RepositoryAnalysisInput(
            repo_url=args.repo,  # Use the original input for reference
            readme_files=readme_files
        )
        
        result = analyze_repository(client, system_prompt, input_data)
        
        # After getting the result, check if we should force formatting
        if args.format and result.tools:
            print("Formatting README with built-in formatter...")
            result.unified_readme = generate_markdown_from_analysis(result)
        
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
        import traceback
        traceback.print_exc()
        print("\nPlease check:")
        print("1. The repository URL or path is valid and accessible")
        print("2. Your local OpenAI API is running at http://localhost:4000/v1")
        print("3. You have git installed and can clone repositories (if using a URL)")
    finally:
        # Clean up temporary directory if it exists and was created by us
        if is_temp_dir and repo_path and os.path.exists(repo_path):
            try:
                shutil.rmtree(repo_path)
                print(f"Cleaned up temporary repository at {repo_path}")
            except Exception as e:
                print(f"Warning: Failed to clean up temporary directory: {e}")

if __name__ == "__main__":
    main()
