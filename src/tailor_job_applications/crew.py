from crewai import Task, Agent, Crew
from crewai.project import CrewBase, agent, task, crew
from crewai_tools import (
  FileReadTool,
  ScrapeWebsiteTool,
  SerperDevTool,
  MDXSearchTool
)
from typing import List
from pathlib import Path

@CrewBase
class JobApplicationCrew():
    """
    A team of AI agents seasoned in planning and executing job application strategies.
    """
    
    agents: List[Agent]
    tasks: List[Task]

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()

    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()

    def __init__(self):
        # Get the base directory path
        base_path = Path(__file__).parent
        self.read_resume = FileReadTool(file_path=str(base_path / 'files/fake_resume.md'))
        self.semantic_search_resume = MDXSearchTool(mdx=str(base_path / 'files/fake_resume.md'))
    
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True,  # Enable verbose output for the researcher agent
            tools=[self.search_tool, self.scrape_tool]  # Assigning tools to the agent
        )

    @agent
    def profiler(self) -> Agent:
        return Agent(
            config=self.agents_config['profiler'], # type: ignore[index]
            verbose=True,  # Enable verbose output for the profiler agent
            tools=[self.search_tool, self.scrape_tool, self.read_resume]  # Assigning tools to the agent
        )
    
    @agent
    def resume_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_strategist'], # type: ignore[index]
            verbose=True,  # Enable verbose output for the resume strategist agent
            tools=[self.search_tool, self.scrape_tool, self.read_resume, self.semantic_search_resume]  # Assigning tools to the agent
        )
    
    @agent
    def interview_preparer(self) -> Agent:
        return Agent(
            config=self.agents_config['interview_preparer'], # type: ignore[index]
            verbose=True,  # Enable verbose output for the interview preparer agent
            tools=[self.search_tool, self.scrape_tool, self.read_resume]  # Assigning tools to the agent
        )
    
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
        )
    
    @task
    def profile_task(self) -> Task:
        return Task(
            config=self.tasks_config['profile_task'] # type: ignore[index]
        )
    
    @task
    def resume_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['resume_strategy_task'] # type: ignore[index]
        )
    
    @task
    def interview_preparation_task(self) -> Task:
        return Task(
            config=self.tasks_config['interview_preparation_task'] # type: ignore[index]
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[
                self.researcher(),
                self.profiler(),
                self.resume_strategist(),
                self.interview_preparer()
            ],
            tasks=[
                self.research_task(),
                self.profile_task(),
                self.resume_strategy_task(),
                self.interview_preparation_task()
            ],
            verbose=True,  # Enable verbose output for the crew
        )
        
        
        