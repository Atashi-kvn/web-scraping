import sys
import time
from bs4 import BeautifulSoup
import requests

try:

    page = requests.get('')  #place the link in the('#') just like the # 

except Exception as er:
    error_type, error_obj, error_info = sys.exc_info()
    print('ERROR FOR LINK:', url)
    print(error_type, 'Line:', error_info.tb_lineno)

time.sleep(3)
scrap = BeautifulSoup(page.text, 'html.parser')
links = scrap.find_all('div', attrs={'class':'cb-nws-intr'})  # in between the () place the html tags with the info you targeting

# page

# scrap

# links

for info in links:
    print(info.text + "\n")
