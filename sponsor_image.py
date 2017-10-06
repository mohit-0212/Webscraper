import urllib3
import wget
from bs4 import BeautifulSoup
http = urllib3.PoolManager()
site = http.request('GET', ':http://www.udacity.com/intersect')
print(site.data)