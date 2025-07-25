from crewai import Task, Agent, Crew
from crewai.project import CrewBase, agent, task, crew
from typing import List
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool

@CrewBase
class CustomerSupportCrew():
    """
    A team of AI agents seasoned in providing customer support.
    """
    
    agents: List[Agent]
    tasks: List[Task]

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # Tools
    docs_scrape_tool = ScrapeWebsiteTool(website_url="https://docs.crewai.com/en/concepts/crews#kicking-off-a-crew")

    @agent
    def support_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['support_agent'], # type: ignore[index]
            verbose=True,  # Enable verbose output for the support agent
        )

    @agent
    def support_quality_assurance_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['support_quality_assurance_agent'], # type: ignore[index]
            verbose=True,  # Enable verbose output for the support quality assurance agent
        )
  
    @task
    def inquiry_resolution(self) -> Task:
        return Task(
            config=self.tasks_config['inquiry_resolution'], # type: ignore[index]
            tools=[self.docs_scrape_tool]
        )
    
    @task
    def quality_assurance_review(self) -> Task:
        return Task(
            config=self.tasks_config['quality_assurance_review'] # type: ignore[index]
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True  # Enable verbose output for the crew
        )