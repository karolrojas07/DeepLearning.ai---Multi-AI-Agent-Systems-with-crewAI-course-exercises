from crewai import Task, Agent, Crew
from crewai.project import CrewBase, agent, task, crew
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from typing import List
from .models.venueDetails import VenueDetails

@CrewBase
class EventPlanningCrew():
    """
    A team of AI agents seasoned in planning and executing events.
    """
    
    agents: List[Agent]
    tasks: List[Task]

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()

    @agent
    def venue_coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config['venue_coordinator'], # type: ignore[index]
            verbose=True,  # Enable verbose output for the venue coordinator agent
            tools=[self.search_tool, self.scrape_tool]  # Assigning tools to the agent
        )

    @agent
    def logistics_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['logistics_manager'], # type: ignore[index]
            verbose=True,  # Enable verbose output for the logistics manager agent
            tools=[self.search_tool, self.scrape_tool]  # Assigning tools to the agent
        )
    
    @agent
    def marketing_communications_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['marketing_communications_agent'], # type: ignore[index]
            verbose=True,  # Enable verbose output for the marketing communications agent
            tools=[self.search_tool, self.scrape_tool]  # Assigning tools to the agent
        )
    
    @task
    def venue_task(self) -> Task:
        return Task(
            config=self.tasks_config['venue_task'], # type: ignore[index]
            output_json= VenueDetails
        )
    
    @task
    def logistics_task(self) -> Task:
        return Task(
            config=self.tasks_config['logistics_task'] # type: ignore[index]
        )
    
    @task
    def marketing_task(self) -> Task:
        return Task(
            config=self.tasks_config['marketing_task'] # type: ignore[index]
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=[self.venue_task(), 
                    self.logistics_task(), 
                    self.marketing_task()],
            verbose=True,  # Enable verbose output for the crew
        )