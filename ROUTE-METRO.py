import os
import urllib2
import sys
import json
from bs4 import BeautifulSoup

sys_args = sys.argv

url = "https://delhimetrorail.info/"

try:
	from_station = str(sys.argv[1])
except IndexError:
	from_station = str(raw_input("Enter the Boarding Station: "))
from_station = str.lower(from_station)
from_station = from_station.replace(" ","-") + "-delhi-metro-station"

try:
	to_station = str(sys.argv[2])
except IndexError:
	to_station = str(raw_input("Enter the Destination: "))
to_station = str.lower(to_station)
to_station = to_station.replace(" ","-") + "-delhi-metro-station"

page = urllib2.urlopen(url)
page_html = BeautifulSoup(page)


station_list = []

for tt in page_html.find_all('option'):
	station_list.append(str(tt['value'].encode('utf-8')))

if from_station not in station_list or to_station not in station_list :
	sys.exit()

url = url + from_station + "-to-" + to_station
#print url
print "Establishing Connection"
page = urllib2.urlopen(url)

page_html = BeautifulSoup(page)
l = page_html.find_all('td')
fare_details = l[0].text.encode('utf-8')
fare_details = fare_details.replace("Time","\n\t\tTime ")
fare_details = fare_details.replace("Distance","\n\t\tDistance ")
final = fare_details.split("First")
print "Parsing Data, Collecting Information"
print "Making Route Chart!"
print "\n-------------------FARE DETAILS-------------------\n"
print "\t\t" + str(final[0])

temp = page_html.find_all('span')
route_map = temp[15].find_all('a')


print "\n\n-------------------ROUTE MAP-------------------\n"
for i in range(1,len(route_map)):
	if i > 1:
		if route_map[i-1].text == route_map[i].text:
			print "\n<------------- INTERCHANGE HERE ------------->\n"
			print "\t\t" + route_map[i].text
		else:
			print "\t\t" + route_map[i].text
	else:
		print "\t\t" + route_map[i].text


