# README Generator

A Python script that uses Atomic Agents to generate a unified README for a repository containing different tools.

## Overview

This script analyzes a repository containing multiple tools, each with its own README file. It then generates a unified README that provides a user-friendly overview of the entire repository, making it easier for users to understand the purpose and functionality of all the tools in one place.

## Features

- Recursively finds all README files in a repository
- Uses AI to analyze the content of each README
- Extracts key information about each tool
- Generates a unified README with a consistent structure
- Provides a summary of all tools found in the repository

## Requirements

- Python 3.8+
- OpenAI API key
- Local OpenAI-compatible API server (optional)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/readme-generator.git
   cd readme-generator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   export OPENAI_API_KEY="your_openai_api_key"
   export OPENAI_BASE_URL="http://localhost:4000/v1"  # Optional, for local API server
   ```

## Usage

```bash
python readmeagent.py /path/to/repository --output UNIFIED_README.md
```

### Arguments

- `repo_path`: Path to the repository to analyze (required)
- `--output`, `-o`: Output file path for the unified README (default: UNIFIED_README.md)

## Example

```bash
python readmeagent.py ~/projects/my-toolkit --output ~/projects/my-toolkit/README.md
```

This will:
1. Find all README files in the repository
2. Analyze each README to understand the purpose of each tool
3. Generate a unified README that provides an overview of all tools
4. Save the unified README to the specified output file

## How It Works

The script uses the Atomic Agents framework to create an AI agent that:

1. Recursively searches for all README files in the repository
2. Analyzes the content of each README to understand the purpose and features of each tool
3. Identifies common themes and relationships between the tools
4. Extracts key information about each tool
5. Generates a unified README that provides a user-friendly overview of the entire repository

