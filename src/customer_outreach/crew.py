from crewai import Task, Agent, Crew
from crewai.project import CrewBase, agent, task, crew
from typing import List
from crewai_tools import DirectoryReadTool, FileReadTool, SerperDevTool
from .tools.sentiment_analysis_tool import SentimentAnalysisTool

@CrewBase
class CustomerOutreachCrew():
    """
    A team of AI agents seasoned in outreach customers.
    """
    
    agents: List[Agent]
    tasks: List[Task]

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # Tools
    directory_read_tool = DirectoryReadTool(directory='./instructions')
    file_read_tool = FileReadTool()
    search_tool = SerperDevTool()
    sentiment_analysis_tool = SentimentAnalysisTool()

    @agent
    def sales_rep_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['sales_rep_agent'], # type: ignore[index]
            verbose=True,  # Enable verbose output for the sales representative agent
        )

    @agent
    def lead_sales_rep_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['lead_sales_rep_agent'], # type: ignore[index]
            verbose=True,  # Enable verbose output for the lead sales representative agent
        )
  
    @task
    def lead_profiling_task(self) -> Task:
        return Task(
            config=self.tasks_config['lead_profiling_task'], # type: ignore[index]
            tools=[self.directory_read_tool, self.file_read_tool, self.search_tool]  # type: ignore[index]
        )
    
    @task
    def personalized_outreach_task(self) -> Task:
        return Task(
            config=self.tasks_config['personalized_outreach_task'], # type: ignore[index]
            tools=[self.sentiment_analysis_tool, self.search_tool]  # type: ignore[index]
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True  # Enable verbose output for the crew
        )