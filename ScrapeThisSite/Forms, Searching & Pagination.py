
import requests, os
from bs4 import BeautifulSoup as bs

# import pandas as pd
# all_tables = pd.read_html(link)

try: os.mkdir('Scrapped')
except: pass

link = 'https://www.scrapethissite.com/pages/forms/?page_num=1&per_page=25'
req = requests.get(link)
soup = bs(req.content, 'html5lib')

table = soup.findAll('table', attrs = {'class':'table'})[0]
for i in table:
    tr = table.findAll('tr')
    print(tr)
