import urllib.request


from bs4 import BeautifulSoup

import pprint

url = ("http://books.toscrape.com/catalogue/category/books_1/index.html")

ques = urllib.request.urlopen(url)

soup = BeautifulSoup(ques.read(), "html.parser")

print(soup.select(".btn btn-primary btn-block"))
 

