import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# AWS SES SMTP server details
smtp_server = 'email-smtp.eu-central-1.amazonaws.com'
smtp_port = 587

# Your AWS SES SMTP credentials
smtp_username = 'AKIATCKASLP7YQNAET4E'
smtp_password = 'BE/FsFErTKDstWEsiqr8LzcoZMSjBFHRgwJMzKHN7d9/'

sender_email = 'mail@mail.framewise.ai'  # Updated sender email address
recipient_email = 'kowshik@framewise.ai'

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = 'Test Email from AWS SES'

body = 'This is a test email sent from Amazon SES using SMTP.'
message.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP(smtp_server.format(region='your-region'), smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, recipient_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print("Error: ", e)
finally:
    server.quit()
