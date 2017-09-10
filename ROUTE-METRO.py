import os
import urllib2
import sys
import json
from bs4 import BeautifulSoup

sys_args = sys.argv

url = "https://delhimetrorail.info/"
url2 ="https://delhimetrorail.info/delhi-metro-stations"

try:
	from_station = str(sys.argv[1])
except IndexError:
	from_station = str(raw_input("Enter the Boarding Station: "))
from_station_name=from_station
from_station = str.lower(from_station)
from_station = from_station.replace(" ","-") + "-delhi-metro-station"

try:
	to_station = str(sys.argv[2])
except IndexError:
	to_station = str(raw_input("Enter the Destination: "))
to_station_name=to_station
to_station = str.lower(to_station)
to_station = to_station.replace(" ","-") + "-delhi-metro-station"

page = urllib2.urlopen(url2)
page_html = BeautifulSoup(page,'html.parser')


station_list = []

for tt in page_html.find_all("td", class_="left"):
	ss=tt.find_all('a')
	for ess in ss:
		station_list.append(str(ess.text).encode('utf-8'))

if from_station_name not in station_list or to_station_name not in station_list :
	print from_station_name
	print to_station_name
	print "Nahi Hai"
	sys.exit()

url = url + from_station + "-to-" + to_station
print url
print "Establishing Connection"
page = urllib2.urlopen(url)

page_html = BeautifulSoup(page,'html.parser')

fare_details = []

table = page_html.find('table', attrs={'class':'table'})
#print table


rows = table.find('td')
cols = rows.find('tr')
r1=cols.find('td')
fare_details.append(str(r1.text).encode('utf-8'))
print fare_details

print "Parsing Data, Collecting Information"
print "Making Route Chart!"
print "\n-------------------FARE DETAILS-------------------\n"
print str(fare_details[0])
