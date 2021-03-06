import json
import os
import io
import requests
from bs4 import BeautifulSoup as BS
try:
    to_unicode = unicode
except NameError:
    to_unicode = str
site = requests.get('https://developer.apple.com/wwdc/guest-speakers/')
data = site.content.decode('utf-8')
Soup = BS(data, 'lxml')
path = "Apple WWDC/Data/Guest Speakers/"
if not os.path.exists(path):
    os.makedirs(path)
with io.open('Apple WWDC/Data/Guest Speakers/GuestSpeakers_data.json', 'w', encoding='utf8') as outfile:
    guest = {'speakers': [], 'description': [], 'date-time': []}
    for ele in Soup.find_all('p', {'class': 'heading'}):
        guest['speakers'].append(ele.text)
    for ele in Soup.find_all('p', {'class': 'description'}):
        guest['description'].append(
            ele.text.replace("\t", "").replace("\n", ""))
    for ele in Soup.find_all('p', {'class': 'date-time'}):
        guest['date-time'].append(ele.text.replace("\t", "").replace("\n", ""))

    str_ = json.dumps(guest, indent=2, sort_keys=False,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
