from django.db import models
from datetime import datetime
# Create your models here.


class Popularity(models.Model):
    lat = models.DecimalField(max_digits = 12, decimal_places=8,unique=False)
    lng = models.DecimalField(max_digits = 12, decimal_places=8,unique=False)
    pop = models.CharField(max_length=128,unique=False)

    def __unicode__(self):
        return self.pop + ": " + str(self.lat) + "," + str(self.lng)

class Weather(models.Model):
    date_id = models.DateField(primary_key=True)
    weather_string = models.CharField(max_length=140)


    def __unicode__(self):
        return self.weather_string
