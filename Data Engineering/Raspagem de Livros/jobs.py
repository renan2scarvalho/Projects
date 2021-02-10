import schedule
import time
from book_scraping import scrap_books
from send_email import send_mail

schedule.every().day.at('11:56').do(scrap_books)
schedule.every().day.at('11:56').do(send_mail)

while True:
	schedule.run_pending()
	time.sleep(60)