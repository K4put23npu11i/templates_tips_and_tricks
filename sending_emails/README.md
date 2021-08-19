# Sending mails with Python
## Why use it?
- For notifications or alerts
- For regular information about something

## How does it work?
The script uses the `smtp library` to send the mails.
In addition there is a `user_and_pw_information.py` file needed. It includes the following two functions:
```
def sender():
    sender = "mail@sender.com"
    sender_pw = "sender_password"
    return sender, sender_pw

def recipients():
    recipients = ["recipient1@gmail.com", "recipient2@gmail.com"]
    return recipients
```

The file is included in a `.gitignore` to securly store user information about sender and reciever. The information will be called from the actual file.

## Sources
- [towards Data Science - Example]( https://towardsdatascience.com/automate-sending-emails-with-gmail-in-python-449cc0c3c317)
