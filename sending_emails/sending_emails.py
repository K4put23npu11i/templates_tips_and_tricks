import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import user_and_pw_information
(sender, sender_pw) = user_and_pw_information.sender()
recipients = user_and_pw_information.recipients()

if "gmail" in sender:
    host = "smtp.gmail.com"
    port = 465
else:  # outlook
    host = "smtp.office365.com"
    port = 587

subject = "This is a test mail from python"
body = """Hello there,
    this is a very short text to test the functionality to send mails...
    
    Yours sincerely,
    Python ;)"""


def send_mail(sender, sender_pw, recipient, subject, body, host, port):
    msg = MIMEMultipart()
    msg['From'] = sender  # senders email address
    msg['To'] = recipient  # receivers email address
    msg['Subject'] = subject
        
    msg.attach(MIMEText(body, 'plain'))  # attach the body with the msg instance
    
    s = smtplib.SMTP(host, port)
    s.starttls()  # start TLS for security
    s.login(sender, sender_pw)  # Authentication
    text = msg.as_string()  # Converts the Multipart msg into a string
    s.sendmail(sender, recipient, text)  # sending the mail
    s.quit()
    return "Done"


for recipient in recipients:
    print(recipient)
    send_mail(sender, sender_pw, recipient, subject, body, host, port)
