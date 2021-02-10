import urllib
from bs4 import BeautifulSoup
import pandas as pd


def scrap_books():

	"""Function to scrape books from www.books.toscrape.com and save in a csv file."""

	url_t = 'http://books.toscrape.com/'

	try:
		page = urllib.request.urlopen(url_t)
	except urllib.error.HTTPError as e_http:
		print('HTTPError: {}'.format(e_http.code))
	except urllib.error.URLError as e_url:
		print('URLError: {}'.format(e_url.reason))

	page_html = page.read()
	page.close()
	page_soup = BeautifulSoup(page_html, 'html.parser')
	pages = page_soup.find('li', class_='current')
	num_pages = pages.text.strip()
	num_pages = int(num_pages.split()[-1])

	url = 'https://books.toscrape.com/catalogue/page-{}.html'

	titles = []
	prices = []
	ratings = []
	availability = []

	for i in range(1,num_pages+1):

		url_ = url.format(i)
		try:
			page = urllib.request.urlopen(url_)
			page_html = page.read()
			page.close()
			page_soup = BeautifulSoup(page_html, 'html.parser')
			books = page_soup.findAll('li',
									'col-xs-6 col-sm-4 col-md-3 col-lg-3')
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

		except urllib.error.HTTPError as e_http:
			# code error e.g. 404, 501, ...
			print('HTTPError: {}'.format(e_http.code))
		except urllib.error.URLError as e_url:
			# HTTP-error e.g. connection refused
			print('URLError: {}'.format(e_url.reason))


	df = pd.DataFrame({'Title':titles, 'Price (£)':prices, 
						'Rating':ratings, 'In Stock':availability})

	df.to_csv('book_scraping.csv', index=False)

