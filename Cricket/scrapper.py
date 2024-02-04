import sys
import time
from urllib.error import URLError
from bs4 import BeautifulSoup
import requests

try:

    page = requests.get('https://www.cricbuzz.com/')  

except Exception as er:
    error_type, error_obj, error_info = sys.exc_info()
    print('ERROR FOR LINK:', URLError)
    print(error_type, 'Line:', error_info.tb_lineno)

time.sleep(3)
scrap = BeautifulSoup(page.text, 'html.parser')
links = scrap.find_all('div', attrs={'class':'cb-nws-intr'})
date = scrap.find_all('div', attrs={'class':'crd-cntxt'})



for info in links:
    print(info.text + "\n")
for dat in date:
     print(dat.text)

