import urllib2
import json

#testing function for the JSON parser
WEATHER_URL = 'http://api.wunderground.com/api/4aa0f6fa0f9a7077/forecast10day/q/Canada/Vancouver.json'

#custom exception for errors made in parsing.
class ParserError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def urlParserTester():

    #tests that correct JSON is made from correct HTTPrequest
    print "BEGIN TESTS"
    print "==================================================================================================="
    print "TEST: correct JSON is made from correct HTTPrequest\n"

    #attempt making an httprequest
    try:
        f = urllib2.urlopen(WEATHER_URL)
    except IOError as e:
        raise parsorError("problem making a web request")

    json_string = f.read()
    parsed_json = json.loads(json_string)

    #attempt reading JSONObject to see if it's correct
    try:
        forcast_array = parsed_json['forecast']['txt_forecast']['forecastday']
        for j_string in forcast_array:
            print j_string
    except KeyError as e:
        raise parsorError("problem with JSONArray made")

    #tests that correct String object is made from correct directory.
    print "==================================================================================================="
    print"TEST: correct String object is made from correct directory.\n"
    print"lines below should read as weather forecasts.\n"

    #attempt to cast information inside JSONArray into correct format.
    try:
        for object in forcast_array:
            forcast = object['title'] +": "+ object['fcttext_metric']
            print forcast
    except KeyError as e:
        raise parsorError("JSONObject wasn't made correctly")


    print "==================================================================================================="

    #tests that no string is made from incorrect url.
    print "TEST: no string is made from incorrect url.\n"
    test_url ='http://api.wunderground.com/api/4aa0f6fa0f9a7077/forecast10day/'

    f = urllib2.urlopen(test_url)
    json_string = f.read()
    parsed_json = json.loads(json_string)


    try:
        forcast_array = parsed_json['forecast']['txt_forecast']['forecastday']
    except KeyError as e:
        print "no invalid string was made from wrong url"
    else:
       raise ParserError("URL was invalid, that shouldn't have happened!")

    print "==================================================================================================="
    print "END TESTS"

#initialze the testing methods.
urlParserTester()