from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time


def scrap_books():

	"""Function to scrape books from www.books.toscrape.com and save in a csv file."""

	# get number of pages
	url1 = 'http://books.toscrape.com/'
	page = urlopen(url1)
	page_html = page.read()
	page.close()
	page_soup = BeautifulSoup(page_html, 'html.parser')
	pages = page_soup.find('li', class_='current')
	num_pages = pages.text.strip()
	num_pages = int(num_pages.split()[-1])

	# set url
	url = 'https://books.toscrape.com/catalogue/page-{}.html'

	titles = []
	prices = []
	ratings = []
	availability = []

	# loop over pages
	for i in range(1,num_pages+1):

		# get url
		url_ = url.format(i)
		# open, read, and close page
		page = urlopen(url_)
		page_html = page.read()
		page.close()
		# parse page
		page_soup = BeautifulSoup(page_html, 'html.parser')
		# get books
		books = page_soup.findAll('li',
								'col-xs-6 col-sm-4 col-md-3 col-lg-3')
		# loop over books on page
		for book in books:

			title = book.h3.a['title']
			titles.append(title)

			price_color = book.findAll('p', {'class':'price_color'})
			price = price_color[0].text.strip()[1:]
			prices.append(price)

			instock_availability = book.findAll('p',{'class':'instock availability'})
			available = instock_availability[0].text.strip()
			availability.append(available)

			rating = book.find('p', {'class':'star-rating'}).attrs['class'][1]
			ratings.append(rating)


	# create df
	df = pd.DataFrame({'Title':titles, 'Price (£)':prices, 
						'Rating':ratings, 'In Stock':availability})


	# save scrapping on csv file
	df.to_csv('book_scraping.csv', index=False)


# schedule scrapping to everyday at 12:00
schedule.every().day.at('12:00').do(scrap_books)

while True:
	schedule.run_pending()
	time.sleep(1)