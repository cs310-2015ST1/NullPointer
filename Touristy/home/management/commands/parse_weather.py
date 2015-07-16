import urllib2
import json

WEATHER_URL = 'http://api.wunderground.com/api/4aa0f6fa0f9a7077/forecast10day/q/Canada/Vancouver.json'

def urlParser():

    f = urllib2.urlopen(WEATHER_URL)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    location = parsed_json['location']['city']
    temp_f = parsed_json['current_observation']['temp_f']
    print "Current temperature in %s is: %s" % (location, temp_f)
    f.close()