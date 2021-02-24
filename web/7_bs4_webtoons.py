import requests
from bs4 import BeautifulSoup 

url = "https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")  # lxml document pathway.

# extracting all NAVER WEBTOON cartoons:
cartoons = soup.find_all("a", attrs={"class":"title"})
for cartoon in cartoons:
	print(cartoon.get_text())

