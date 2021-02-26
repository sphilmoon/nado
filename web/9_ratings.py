import requests
from bs4 import BeautifulSoup 

url = "https://comic.naver.com/webtoon/list.nhn?titleId=736989&weekday=thu"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")  # lxml document pathway.
cartoons = soup.find_all("div", attrs={"class":"rating_type"})

total_rating = 0
for cartoon in cartoons:
	rating = (cartoon.find("strong").get_text())
	# print(rating)
	total_rating += float(rating)
	formatted_total = "{:.3f}".format(total_rating)

print("TOTAL: ", formatted_total)
print("AVERAGE: ", total_rating / len(cartoons))
