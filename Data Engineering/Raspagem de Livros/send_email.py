from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import smtplib
import json


f = open('e_mail.json')
data = json.load(f)
usr_email = data['email']
usr_password = data['password']
email_to = data['email_to']


def send_mail():

	"""Enviar e-mail de confirmação do scraping."""

	msg = MIMEMultipart()
	msg['From'] = usr_email
	msg['To'] = email_to
	msg['Subject'] = 'Python Scraping Books'

	text = "Hello!\n\nThis is an automated message.\nPlease, find attached the books' scraping csv file.\n\nRegards!"

	msg.attach(MIMEText(text, 'plain'))

	file_path = './book_scraping.csv'
	file_name = 'book_scraping.csv'
	
	part = MIMEBase('application', 'octet-stream')
	part.set_payload(open(file_path, 'rb').read())
	encoders.encode_base64(part)
	part.add_header('Content-Decomposition', 'attachmet', filename=file_name)
	msg.attach(part)


	s = smtplib.SMTP('smtp.live.com', 587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(usr_email, usr_password)
	s.sendmail(usr_email, email_to, msg.as_string())
	s.quit()
