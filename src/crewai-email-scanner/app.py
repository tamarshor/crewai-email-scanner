from flask import Flask, render_template, request
import main  # Import main.py

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Show input form

@app.route("/run_crewai", methods=["POST"])
def run_crewai():
    # Get input values from form
    policy_text = request.form.get("policy_text")
    email_body_text = request.form.get("email_body_text")
    attachment_text = request.form.get("attachment_text")
    recipient_email = request.form.get("recipient_email")

    # Prepare inputs dictionary for main.py
    inputs = {
        'policy_text': policy_text,
        'email_body_text': email_body_text,
        'attachment_text': attachment_text,
        'recipient_email': recipient_email
    }

    # Run CrewAI with inputs
    result = main.run(inputs)

    return render_template("result.html", output=result)  # Show CrewAI output

if __name__ == "__main__":
    app.run(debug=True)