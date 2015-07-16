from django.core.management.base import BaseCommand,CommandError
#from home.models import Weather
#from datetime import datetime
import urllib2
import json

WEATHER_URL = 'http://api.wunderground.com/api/4aa0f6fa0f9a7077/forecast10day/q/Canada/Vancouver.json'


# class Command(BaseCommand):
#     help = "Call it with no arguments to save the current weather to the database."
#
#     def handle(selfself, *args, **options):
#         today = datetime.now()
#         today = str(today.day)
#         #weather = Weather.objects.get(date=)
#
#
#     def urlParser(self):
#         f = urllib2.urlopen(WEATHER_URL)
#         json_string = f.read()
#         parsed_json = json.loads(json_string)
#         forcast_array = parsed_json['forecast']['txt_forecast']['forecastday']
#         today_forcast = forcast_array[0]['title'] +": "+ forcast_array[0]['fcttext_metric']
#         #print today_forcast
#    f.close()


