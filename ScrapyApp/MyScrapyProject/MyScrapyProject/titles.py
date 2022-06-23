import requests
from bs4 import BeautifulSoup
import csv
# brings data
html_text = requests.get("https://www.geeksforgeeks.org/python-web-scraping-tutorial/").text
soup = BeautifulSoup(html_text, 'lxml')
titles = soup.find_all('div', attrs={'class', 'head'})
titles_list = []

# sets serial numbers for data records
count = 1
for title in titles:
	d = {}
	d['Title Number'] = f'Title {count}'
	d['Title Name'] = title.text
	count += 1
	titles_list.append(d)

# create csv file and stores data in simple text format in csv file
filename = 'titles.csv'
with open(filename, 'w', newline='') as f:
	w = csv.DictWriter(f,['Title Number','Title Name'])
	w.writeheader()
	
	w.writerows(titles_list)