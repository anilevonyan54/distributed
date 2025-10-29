import time
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(to, subject, body):
    print(f"[Task] Sending email to {to}...")
    time.sleep(2)
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = to
    msg.set_content(body)
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL, PASSWORD)
            smtp.send_message(msg)
        print(f"[Task] Email sent to {to}")
        return f"Email successfully sent to {to}"
    except Exception as e:
        print(f"[Task] Email failed: {e}")
        return f"Failed to send email: {e}"
