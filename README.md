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

