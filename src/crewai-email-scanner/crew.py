from crewai import Agent, Crew, Process, Task # type: ignore
from crewai.project import CrewBase, agent, crew, task # type: ignore

@CrewBase
class EmailScannerCrew():
    """EmailScannerCrew crew"""

    @agent
    def PolicyInterpreter(self) -> Agent:
        return Agent(
            config=self.agents_config['PolicyInterpreter'],
            tools=[],
        )

    @agent
    def PolicyDisplay(self) -> Agent:
        return Agent(
            config=self.agents_config['PolicyDisplay'],
            tools=[],
        )

    @agent
    def ContentScanner(self) -> Agent:
        return Agent(
            config=self.agents_config['ContentScanner'],
            tools=[],
        )

    @agent
    def AttachmentScanner_PDF(self) -> Agent:
        return Agent(
            config=self.agents_config['AttachmentScanner_PDF'],
            tools=[],
        )

    @agent
    def RecipientCheck(self) -> Agent:
        return Agent(
            config=self.agents_config['RecipientCheck'],
            tools=[],
        )

    @agent
    def DecisionMaker(self) -> Agent:
        return Agent(
            config=self.agents_config['DecisionMaker'],
            tools=[],
        )
    
    @agent
    def DecisionDisplay(self) -> Agent:
        return Agent(
            config=self.agents_config['DecisionDisplay'],
            tools=[],
        )

    @agent
    def LogRecorder(self) -> Agent:
        return Agent(
            config=self.agents_config['LogRecorder'],
            tools=[],
        )


    @task
    def interpret_policy_task(self) -> Task:
        return Task(
            config=self.tasks_config['interpret_policy_task'],
            tools=[],
        )

    @task
    def display_policy_task(self) -> Task:
        return Task(
            config=self.tasks_config['display_policy_task'],
            tools=[],
        )

    @task
    def scan_email_body_task(self) -> Task:
        return Task(
            config=self.tasks_config['scan_email_body_task'],
            tools=[],
        )

    @task
    def scan_pdf_attachments_task(self) -> Task:
        return Task(
            config=self.tasks_config['scan_pdf_attachments_task'],
            # tools=[PDFSearchTool()],
            tools=[],
        )

    @task
    def check_recipient_task(self) -> Task:
        return Task(
            config=self.tasks_config['check_recipient_task'],
            tools=[],
        )

    @task
    def decision_and_alert_task(self) -> Task:
        return Task(
            config=self.tasks_config['decision_and_alert_task'],
            tools=[],
        )
    
    @task
    def display_decision_task(self) -> Task:
        return Task(
            config=self.tasks_config['display_decision_task'],
            tools=[],
        )

    @task
    def logging_task(self) -> Task:
        return Task(
            config=self.tasks_config['logging_task'],
            tools=[],
        )


    @crew
    def crew(self, verbose=False) -> Crew:
        """Creates the EmailScannerCrew crew"""
        
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,

            
        )



