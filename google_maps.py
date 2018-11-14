"""
import requests
import json

# importing required libraries 
import requests, json 

# enter your api key here 
api_key ='AIzaSyCFaWan7OuUieYghWQ46SkG6pNAgiMFgsY'

# Take source as input 
source = 'ntu' 

# Take destination as input 
dest = 'boon lay' 

# url variable store url 
url ='https://maps.googleapis.com/maps/api/distancematrix/json?'

# Get method of requests module 
# return response object 
r = requests.get(url + 'origins = ' + source +
				'&destinations = ' + dest +
				'&key = ' + api_key) 
					
# json method of response object 
# return json format result 
x = r.json() 

# bydefault driving mode considered 

# print the vale of x 
print(x) 

"""
import googlemaps
import json
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDoOvMXUrPg90BxvQb2F4VhahoNG_5aRSM')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Hall 1, NTU",
                                     "The Hive, NTU",
                                     mode="transit",
                                     departure_time=now)
print(directions_result)
