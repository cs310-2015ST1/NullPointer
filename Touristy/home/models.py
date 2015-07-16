from django.db import models
from datetime import datetime
# Create your models here.


class Weather(models.Model):
    date_id = models.DateField(primary_key=True)
    weather_string = models.CharField(max_length=140)


    def __unicode__(self):
        return self.weather_string
