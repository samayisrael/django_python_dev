import folium
import googlemaps
from datetime import datetime

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re
import os
from secrets import google_key

url = 'https://sffnb.org/list-of-san-francisco-empty-and-abandoned-buildings/'
#Connect to Google
gmaps = googlemaps.Client(key=google_key)

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#the start
var_write = 'eqfeed_callback({"type":"FeatureCollection","features":['

build_json = ''
for tag in soup.find_all(re.compile("^p")):
    if re.search('\d{1,5}\s\w+', tag.text) and tag.text.find('–') == -1 and tag.text.find('(') == -1:
        addy = tag.text
        addy_param = addy+', San Francisco, CA'
        # Geocoding an address
        geocode_result = gmaps.geocode(addy_param)

        print('Current Address', addy_param)
        #print(geocode_result)

        #lngLat = str(geocode_result[0]['geometry']['bounds']['northeast']['lng'])+','+str(geocode_result[0]['geometry']['bounds']['northeast']['lat'])
        lngLat = str(geocode_result[0]['geometry']['location']['lng'])+','+str(geocode_result[0]['geometry']['location']['lat'])
        var_write += '{'
        var_write +='"type": "Feature",'
        var_write +='"geometry": {'
        var_write +='"type": "Point",'
        var_write +='"coordinates": ['+lngLat+'],'
        var_write +='"markerlabel": "'+addy+'"'
        var_write +='}'
        var_write +='}'
#the end
var_write +=']});'

f = open("somethingdifferent.js", "w")
f.write(var_write)
f.close()
#f = open("somethingdifferent.js", "r")
#print(f.read())
#print(os.path.abspath('somethingdifferent.js'))


#geocode_result = '{"type": "Feature","geometry": { "type": "Point","coordinates": [125.6, 10.1]},"properties": {"name": "Dinagat Islands"}}'

# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))



    buildings_info = 'test2'
    return render(request, "buildings.html",  {"dataset": buildings_info})
