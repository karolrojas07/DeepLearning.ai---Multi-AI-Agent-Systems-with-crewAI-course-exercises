from crewai import Task, Agent, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from typing import List

@CrewBase
class FinancialAnalysisCrew():
    """
    A team of AI agents seasoned in planning and executing financial strategies.
    """
    
    agents: List[Agent]
    tasks: List[Task]

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()

    @agent
    def data_analyst_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['data_analyst_agent'], # type: ignore[index]
            verbose=True,  # Enable verbose output for the data analyst agent
            tools=[self.search_tool, self.scrape_tool]  # Assigning tools to the agent
        )

    @agent
    def trading_strategy_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['trading_strategy_agent'], # type: ignore[index]
            verbose=True,  # Enable verbose output for the trading strategy agent
            tools=[self.search_tool, self.scrape_tool]  # Assigning tools to the agent
        )
    
    @agent
    def execution_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['execution_agent'], # type: ignore[index]
            verbose=True,  # Enable verbose output for the execution agent
            tools=[self.search_tool, self.scrape_tool]  # Assigning tools to the agent
        )
    
    @agent
    def risk_management_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['risk_management_agent'], # type: ignore[index]
            verbose=True,  # Enable verbose output for the risk management agent
            tools=[self.search_tool, self.scrape_tool]  # Assigning tools to the agent
        )
    
    @task
    def data_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['data_analysis_task'], # type: ignore[index]
        )
    
    @task
    def strategy_development_task(self) -> Task:
        return Task(
            config=self.tasks_config['strategy_development_task'] # type: ignore[index]
        )
    
    @task
    def execution_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['execution_planning_task'] # type: ignore[index]
        )
    
    @task
    def risk_assessment_task(self) -> Task:
        return Task(
            config=self.tasks_config['risk_assessment_task'] # type: ignore[index]
        )
    
    @crew
    def crew(self) -> Crew:
        try:
            return Crew(
                agents=[
                    self.data_analyst_agent(),
                    self.trading_strategy_agent(),
                    self.execution_agent(),
                    self.risk_management_agent()
                ],
                tasks=[
                    self.data_analysis_task(),
                    self.strategy_development_task(),
                    self.execution_planning_task(),
                    self.risk_assessment_task()
                ],
                manager_llm="gemini/gemini-2.0-flash",
                process=Process.hierarchical,
                verbose=True,  # Enable verbose output for the crew
            )
        except Exception as e:
            raise Exception(f"Failed to initialize Gemini LLM: {str(e)}")
        