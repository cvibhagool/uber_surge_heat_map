import requests
import datetime
import threading
import json
import pprint

f = open('SF_neighborhood_loc.json')
nbh_loc = json.load(f)
f.close()

interval = 60 * 3
pp = pprint.PrettyPrinter()
def getData():

	#threading.Timer(interval, getData).start()

	url = 'https://api.uber.com/v1/estimates/price'
	for nbh in nbh_loc:
		nbh_data = {}

		lat = nbh_loc[nbh]['y']
		lon = nbh_loc[nbh]['x']

		parameters = {
		    'server_token': '*********************************',
		    'start_latitude': lat,
		    'start_longitude': lon,
		    'end_latitude': 37.7833,
		    'end_longitude': -122.4167
		}

		response = requests.get(url, params=parameters)
		raw_data = response.json()

		surge = raw_data['prices'][0]['surge_multiplier']
		timestamp = str(datetime.datetime.now())

		nbh_data['surge_multiplier'] = surge
		nbh_data['timestamp'] = timestamp

		json_data = {}
		f = open('SF_data.json')
		json_data = json.load(f)
		f.close()

		if nbh not in json_data.keys():
			json_data[nbh] = []
		json_data[nbh].append(nbh_data)

		f = open('SF_data.json', 'w')
		json.dump(json_data, f)
		f.close()

		print("Neighbhood: " + nbh)
		pp.pprint(nbh_data)

	print("\n" + "Finished for timestamp: " + timestamp + "\n")

print("\nStarted at time: " + str(datetime.datetime.now()) + "\n")

#Run Function
getData()
