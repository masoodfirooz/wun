from django.shortcuts import render

import googlemaps, json
from datetime import datetime
# Create your views here.

def home(request): 
	gmaps = googlemaps.Client(key='AIzaSyAmB2FEiZxKjtvJcGS1oQBiKtHrs03hpa8')

	# Geocoding an address, which needs Google Maps Geocoding API :
	geocode_result = gmaps.geocode('25150 South Woodland Rd Beacheood OH')

	from showevents.models import Event
	events = Event.objects.all()

	coords = []
	for event in events:
		coords.append(gmaps.geocode(event.locationAddress)[0]['geometry']['location'])
	coords = json.dumps(coords)

	return render(request, 'showevents/templates/showevents/home.html', {'coords': coords})