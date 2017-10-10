import urllib3
import wget
import os
from bs4 import BeautifulSoup

urllib3.disable_warnings()
http = urllib3.PoolManager()
site = http.request('GET','https://www.udacity.com/intersect/agenda')
data = site.data
soup = BeautifulSoup(data,'html.parser')
schedule_wrappers = soup.find_all('div',attrs={'class':'schedule__wrapper'})
time = []
events = []

for schedule__wrapper in schedule_wrappers:
	schedule_list = schedule__wrapper.find_all('li')
	for schedule in schedule_list:
		time.append(schedule.find('div',attrs={'class':'time'}))
		events.append(schedule.find('div',attrs={'class':'event'}))

'''
for _time,event in zip(time,events):
	print(_time.text)
	print(event.text)
'''

	
