import json
import os
import io
import requests
from bs4 import BeautifulSoup as BS
try:
    to_unicode = unicode
except NameError:
    to_unicode = str
site = requests.get('https://developer.apple.com/wwdc/more/')
data = site.content.decode('utf-8')
Soup = BS(data, 'lxml')
path = "Apple WWDC/Data/Special Events/Third Party Events"
if not os.path.exists(path):
    os.makedirs(path)
with io.open('Apple WWDC/Data/Special Events/Third Party Events/ThirdPartyEvents_data.json', 'w', 
    encoding='utf8') as outfile:
    events = {'name': [], 'description': [], 'location': [], 'date-day': []}
    for ele in Soup.find_all('h4'):
        events['name'].append(ele.text)
    for ele in Soup.find_all('p', {'class': 'description'}):
        events['description'].append(
            ele.text.replace("\t", "").replace("\n", ""))
    for ele in Soup.find_all('p', {'class': 'location'}):
        events['location'].append(ele.text.replace("\t", "").replace("\n", ""))
    dates = Soup.find_all('p', {'class': 'date'})
    days = Soup.find_all('p', {'class': 'day'})
    for x in range(len(days)):
        day_date = dates[x].text.replace("\t", "").replace("\n", "") + ", " 
        + days[x].text.replace("\t", "").replace("\n", "")
        events['date-day'].append(day_date)

    str_ = json.dumps(events, indent=2, sort_keys=False,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))