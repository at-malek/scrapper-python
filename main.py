import math
import requests
import csv
from bs4 import BeautifulSoup

DEFAULT_TEXT = "No Phone Found"


def extractPrice(price):
  price = price.replace(',', '')
  for word in price.split():
    if word.isdigit():
      return int(word)

  return None


def main():
  URL = "https://www.whatmobile.com.pk/"
  r = requests.get(URL)

  f = open('task1.csv', 'w+')
  writer = csv.writer(f)
  writer.writerow(["Product name","Price"])

  highest_name = DEFAULT_TEXT
  lowest_name = DEFAULT_TEXT

  highest_price = 0
  lowest_price = math.inf

  soup = BeautifulSoup(r.content, 'html5lib')


  for row in soup.findAll('li', attrs={'class':'product'}):
    name = row.h4.a['title']
    price = row.span.text
    writer.writerow([name, price])
    # print(name, "\n", price)
    # print("\n")

    price_val = extractPrice(price)
    if price_val > highest_price:
      highest_price = price_val
      highest_name = name

    if price_val < lowest_price:
      lowest_price = price_val
      lowest_name = name

  f.close()
  f = open('task2.csv', 'w+')
  writer = csv.writer(f)
  writer.writerow(["Product Name","Price"])
  writer.writerow(["Highest Price Product"])
  writer.writerow([highest_name, str(highest_price)])
  writer.writerow(["Lowest Price Product"])
  writer.writerow([lowest_name, str(lowest_price)])
  f.close()

  f = open('task3.csv', 'w+')
  writer = csv.writer(f)
  writer.writerow(["BRAND NAMES"])
  table = soup.find('div', attrs={'class':'verticalMenu'})
  sections = table.findAll('section')
  items = sections[1].findAll('li')
  for item in items:
    writer.writerow([item.a.text])




if __name__ == "__main__":
  main()

#DONE: TODO Task1: Get all Phones on main page: name and price and store them in csv file
#DONE: TODO Task2: Get highest and lowest price phone and store them in 2nd csv file
#DONE: TODO Task3: Get All Phone Brands name from "search by brand" and store that in seperate csv file
