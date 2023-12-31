import smtplib
from email.message import EmailMessage
from core.settings import EMAIL, PASSWORD

def send_mail(email, name):
    try:
        #making connection with server
        email_server = smtplib.SMTP('smtp.gmail.com', 587)
        email_server.starttls()
        email_server.login(EMAIL,PASSWORD)#this is this app token

        sender = EMAIL
        recipient = email
        message = EmailMessage()
        message['Subject'] = 'Here is your invite'
        message_body = f"""

                    <h1>Good Morning!! {name}\n</h1>
                    <h4>You have asked for a invite, so, there is your invite!!</h4>
                    <img src="/home/davi/DEV/GIT/Celery/Celery/media/card.png"></img>

                        """
        message.add_header('Content-Type', 'text/html')
        message.set_payload(message_body)

        email_server.sendmail(sender, recipient, message.as_string().encode('utf-8'))
        email_server.quit()

    except Exception as e:
        print(e)
        return f'Error: {e}'