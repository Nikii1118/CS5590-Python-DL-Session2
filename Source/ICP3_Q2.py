import requests
from bs4 import BeautifulSoup
import os
url="https://en.wikipedia.org/wiki/Deep_learning"
source_code=requests.get(url)
plain_text=source_code.text
soup=BeautifulSoup(plain_text,"html.parser")
#result_list=soup.findALL("a")
for div in soup.findAll('a'):
    print(div.get("href"))