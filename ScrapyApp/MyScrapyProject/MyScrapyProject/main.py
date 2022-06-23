from email import header
from bs4 import BeautifulSoup
import requests
from csv import writer

# url = "https://www.linkedin.com/pulse/topics/home/?trk=homepage-basic_guest_nav_menu_discover"
# page = requests.get(url)


# soup = BeautifulSoup(page.content , 'html.parser')

# lists = soup.find_all('li', class_= "topic-article-card")
# for list in lists:
#   title = list.find('h3',class_="base-main-card__title").text.replace('\n','')
# #   designation = list.find ('h4')
#   role = list.find('p',class_="topic-article-card__summary").text.replace('</p>','')

#   info = [title,role]
#   print(info)




html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Senior+Software+Developer&txtLocation=Pune").text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')

# To open csv file automatically with data
with open('main.csv','w',encoding='utf8',newline='') as f:
    thewriter = writer(f)
    header = ['Company','Skills','Experience']
    thewriter.writerow(header)
    for job in jobs:
        company_name = job.find('h3',class_ = 'joblist-comp-name').text.replace(' ',' ')
        skills = job.find('span',class_ = 'srp-skills').text.replace(' ','')
        exp = job.find('ul',class_ = 'top-jd-dtl clearfix').text.replace('card_travel','')
        info = [company_name.strip(),skills.strip(),exp.strip()]
        thewriter.writerow(info)

        print('')





# from email import header
# from bs4 import BeautifulSoup
# import requests
# from csv import writer

# html_text = requests.get("https://www.magicbricks.com/flats-in-pune-for-sale-pppfs?mbtracker=google_paid_brand_desk_pune&ccode=brand_sem&gclid=CjwKCAjwy_aUBhACEiwA2IHHQIrPqqaG1E2bYqFa-qFTuI48ngl12ucLQsakhd1dNlYRxe1quT7-lBoC5ywQAvD_BwE").text

# soup = BeautifulSoup(html_text, 'lxml')
# estate = soup.find_all('div',class_ = 'mb-srp__card__container')
# print(estate)


# with open('estate.csv','w',encoding='utf8',newline='') as f:
#     thewriter = writer(f)
#     header = ['Society Name','Area','Type']
#     thewriter.writerow(header)
#     for e in estate:
#         Society_Name = e.find('div',class_ = 'mb-srp__card__society').text.replace(' ',' ')
#         area = e.find('div',class_ = 'mb-srp__card__summary__list--item').text.replace(' ','')
#         type = e.find('div',class_ = 'mb-srp__card__summary--value').text.replace('card_travel','')
#         info = [Society_Name.strip(),area.strip(),type.strip()]
#         thewriter.writerow(info)

#         print('')