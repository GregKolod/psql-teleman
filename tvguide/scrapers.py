from urllib.request import urlopen
from bs4 import BeautifulSoup


quote_page = 'https://www.teleman.pl/program-tv/stacje/TVP-1?hour=-1'

page = urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')


ul_tag = soup.find('ul', attrs={'class': 'stationItems'})  # ul_tag = soup.find('ul', class_='stationItems')
# print(ul_tag)

print('------------------------------------------------')

for li in ul_tag.find_all('li'):
    em = li.find('em')
    div = li.find('div', attrs={'class': 'detail'})
    if em:
        print(em.text + ':\t' + div.find('a').text)

print('================================================')