"""Interact with mail services."""
import smtplib


def sendMail(sender, password, recipient, content, iters):
    """Send an email."""
    try:
        mail = smtplib.SMTP('64.233.184.108', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(sender, password)
        for x in range(iters):
            mail.sendmail(sender, recipient, content)
        mail.close()
        return True
    except Exception:
        return False
