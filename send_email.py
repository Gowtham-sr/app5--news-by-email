import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    # send_email function uses the Gmail username and password of the person who owns the Gmail account
    # to authenticate the connection,
    # regardless of who the sender of the email is.

    username = "gowthamsr49@gmail.com"
    password = "dalsxvmskrtqjckg"
    # Storing password in environment variable. Letting python get the actual passwd from computer.

    receiver = "gowthamsr49@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
