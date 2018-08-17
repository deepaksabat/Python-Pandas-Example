import urllib
from bs4 import BeautifulSoup
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
   print(html)
# soup = BeautifulSoup(htmlSource)
# print(soup.prettify())