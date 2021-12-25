from rest_framework import serializers
from .models import Car, Fridge, Basic_device


class DeviceDerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Basic_device
        fields = [
            'track_id',
            'device_type',
            'loc_lat',
            'loc_lng',
        ]

class CarSerializer(DeviceDerializer):
    class Meta:
        model = Car
        fields = DeviceDerializer.Meta.fields + ['fluid_level', 'engine_temp', 'tire_pressure'] 

class FridgeSerializer(DeviceDerializer):
    class Meta:
        model = Fridge
        fields = DeviceDerializer.Meta.fields + ['ice_level', 'water_leak']