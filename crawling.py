import requests
from bs4 import BeautifulSoup
url = "https://section.cafe.naver.com/ca-fe/home"
response = requests.get(url, timeout=5)
soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())