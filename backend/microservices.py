import os
from dotenv import load_dotenv

from email.message import EmailMessage
import smtplib

load_dotenv()

def sec_to_minute(secs: int):
    minutes = secs / 60
    return int(minutes)

def sendEmail(battery_percent: float, plugged: bool):
    sender = os.getenv("EMAIL_SENDER")
    receiver = os.getenv("EMAIL_RECEIVER")
    password = os.getenv("GOOGLE_PASSWORD")

    emailmessage = EmailMessage()

    emailmessage["Subject"] = "Alerta: bateria do notebook"
    emailmessage["From"] = sender
    emailmessage["To"] = receiver

    if battery_percent == 95 and plugged:
        emailmessage.set_content(
            f"""
            Fique atento!

            A bateria do seu notebook chegou a {battery_percent:.0f}%
            """
        )
    elif battery_percent == 100 and plugged:
        emailmessage.set_content(
            f"""
            Oi!

            Seu notebook atingiu 100% de bateria. Hora de remover o carregador.
            """
        )
    elif battery_percent <= 5 and not plugged:
        emailmessage.set_content(
            f"""
            Olá!

            Vim te avisar que a bateria do seu notebook está extremamente baixa. É hora de colocar ele para carregar; não o deixe morrer!
            """
        )

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

        smtp.starttls()

        smtp.login(
            sender,
            password.replace(" ", "")
        )

        smtp.send_message(emailmessage)

    