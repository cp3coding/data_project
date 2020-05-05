# TODO
# 1. Make a request to the ebay.com and get a page
# 2.collect data from each detail page
# 3.collect all links to detail pages of each product
# 4.write scraped data to a csv file

import requests
from bs4 import BeautifulSoup
import csv

def get_page(url):
    response = requests.get(url)
    if not response.ok:
        print("Server responded:", response.status_code)
    else:
        soup = BeautifulSoup(response.text, "lxml")
    return soup

def get_detail_data(soup):
    #title
    #price
    #item sold
    try:
        title = soup.find('h1', class_="it-ttl").text.strip().split('\xa0')[1]
    except:
        title = ''

    try:
        price = soup.find("span", class_="notranslate").text.strip().encode("utf-8")
    except:
        price = ''

    try:
        sold = soup.find('a', class_= "vi-txt-underline").text.strip().split(' ')[0]
    except:
        sold = ''

    data = {
        'title': title,
        'price': price,
        'total sold': sold
    }


    return data

def get_index_data(soup):
    try:
        links = soup.find_all('a', class_='s-item__link')
    except:
        links = []
    urls = [item.get('href') for item in links]


    return urls

def write_csv(data, urls):
    with open('output_ebay_laptop.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)

        row = [data["title"], data['price'], data['total sold'], urls]

        writer.writerow(row)

def main():
    url = 'https://www.ebay.com/sch/i.html?_nkw=laptop&_pgn=1'
    products = get_index_data(get_page(url))

    for link in products:
        data = get_detail_data(get_page(link))
        write_csv(data, link)



if __name__ == "__main__":
    main()