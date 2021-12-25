from typing_extensions import Self
from django.db import models

# Create your models here.

class Basic_device(models.Model):
    track_id = models.AutoField(primary_key=True)
    loc_lat = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    loc_lng = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    device_type = models.CharField(max_length = 15, choices=[('CAR', 'CAR'), ('FRIDGE', 'FRIDGE'), ('UNKOWN', 'UNKOWN')], default="UNKOWN")
        
class Car(Basic_device):
    fluid_level = models.CharField(max_length = 4, choices=[('LOW', 'LOW'), ('HALF', 'HALF'), ('FULL', 'FULL')])
    engine_temp = models.IntegerField()
    tire_pressure = models.IntegerField()
class Fridge(Basic_device):
    ice_level = models.CharField(max_length = 4, choices=[('LOW', 'LOW'), ('HALF', 'HALF'), ('FULL', 'FULL')])
    water_leak = models.CharField(max_length = 4, choices=[('YES', 'YES'), ('NO', 'NO')])