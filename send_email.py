import smtplib, ssl
import os


def sen_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "piyush362002@gmail.com"
    password = os.getenv("passwordss")
    receiver = "piyush362002@gmail.com"
    context_l = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context_l) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)













