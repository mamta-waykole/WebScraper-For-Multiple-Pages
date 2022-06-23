from __future__ import barry_as_FLUFL
import csv
from email import header
from bs4 import BeautifulSoup
import requests
from csv import writer
import os

html_text = requests.get("https://www.dexciss.com").text

soup = BeautifulSoup(html_text, 'lxml')
estate = soup.find_all('div',class_ = 'mb-srp__card__container')
# print(estate)

# create csv file
with open('estate.csv','w',encoding='utf8',newline='') as f:
    thewriter = writer(f)
    header = ['Society Name','Area','Builder']
    thewriter.writerow(header)
    for e in estate:
        society_name = e.find('div',class_ = 'mb-srp__card__society').text.replace(' ',' ')
        area = e.find('div',class_ = 'mb-srp__card__summary--value').text.replace(' ',' ')
        builder = e.find('div',class_ = 'mb-srp__card__ads--name').text.replace(' ',' ')
        info = [society_name.strip(),area.strip(),builder.strip()]
        thewriter.writerow(info)

# with open ("/home/mamta/ScrapyApp/MyScrapyProject/estate.csv","r") as file:

#  Takes above path of csv file dinamically in case one want to save the file on particular location
csv_path = './estate.csv'

abs_path = os.path.abspath(csv_path)
print("**+**",abs_path)

with open (str(abs_path),"r") as file:

    reader = csv.reader(file)
    print("*****+++++++*****",reader)
    for each in reader:
        print("****************************",each)
        



