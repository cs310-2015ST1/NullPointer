from django.db import models

class Popularity(models.Model):
    lat = models.DecimalField(max_digits = 12, decimal_places=8,unique=False)
    lng = models.DecimalField(max_digits = 12, decimal_places=8,unique=False)
    pop = models.CharField(max_length=128,unique=False)

    def __unicode__(self):
        return self.lat + "," + self.lng
