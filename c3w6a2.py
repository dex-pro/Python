import urllib.request , urllib.parse , urllib.error
import json
import ssl
key=False
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
if key is False:
    key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    parms = dict()
    parms['address'] = address
    if key is not False: parms['key'] = key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    js=json.loads(data)
    print(json)
    if not js or 'status' not in js or js['status'] != 'OK':
        print('Failed')
        continue
    print(json.dumps(js,indent=4))
    x=js["results"][0]["place_id"]
    print(x)