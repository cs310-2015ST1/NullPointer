from django.db import models

class Popularity(models.Model):
    lat = models.FloatField(max_length=128,unique=True)
    lng = models.FloatField(max_length=128,unique=True)
    pop = models.CharField(max_length=128,unique=False)

    def __unicode__(self):
        return self.name
