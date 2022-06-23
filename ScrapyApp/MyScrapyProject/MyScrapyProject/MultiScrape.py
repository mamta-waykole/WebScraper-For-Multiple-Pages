import requests
from bs4 import BeautifulSoup as bs
from random import randint
from time import sleep
# One should enter website url which site will being scraped
# Refer legal terms before implementing this method of scraping
URL = ''

for page in range(1,150):
	

	req = requests.get(URL + str(page) + '/')
	soup = bs(req.text, 'html.parser')

	titles = soup.find_all('div',attrs={'class','head'})

	for i in range(4,19):
		if page>1:
			print(f"{(i-3)+page*15}=> " + titles[i].text)
		else:
			print(f"{i-3} -" + titles[i].text)

	sleep(randint(2,10))
