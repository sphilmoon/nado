import requests
from bs4 import BeautifulSoup 

url = "https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")  # lxml document pathway.
# print(soup.title)  # title in html format.
# print(soup.title.get_text())  # just the text.
# print(soup.a)  # the first a element. 
# print(soup.a.attrs) # attributes in dictionary.
# print(soup.a["href"])  # value of "href" key.

# print(soup.find("a", attrs={"class":"Nbtn_upload"}))

# rank1 = soup.find("li", attrs={"class":"rank01"})
# # print(soup.find("li", attrs={"class":"rank01"}))
# print(rank1.a.get_text())
# # print(rank1.next_sibling)
# # print(rank1.next_sibling.next_sibling) # there are a new line change, so twice the argument.
# # rank2 = rank1.next_sibling.next_sibling
# # rank3 = rank2.next_sibling.next_sibling
# # # print(rank3.a.get_text())

# # rank4 = rank3.previous_sibling.previous_sibling
# # print(rank4.a.get_text())
# # print(rank1.parent)

# # rank2 = rank1.find_next_sibling("li")
# # print(rank2.a.get_text())
# # rank3 = rank2.find_next_sibling("li")
# # print(rank3.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="독립일기-64화 혼자라서 난감한")
print(webtoon)