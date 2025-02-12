#!/usr/bin/env python
import sys
from email_crew_automates_sensitive_data_checking.crew import EmailCrewAutomatesSensitiveDataCheckingCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'policy_document': 'sample_value',
        'structured_policy_rules': 'sample_value',
        'email_content': 'sample_value',
        'attachments': 'sample_value',
        'recipient_email': 'sample_value',
        'crm_customer_list': 'sample_value',
        'admin_email': 'sample_value',
        'sender_email': 'sample_value',
        'timestamp': 'sample_value'
    }
    EmailCrewAutomatesSensitiveDataCheckingCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'policy_document': 'sample_value',
        'structured_policy_rules': 'sample_value',
        'email_content': 'sample_value',
        'attachments': 'sample_value',
        'recipient_email': 'sample_value',
        'crm_customer_list': 'sample_value',
        'admin_email': 'sample_value',
        'sender_email': 'sample_value',
        'timestamp': 'sample_value'
    }
    try:
        EmailCrewAutomatesSensitiveDataCheckingCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        EmailCrewAutomatesSensitiveDataCheckingCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'policy_document': 'sample_value',
        'structured_policy_rules': 'sample_value',
        'email_content': 'sample_value',
        'attachments': 'sample_value',
        'recipient_email': 'sample_value',
        'crm_customer_list': 'sample_value',
        'admin_email': 'sample_value',
        'sender_email': 'sample_value',
        'timestamp': 'sample_value'
    }
    try:
        EmailCrewAutomatesSensitiveDataCheckingCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
