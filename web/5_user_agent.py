import requests

url = "https://naver.com"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

with open("naver.html", "w", encoding="utf8") as file:
	file.write(res.text)