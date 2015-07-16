from django.db import models
from datetime import datetime
# Create your models here.


class Weather(models.Model):
    date = models.CharField(max_length=50)
    weather_string = models.CharField(max_length=140)


    def __unicode__(self):
        return self.weather_string