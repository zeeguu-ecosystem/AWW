import requests

import smtplib
from getpass import getpass
from email.mime.text import MIMEText
import os

URL_TO_TEST="https://zeeguu.org/"
TOO_SLOW_THRESHOLD=1 # in seconds

def notify_by_email(title, content):

	send_email(
		os.environ["WATCHDOG_EMAIL"] , 
		os.environ["WATCHDOG_PASS"], 
		os.environ["THE_WOLF_EMAIL"], # I'm the Wolf. I solve problems. 
		title, 
		content)


def send_email(user, pwd, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
    
    except:
        print ("failed to send mail")


try:
	response = requests.post(URL_TO_TEST)
	elapsed_time = response.elapsed.total_seconds()
	print(elapsed_time)
	if ( elapsed_time > TOO_SLOW_THRESHOLD ):
		notify_by_email("API STATUS: slow",
			f"{URL_TO_TEST} took: {elapsed_time} seconds")

except Exception as e: 
	notify_by_email("API STATUS: offline?", f"{URL_TO_TEST} could not be reached. Exception: " + str(e))

