import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_feedback_email(to_email, score, feedback):
    from_email = "your_email@gmail.com"
    from_password = "your_password"
    
    subject = "Your Resume Scoring and Feedback"
    body =  f"Dear Candidate,\n\nThank you for submitting your resume. Here is your score and feedback:\n\n" \
            f"CV Score: {score}\n\n" \
            f"Feedback: {feedback}\n\nBest regards,\nResume Scoring AI Agent"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(from_email, from_password)
            server.sendmail(from_email, to_email, msg.as_string())
        print(f"Feedback email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_feedback_email(to_email, score, feedback):
    from_email = "your_email@gmail.com"
    from_password = "your_password"
    
    subject = "Your Resume Scoring and Feedback"
    body =  f"Dear Candidate,\n\nThank you for submitting your resume. Here is your score and feedback:\n\n" \
            f"CV Score: {score}\n\n" \
            f"Feedback: {feedback}\n\nBest regards,\nResume Scoring AI Agent"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(from_email, from_password)
            server.sendmail(from_email, to_email, msg.as_string())
        print(f"Feedback email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")