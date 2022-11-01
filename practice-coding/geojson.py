import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    #Assign address to a variable
    address = input('Enter location: ')
    #if user did not enter something just break
    if len(address) < 1: break

    #creating a dictionary call parms where you will save the address as search parameters in the URL as well as the api key at the end of the url
    parms = dict()
    parms['address'] = address
    #if api key is not false then assign the value from api_key to key and add it to the dictionary
    if api_key is not False: parms['key'] = api_key
    #create the full URL to enter in the search where url = api_url + address + api_key, url must be enconded 
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    #the next line will open the url and ignoring the SSL certificates to get url handler (uh)
    uh = urllib.request.urlopen(url, context=ctx)
    #read the whole document and because is UTF-8 coming from the outside world we are going to turn into unicode in the app using decode()
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')


    #loading the data in json
    try:
        js = json.loads(data)
    except:
        js = None

    #since the response is a dictionary and has a status parameter in it, we can ask if js is None or if status is not found in js or if the status is different than OK then quit
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    
    #json.dumps does the opposite of json.loads which make js more readible by indenting it
    print(json.dumps(js, indent=4))

    #extracting data from the command above, because js is a dictionary nested within dictionaries inside it the next lines are to retirve the info that we want
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    #printing lat and long
    print('lat', lat, 'lng', lng)
    #Extracting data again from json but looking for the address and then printing it
    location = js['results'][0]['formatted_address']
    print(location)