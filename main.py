import smtplib
from email.mime.text import MIMEText

recipients = []
subject = str(input("Insira o assunto do Email: "))
body = str(input("Insira o corpo do Email: "))
sender = "--Seu Email Aqui--"
password = '--Sua Senha Aqui--'
receiver = str(input("Insira quem receberá o Email: "))
recipients.append(receiver)



def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Email Enviado!")


send_email(subject, body, sender, recipients, password)
