import email
import smtplib
import json


f = open('e_mail.json')
data = json.load(f)
usr_email = data['email']
usr_password = data['password']
email_to = data['email_to']

message = "Hello!\nThis is an automated message.\nScraping completed with success!\n\nRegards!"

def send_mail():

	"""Enviar e-mail de confirmação do scraping."""

	msg = email.message_from_string(message)
	msg['From'] = usr_email
	msg['To'] = email_to
	msg['Subject'] = 'Python Scraping Books'

	s = smtplib.SMTP('smtp.live.com', 587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(usr_email, usr_password)
	s.sendmail(usr_email, email_to, msg.as_string())
	s.quit()
