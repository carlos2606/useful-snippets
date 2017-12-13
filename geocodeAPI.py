import urllib
import json

service_url = "https://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = raw_input("Ingrese el nombre de la ciudad: ")
    if len(address) < 1: break

    url = service_url + urllib.urlencode({"address": address})
    uh = urllib.urlopen(url)

    data = uh.read()

    js = json.loads(str(data))

    print json.dumps(js, indent=4)
