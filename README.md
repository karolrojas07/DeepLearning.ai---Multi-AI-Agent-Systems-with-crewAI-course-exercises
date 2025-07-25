# Lessons' Exercises from DeepLearning.ai -  Multi AI Agent Systems with crewAI Course
This project uses `uv` as package manager.
Is developed in a  Windows 11 operating system and with python version 3.13.5..
Also uses Google GEMINI as LLM for all agents.

## Pre-requrements
1. Install `uv`
   ``` shell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

## Setup intructions
1. Create environment `uv venv --python 3.13`
2. Activate environment `source .venv/Scripts/activate`
3. Install dependencies `uv pip install .`
4. Set up environment variables `mv .env.example .env`
   ``` .env
    GEMINI_API_KEY=your_api_key // Get it from: https://aistudio.google.com/apikey
    MODEL=gemini/gemini-2.0-flash
   ```


## Run lessons
### Lesson 1: Article writer system

``` bash
uv run python -m src.article_writer.main
```


## Troubleshoot errors
If you face issues installing `crewai`, refer to the official [CrewAI installation instructions and issues](https://docs.crewai.com/en/installation#video-tutorial).