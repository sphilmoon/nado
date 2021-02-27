import requests
from bs4 import BeautifulSoup
import re

url = "https://www.coupang.com/np/search?q=macbook+pro&channel=auto&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
res = requests.get(url)
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "lxml")  # lxml document pathway.

items = soup.find_all("li", attrs={"class":re.compile("^search-product-wrap")})
# print(items[1].find("div", attrs={"class":"name"}).get_text())
# print(res.text)

for item in items:
	ad_bagde = item.find("span", attrs={"class":"ad-badge-text"})
	if ad_bagde:
		print("	<excluding promotion items>")
		continue

	name = items[1].find("div", attrs={"class":"name"}).get_text()
	price = items[1].find("strong", attrs={"class":"price-value"}).get_text()


	rating = itmes[1].find("em", attrs={"class":"rating"})
	if rating is none:
		# rating = "No ratings"
		print(" <0 rating items excluded>")
		continue
	else:
		rating = rating.get_text()

	review = itmes[1].find("span", attrs={"class":"rating-total-count"})
	if review is none:
		# review = "No reviews"
		print(" <0 review items excluded>")
		continue
	else:
		review = review.get_text()
		review = review[1:-1]

	if float(rating) >= 4.0 and int(review) >= 50:
		print(name, price, rating, review)