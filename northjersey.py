from bs4 import BeautifulSoup as bs
import requests
import csv
import re
url = "https://www.dailyrecord.com/news/"
r = requests.get(url)

r_html = r.text

soup = bs(r_html, 'lxml')

for link in soup.find_all('a'):
    if link.a.h1.text != ""
    result = link.get("href")
    csv_writer.writerow([result])
'''''csv_file = open("northjersey_title1.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["headline", "result"])
news = soup.find("div", class_="flm-module-wrap gallery-mosaic short-headlines inline-video js-lazy-load js-ad-cleanup")

for new in news.find_all("div", class_="flm-bundle js-llc"):
    result = new.find_all('a')['href']
    headline = new.a.h1.text
    # headline = new.a.h1.text
    print(headline)
    print(result)
    csv_writer.writerow([headline, result])'''''






# csv_file = open("northjersey_title.csv", "w")
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(["headline", "result"])
# for title in soup.find_all("span", class_ ="js-asset-headline js-asset-headline-short"):
#     headline = title.contents
#
#     csv_writer.writerow([headline])
# for link in soup.find_all('a'):
#     result = link.get("href")
#     csv_writer.writerow([result])
# csv_file.close()



