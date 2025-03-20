#!/usr/bin/env python3

import os
import argparse
import glob
import tempfile
import subprocess
import shutil
from pathlib import Path
from typing import List, Optional
from pydantic import Field, BaseModel
from atomic_agents.lib.components.system_prompt_generator import SystemPromptGenerator
from atomic_agents.agents.base_agent import BaseAgent, BaseAgentConfig
from atomic_agents.lib.base.base_io_schema import BaseIOSchema
import instructor
import openai

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

# Create the agent configuration
AGENT_PROMPT = {
    "background": [
        "You are an expert repository analyzer that helps create unified documentation.",
        "Your task is to analyze README files from different tools in a repository and create a unified README.",
        "The unified README should provide a clear overview of the repository and its tools."
    ],
    "steps": [
        "Analyze each README file to understand the purpose and features of each tool.",
        "Identify common themes and relationships between the tools.",
        "Extract key information about each tool including name, description, key features, and usage examples.",
        "Create a unified README that provides a user-friendly overview of the entire repository."
    ],
    "output_instructions": [
        "The unified README should be well-structured with clear headings and sections.",
        "Include an introduction to the repository as a whole.",
        "For each tool, provide a concise description and highlight key features.",
        "Include installation and usage instructions if applicable.",
        "The README should be informative but not excessively long.",
        "Use markdown formatting for better readability.",
        "Your response should be a JSON object with the following structure:",
        "{",
        "  \"repo_name\": \"Name of the repository\",",
        "  \"repo_description\": \"Brief description of the repository\",",
        "  \"tools\": [",
        "    {",
        "      \"name\": \"Tool name\",",
        "      \"description\": \"Tool description\",",
        "      \"key_features\": [\"Feature 1\", \"Feature 2\", ...],",
        "      \"usage_example\": \"Example of how to use the tool (optional)\"",
        "    },",
        "    ...",
        "  ],",
        "  \"unified_readme\": \"The full markdown content of the unified README\"",
        "}"
    ]
}

# Create the agent
readme_agent = BaseAgent(
    BaseAgentConfig(
        client=instructor.from_openai(
            openai.OpenAI(base_url="http://localhost:4000/v1", api_key="sk-1212")
        ),
        model="gpt4o",
        temperature=0.2,
        system_prompt_generator=SystemPromptGenerator(
            background=AGENT_PROMPT["background"],
            steps=AGENT_PROMPT["steps"],
            output_instructions=AGENT_PROMPT["output_instructions"],
        ),
        input_schema=RepositoryAnalysisInput,
        output_schema=RepositoryAnalysisOutput,
    )
)

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
            parts = repo_url.split("github.com/")
            repo_url = f"https://{token}@github.com/{parts[1]}"
        elif repo_url.startswith("git@github.com:"):
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
    
    for readme_path in glob.glob(f"{repo_path}/**/README*", recursive=True):
        try:
            if ".git" in readme_path:
                continue
                
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
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
        repo_path, is_temp_dir = get_repository_path(args.repo, args.token)
        
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
        
        input_data = RepositoryAnalysisInput(
            repo_url=args.repo,
            readme_files=readme_files
        )
        
        print("Analyzing repository and generating unified README...")
        result = readme_agent.run(input_data)
        
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(result.unified_readme)
        
        print(f"Unified README saved to {args.output}")
        print("\nRepository Analysis Summary:")
        print(f"Repository Name: {result.repo_name}")
        print(f"Repository Description: {result.repo_description}")
        print(f"Tools Found: {len(result.tools)}")
        # for tool in result.tools:
        #     print(f"  - {tool.name}: {tool.description}")
            
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
        if is_temp_dir and repo_path and os.path.exists(repo_path):
            try:
                shutil.rmtree(repo_path)
                print(f"Cleaned up temporary repository at {repo_path}")
            except Exception as e:
                print(f"Warning: Failed to clean up temporary directory: {e}")

if __name__ == "__main__":
    main()