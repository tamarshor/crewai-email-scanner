#!/usr/bin/env python
import sys
import os
from crew import EmailScannerCrew
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv # type: ignore
# Load environment variables from .env
load_dotenv()

def run(user_inputs):
    
    """
    Prepare the inputs for the crew.
    """
    
    """Returns the current timestamp in a nicely formatted string."""
    timestamp_now = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

    # Get input values (provided by the user in the web form)
    policy_text = user_inputs.get("policy_text", "")
    email_body_text = user_inputs.get("email_body_text", "")
    attachment_text = user_inputs.get("attachment_text", "")
    recipient_email = user_inputs.get("recipient_email", "")

    # Assuming 'config' folder is at the same level as the script
    config_dir = Path(__file__).parent / 'config'
    approved_recipient_file_path = config_dir / 'approved-recipient.txt'
    
    # Read the approved recipient file (includes the list of approved recipients that are allowed to receive sensitive content)
    with open(approved_recipient_file_path, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()  # Reads full content and splits it into lines
    
    print(f"""
    \n Policy: {policy_text}
    \n Email body: {email_body_text}
    \n Email attachment: {attachment_text}
    \n Email recipient: {recipient_email}
    \n Approved recipient: {lines}
    """)

    inputs = {
        'policy_document': policy_text,
        'structured_policy_rules': 'sample_value',
        'email_content': email_body_text,
        'attachments': attachment_text,
        'recipient_email': recipient_email,
        'approved_recipient_list': lines,
        'admin_email': 'tamarshor1@gmail.com',
        'sender_email': 'tamarshor1@gmail.com',
        'timestamp': timestamp_now,
        'url_policy_rules': 'sample_value'
    }

    """
    Run the crew with the inputs.
    using return result to send back the result to the web app to allow for user interaction 
    """
    
    result = EmailScannerCrew().crew().kickoff(inputs=inputs)
    return result

    '''
    EXIT SCRIPT
    '''
    print("Exiting script...")
    sys.exit()

    

'''
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
        EmailScannerCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    # Replay the crew execution from a specific task.
    """
    try:
        EmailScannerCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    # Test the crew execution and returns the results.
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
        EmailScannerCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
    
'''

#run()

"""
if __name__ == "__main__":
   
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        print("Running crew...")
        run()
    elif command == "train":
        print("Training crew...")
        train()
    elif command == "replay":
        print("Replaying crew...")
        replay()
    elif command == "test":
        print("Testing crew...")
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
else:
    print("OOPS...")
    sys.exit(1)

    """
      
