# none of the track data is up to date, so use this script to build GeoJSON data
# and make some sense of it, until the issue gets resolved.
# You only need to do this if the list of tracks changes.

from geopy.geocoders import Nominatim

# https://pypi.org/project/geopy/
# geolocator = Nominatim(user_agent="myApp")
# location = geolocator.geocode("175 5th Avenue NYC")
# print(location.address)
# # Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
# print((location.latitude, location.longitude))
# # (40.7410861, -73.9896297241625)
# print(location.raw)
# # {'place_id': '9167009604', 'type': 'attraction', ...}

import json

tracks = []

# # parse tracks.json
# with open("tracks.json") as f:
# 	data = json.load(f)
# 	for i in data["items"]:
# 		tracks.append(
# 			dict(
# 				[
# 					("track_name", i["track_name"]),
# 					("address", i["address"]),
# 					("city", i["city"]),
# 					("state", i["state"]),
# 					("zip", i["zip"]),
# 				]
# 			)
# 		)

# # print the starter dictionary based on api
# print(tracks)

# but several of the values are missing or incorrect
tracks = [
	{
		"track_name": "Darlington Raceway",
		"address": "1301 Harry Byrd Hwy",
		"city": "Darlington",
		"state": "SC",
		"zip": "29532",
	},
	{
		"track_name": "Bristol Motor Speedway",
		"address": "151 Speedway Blvd.",
		"city": "Bristol",
		"state": "TN",
		"zip": "37620",
	},
	{
		"track_name": "Martinsville Speedway",
		"address": "340 Speedway Road",
		"city": "Henry",
		"state": "VA",
		"zip": "24112",
	},
	{
		"track_name": "Richmond Raceway",
		"address": "600 East Laburnum Avenue",
		"city": "Richmond",
		"state": "VA",
		"zip": "23222",
	},
	{
		"track_name": "Auto Club Speedway",
		"address": "9300 Cherry Avenue",
		"city": "Fontana",
		"state": "CA",
		"zip": "92335",
	},
	{
		"track_name": "Chicagoland Speedway",
		"address": "500 Speedway Blvd",
		"city": "Joliet",
		"state": "IL",
		"zip": "60433",
	},
	{
		"track_name": "Homestead-Miami Speedway",
		"address": "One Speedway Blvd.",
		"city": "Homestead",
		"state": "FL",
		"zip": "33035-1500",
	},
	{
		"track_name": "Kansas Speedway",
		"address": "400 Speedway Blvd.",
		"city": "Kansas City",
		"state": "KS",
		"zip": "66111",
	},
	{
		"track_name": "Las Vegas Motor Speedway",
		"address": "7000 Las Vegas Blvd. North",
		"city": "Las Vegas",
		"state": "NV",
		"zip": "89115",
	},
	{
		"track_name": "Texas Motor Speedway",
		"address": "3601 Highway 114",
		"city": "Fort Worth",
		"state": "TX",
		"zip": "76177",
	},
	{
		"track_name": "Kentucky Speedway",
		"address": "4760 Sparta Pike",
		"city": "Sparta",
		"state": "KY",
		"zip": "41086",
	},
	{
		"track_name": "Talladega Superspeedway",
		"address": "3366 Speedway Blvd.",
		"city": "Talladega",
		"state": "AL",
		"zip": "35160",
	},
	{
		"track_name": "Sonoma Raceway",
		"address": "29355 Arnold Drive",
		"city": "Sonoma",
		"state": "CA",
		"zip": "95476",
	},
	{
		"track_name": "Dover International Speedway",
		"address": "1131 North DuPont Highway",
		"city": "Dover",
		"state": "DE",
		"zip": "19901",
	},
	{
		"track_name": "Daytona International Speedway",
		"address": "1801 West International Speedway Blvd.",
		"city": "Daytona Beach",
		"state": "FL",
		"zip": "32114-1243",
	},
	{
		"track_name": "Atlanta Motor Speedway",
		"address": "1500 Highways 19 & 41 South",
		"city": "Hampton",
		"state": "GA",
		"zip": "30228",
	},
	{
		"track_name": "Indianapolis Motor Speedway",
		"address": "4790 West 16th Street",
		"city": "Speedway",
		"state": "IN",
		"zip": "46222",
	},
	{
		"track_name": "Michigan International Speedway",
		"address": "12626 U.S. 12",
		"city": "Brooklyn",
		"state": "MI",
		"zip": "49230",
	},
	{
		"track_name": "New Hampshire Motor Speedway",
		"address": "1122 Rte. 106 North",
		"city": "Loudon",
		"state": "NH",
		"zip": "03307",
	},
	{
		"track_name": "Watkins Glen International",
		"address": "2790 County Route 16",
		"city": "Watkins Glen",
		"state": "NY",
		"zip": "14891",
	},
	{
		"track_name": "Pocono Raceway",
		"address": "Long Pond Road",
		"city": "Long Pond",
		"state": "PA",
		"zip": "18334",
	},
	{
		"track_name": "Mid-Ohio Sports Car Course",
		"address": "7721 Steam Corners Road",
		"city": "Lexington",
		"state": "OH",
		"zip": "44904",
	},
	{
		"track_name": "Road America",
		"address": "N7390 Hwy 67",
		"city": "Elkhart Lake",
		"state": "WI",
		"zip": "53020-0338",
	},
	{
		"track_name": "Eldora Speedway",
		"address": "13929 State Route 118",
		"city": "Rossburg",
		"state": "OH",
		"zip": "45348",
	},
	{
		"track_name": "Canadian Tire Motorsport Park",
		"address": "3233 Concession Road #10",
		"city": "Bowmanville",
		"state": "ON",
		"zip": "L1K 0L1",
	},
	{
		"track_name": "Charlotte Motor Speedway Road Course",
		"address": "5555 Concord Parkway South",
		"city": "Concord",
		"state": "NC",
		"zip": "28027",
	},
	{
		"track_name": "Indianapolis Motor Speedway",
		"address": "",
		"city": "Indianapolis",
		"state": "Indiana",
		"zip": "",
	},
	{
		"track_name": "Gateway International Raceway",
		"address": "700 Raceway Blvd.",
		"city": "Madison",
		"state": "IL",
		"zip": "62060",
	},
	{
		"track_name": "Phoenix Raceway",
		"address": "7602 S 115th Avenue",
		"city": "Phoenix",
		"state": "AZ",
		"zip": "85323",
	},
	{
		"track_name": "Iowa Speedway",
		"address": "3333 Rusty Wallace Drive",
		"city": "Newton",
		"state": "IA",
		"zip": "50208",
	},
	{
		"track_name": "Charlotte Motor Speedway",
		"address": "5555 Concord Parkway South",
		"city": "Concord",
		"state": "NC",
		"zip": "28027",
	},
]


# # geolocate:
geolocator = Nominatim(user_agent="myApp")

# for t in tracks:
# 	print(t["track_name"])

# 	# a lot of the addresses do not exist on osm.org
# 	# location = geolocator.geocode(f"{t['address']}, {t['city']}, {t['state']}, {t['zip']}")
# 	# but after a couple changes, all of the track names can be located
# 	location = geolocator.geocode(f"{t['track_name']}")

# 	t["lat"] = location.latitude
# 	t["lon"] = location.longitude

# 	print(location.raw)

# print(tracks)


tracks = [
	{
		"track_name": "Darlington Raceway",
		"address": "1301 Harry Byrd Hwy",
		"city": "Darlington",
		"state": "SC",
		"zip": "29532",
		"lat": 34.29517345,
		"lon": -79.90554636691493,
	},
	{
		"track_name": "Bristol Motor Speedway",
		"address": "151 Speedway Blvd.",
		"city": "Bristol",
		"state": "TN",
		"zip": "37620",
		"lat": 36.515724000000006,
		"lon": -82.25700273678561,
	},
	{
		"track_name": "Martinsville Speedway",
		"address": "340 Speedway Road",
		"city": "Henry",
		"state": "VA",
		"zip": "24112",
		"lat": 36.6353555,
		"lon": -79.84639533266454,
	},
	{
		"track_name": "Richmond International Raceway",
		"address": "600 East Laburnum Avenue",
		"city": "Richmond",
		"state": "VA",
		"zip": "23222",
		"lat": 37.5922778,
		"lon": -77.41933815278796,
	},
	{
		"track_name": "Auto Club Speedway",
		"address": "9300 Cherry Avenue",
		"city": "Fontana",
		"state": "CA",
		"zip": "92335",
		"lat": 34.08824345,
		"lon": -117.49942601393725,
	},
	{
		"track_name": "Chicagoland Speedway",
		"address": "500 Speedway Blvd",
		"city": "Joliet",
		"state": "IL",
		"zip": "60433",
		"lat": 41.47441105,
		"lon": -88.05876255177395,
	},
	{
		"track_name": "Homestead-Miami Speedway",
		"address": "One Speedway Blvd.",
		"city": "Homestead",
		"state": "FL",
		"zip": "33035-1500",
		"lat": 25.45175165,
		"lon": -80.40943043188099,
	},
	{
		"track_name": "Kansas Speedway",
		"address": "400 Speedway Blvd.",
		"city": "Kansas City",
		"state": "KS",
		"zip": "66111",
		"lat": 39.1158122,
		"lon": -94.83060445285224,
	},
	{
		"track_name": "Las Vegas Motor Speedway",
		"address": "7000 Las Vegas Blvd. North",
		"city": "Las Vegas",
		"state": "NV",
		"zip": "89115",
		"lat": 36.2739166,
		"lon": -115.0131184,
	},
	{
		"track_name": "Texas Motor Speedway",
		"address": "3601 Highway 114",
		"city": "Fort Worth",
		"state": "TX",
		"zip": "76177",
		"lat": 33.036838200000005,
		"lon": -97.2838204125359,
	},
	{
		"track_name": "Kentucky Speedway",
		"address": "4760 Sparta Pike",
		"city": "Sparta",
		"state": "KY",
		"zip": "41086",
		"lat": 38.71107815,
		"lon": -84.91621243965287,
	},
	{
		"track_name": "Talladega Superspeedway",
		"address": "3366 Speedway Blvd.",
		"city": "Talladega",
		"state": "AL",
		"zip": "35160",
		"lat": 33.564928550000005,
		"lon": -86.06657144018567,
	},
	{
		"track_name": "Sonoma Raceway",
		"address": "29355 Arnold Drive",
		"city": "Sonoma",
		"state": "CA",
		"zip": "95476",
		"lat": 38.159486799999996,
		"lon": -122.4547007585656,
	},
	{
		"track_name": "Dover International Speedway",
		"address": "1131 North DuPont Highway",
		"city": "Dover",
		"state": "DE",
		"zip": "19901",
		"lat": 39.189684,
		"lon": -75.5303723951515,
	},
	{
		"track_name": "Daytona International Speedway",
		"address": "1801 West International Speedway Blvd.",
		"city": "Daytona Beach",
		"state": "FL",
		"zip": "32114-1243",
		"lat": 29.18400735,
		"lon": -81.07031856465966,
	},
	{
		"track_name": "Atlanta Motor Speedway",
		"address": "1500 Highways 19 & 41 South",
		"city": "Hampton",
		"state": "GA",
		"zip": "30228",
		"lat": 33.390276650000004,
		"lon": -84.31252119722481,
	},
	{
		"track_name": "Indianapolis Motor Speedway",
		"address": "4790 West 16th Street",
		"city": "Speedway",
		"state": "IN",
		"zip": "46222",
		"lat": 39.7971475,
		"lon": -86.2395755,
	},
	{
		"track_name": "Michigan International Speedway",
		"address": "12626 U.S. 12",
		"city": "Brooklyn",
		"state": "MI",
		"zip": "49230",
		"lat": 42.06568255,
		"lon": -84.24932569028121,
	},
	{
		"track_name": "New Hampshire Motor Speedway",
		"address": "1122 Rte. 106 North",
		"city": "Loudon",
		"state": "NH",
		"zip": "03307",
		"lat": 43.3598227,
		"lon": -71.4620406,
	},
	{
		"track_name": "Watkins Glen International",
		"address": "2790 County Route 16",
		"city": "Watkins Glen",
		"state": "NY",
		"zip": "14891",
		"lat": 42.336380500000004,
		"lon": -76.92504880603917,
	},
	{
		"track_name": "Pocono Raceway",
		"address": "Long Pond Road",
		"city": "Long Pond",
		"state": "PA",
		"zip": "18334",
		"lat": 41.05534835,
		"lon": -75.51034422309803,
	},
	{
		"track_name": "Mid-Ohio Sports Car Course",
		"address": "7721 Steam Corners Road",
		"city": "Lexington",
		"state": "OH",
		"zip": "44904",
		"lat": 40.68900855,
		"lon": -82.63635533493026,
	},
	{
		"track_name": "Road America",
		"address": "N7390 Hwy 67",
		"city": "Elkhart Lake",
		"state": "WI",
		"zip": "53020-0338",
		"lat": 43.8049423,
		"lon": -87.9898574,
	},
	{
		"track_name": "Eldora Speedway",
		"address": "13929 State Route 118",
		"city": "Rossburg",
		"state": "OH",
		"zip": "45348",
		"lat": 40.3186573,
		"lon": -84.63385385386567,
	},
	{
		"track_name": "Canadian Tire Motorsport Park",
		"address": "3233 Concession Road #10",
		"city": "Bowmanville",
		"state": "ON",
		"zip": "L1K 0L1",
		"lat": 44.049138549999995,
		"lon": -78.67451128931731,
	},
	{
		"track_name": "Charlotte Motor Speedway Road Course",
		"address": "5555 Concord Parkway South",
		"city": "Concord",
		"state": "NC",
		"zip": "28027",
		"lat": 35.35121205,
		"lon": -80.68390123780337,
	},
	{
		"track_name": "Indianapolis Motor Speedway",
		"address": "",
		"city": "Indianapolis",
		"state": "Indiana",
		"zip": "",
		"lat": 39.7971475,
		"lon": -86.2395755,
	},
	{
		"track_name": "Gateway International Raceway",
		"address": "700 Raceway Blvd.",
		"city": "Madison",
		"state": "IL",
		"zip": "62060",
		"lat": 38.6511242,
		"lon": -90.13554906209112,
	},
	{
		"track_name": "Phoenix Raceway",
		"address": "7602 S 115th Avenue",
		"city": "Phoenix",
		"state": "AZ",
		"zip": "85323",
		"lat": 33.374624999999995,
		"lon": -112.31082891531409,
	},
	{
		"track_name": "Iowa Speedway",
		"address": "3333 Rusty Wallace Drive",
		"city": "Newton",
		"state": "IA",
		"zip": "50208",
		"lat": 41.674520900000005,
		"lon": -93.01345263405133,
	},
	{
		"track_name": "Charlotte Motor Speedway",
		"address": "5555 Concord Parkway South",
		"city": "Concord",
		"state": "NC",
		"zip": "28027",
		"lat": 35.3474866,
		"lon": -80.6836796,
	},
]


# data = {}
# data['type'] = 'FeatureCollection'
# data['features'] = []

# for t in tracks:
# 	print(t["track_name"])

# 	feature = {}
# 	feature["type"] = 'Feature'

# 	# geometry = [t['lat'], t['lon']]
# 	feature["geometry"] = {}
# 	feature["geometry"]["type"] = 'Point'
# 	# GeoJSON reverses lat lon
# 	feature["geometry"]["coordinates"] = [t['lon'],t['lat']]
	
# 	feature["properties"] = {
# 		"title": t['track_name']
# 	}

# 	data['features'].append(feature)

# print(data)
