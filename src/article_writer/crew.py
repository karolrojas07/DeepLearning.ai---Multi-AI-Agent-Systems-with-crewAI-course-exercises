from crewai import Task, Agent, Crew
from crewai.project import CrewBase, agent, task, crew
from typing import List

@CrewBase
class ArticleWriterCrew():
    """
    A team of AI agents seasoned in writing sofisticated articles.
    """
    
    agents: List[Agent]
    tasks: List[Task]

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def planner(self) -> Agent:
        return Agent(
            config=self.agents_config['planner'], # type: ignore[index]
            verbose=True,  # Enable verbose output for the planner agent
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writter'], # type: ignore[index]
            verbose=True,  # Enable verbose output for the writer agent
        )
    
    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config['editor'], # type: ignore[index]
            verbose=True,  # Enable verbose output for the editor agent
        )
    
    @task
    def plan_article(self) -> Task:
        return Task(
            config=self.tasks_config['plan'] # type: ignore[index]
        )
    
    @task
    def write_article(self) -> Task:
        return Task(
            config=self.tasks_config['write'] # type: ignore[index]
        )
    
    @task
    def edit_article(self) -> Task:
        return Task(
            config=self.tasks_config['edit'] # type: ignore[index]
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,  # Enable verbose output for the crew
        )