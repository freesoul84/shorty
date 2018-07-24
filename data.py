
from urllib.request import urlopen
from bs4 import BeautifulSoup
url_page="https://en.wikipedia.org/wiki/Apple"
page = urlopen(url_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('div', attrs={'id': 'bodyContent'})
name = name_box.text.strip() # strip() is used to remove starting and trailing
print(name)
