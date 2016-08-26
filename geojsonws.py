'''
Assignment:
1. prompt for a location
2. contact a web service
3. retrieve JSON for the web service and parse that data
4. retrieve the first place_id from the JSON
API end point: http://python-data.dr-chuck.net/geojson
Test data:
Location: South Federal University
place_id: ChIJJ8oO7_B_bIcR2AlhC8nKlok
'''
import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

address = raw_input('Enter location: ')
if len(address) < 1 :
    #address='South Federal University'
    address='Universidad de Valladolid'

url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

try: js = json.loads(str(data))
except: js = None
if 'status' not in js or js['status'] != 'OK':
    print '==== Failure To Retrieve ===='
    #print data

#print json.dumps(js, indent=4)

print 'Place id',js["results"][0]["place_id"]
