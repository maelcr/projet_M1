import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your email credentials
sender_email = "projet.detection.poussin.mort@gmail.com"
receiver_email = "courtinambroise@gmail.com"
password = "lepouletcesttropbon"

# Create the email content
subject = "Hello from Python!"
body = "This is a test email sent from Python."

# Set up the MIME structure
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Establish a secure connection with the SMTP server
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully!")