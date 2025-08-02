# Lessons' Exercises from DeepLearning.ai -  Multi AI Agent Systems with crewAI Course
This project uses `uv` as package manager.
Is developed in a  Windows 11 operating system and with python version 3.13.5.
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
    GEMINI_API_KEY=your_gemini_api_key // Get it from: https://aistudio.google.com/apikey
    GOOGLE_API_KEY=your_gemini_api_key
    MODEL=gemini/gemini-2.0-flash
    SERPER_API_KEY=your_serper_api_key // Get it from: https://serper.dev/
    OPENAI_API_KEY=your_openai_api_key // Get it from: https://platform.openai.com/api-keys
    OPENAI_MODEL=gpt-3.5-turbo 
   ```

## Run lessons
### Lesson 1: Article writer system

``` bash
uv run python -m src.article_writer.main
```

### Lesson 2: Customer support system

``` bash
uv run python -m src.customer_support.main
```

### Lesson 3: Customer outreach system

``` bash
uv run python -m src.customer_outreach.main
```

### Lesson 4: Event planning system
Because last CrewAI updates nly allows at most one asynchronous last task, the logistic task is not marked as asyncronous. Otherwise this error is prompt it:
```
An error occurred while running the crew: 1 validation error for Crew
  The crew must end with at most one asynchronous task. [type=async_task_count, input_value={'agents': [Agent(role=Ve...own.)], 'verbose': True}, input_type=dict]
```

``` bash
uv run python -m src.event_planning.main
```

### Lesson 5: Financial Analysis system 
``` bash
uv run python -m src.financial_analysis.main
```

### Lesson 6: Tailor Job application system 
``` bash
uv run python -m src.tailor_job_applications.main
```

## Troubleshoot errors
If you face issues installing `crewai`, refer to the official [CrewAI installation instructions and issues](https://docs.crewai.com/en/installation#video-tutorial).