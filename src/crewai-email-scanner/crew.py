from crewai import Agent, Crew, Process, Task # type: ignore
from crewai.project import CrewBase, agent, crew, task # type: ignore
# from crewai_tools import PDFSearchTool # type: ignore
import logging

# Create a custom logger for your application (or for Crew AI if configurable)
logger = logging.getLogger('crewAI')
logger.setLevel(logging.DEBUG)  # Capture all levels; filtering is done in handlers

# Create handlers
console_handler = logging.StreamHandler()  # For main outputs (e.g., results)
file_handler = logging.FileHandler('verbose_logs.txt')  # For verbose chain-of-thought

# Set handler levels
console_handler.setLevel(logging.INFO)  # Only show info and above on console
file_handler.setLevel(logging.DEBUG)    # Capture debug (verbose) logs to file

# Create formatters and assign them to handlers
console_formatter = logging.Formatter('%(message)s')
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)



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
        if verbose:
            logger.debug("Starting Crew AI task with detailed reasoning (verbode = True) ...")
    
        # Simulate main processing and final output
        result = "Final result of the task."
        logger.info(result)
    
        if verbose:
            logger.debug("Crew AI task completed with additional reasoning logs.")

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,

            
        )



