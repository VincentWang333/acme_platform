from channels.layers import get_channel_layer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import CarSerializer, FridgeSerializer, DeviceDerializer
from .models import Car, Fridge, Basic_device
from rest_framework.response import Response
from rest_framework import status
from .consumers import ACMEDataConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

MODEL_SET = {"CAR":(Car, CarSerializer),
             "FRIDGE":(Fridge, FridgeSerializer)}


# GET /devices/ ->  get all device common data which only include track_id, device_type, loc_lat, loc_lng
# DELETE /devices/<track_id> ->  delete all the data of the provided track_id
#PATCH /devices/cars/<track_id> -> update specific device's state of given track_id
class DeviceListViewSet(APIView):
    def get(self, request, track_id=None):
        if track_id:
            item = get_object_or_404(Basic_device, track_id = track_id)
            type = DeviceDerializer(item).data["device_type"]
            model, model_serializer = MODEL_SET[type]
            device = get_object_or_404(model, track_id = track_id)
            device_serializer = model_serializer(device)
            return Response(device_serializer.data, status=status.HTTP_200_OK)
        serializers =  Basic_device.objects.all()    
        device_serializer = DeviceDerializer(serializers, many=True)
        return Response(device_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, track_id=None):
        if not track_id:
            return Response({"status": "error", "data": "No device detail is provided"}, status=status.HTTP_400_BAD_REQUEST)
        item = get_object_or_404(Basic_device, track_id = track_id)
        item.delete()
        send_update_signal()
        return Response({"status": "success", "data": "Item Deleted"})

    def post(self, request):
        type = request.data["device_type"]
        model, model_serializer = MODEL_SET[type]
        serializer = model_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            send_update_signal()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, track_id=None):
        if not track_id:
            return Response({"status": "error", "data": "No device detail is provided"}, status=status.HTTP_400_BAD_REQUEST)
        type = request.data["device_type"]
        model, model_serializer = MODEL_SET[type]
        item = get_object_or_404(model, track_id = track_id)
        serializer = model_serializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            send_update_signal()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
        
    
#GET /devices/cars/ -> get all specific type devices' (cars) detailed info list
#POST /devices/cars/ -> add new specific type (car) device 
class CarListViewSet(APIView):
    def get(self, request, track_id=None):
        queryset_cars = Car.objects.all()
        cars_serializer = CarSerializer(queryset_cars, many=True)
        return Response(cars_serializer.data, status=status.HTTP_200_OK)


#GET /devices/fridges/ -> get all specific type devices' (fridges) detailed info list
#POST /devices/fridges/ -> add new specific type (fridges) device 
class FridgeListViewSet(APIView):
    def get(self, request):
        queryset_fridges = Fridge.objects.all()
        fridge_serializer = FridgeSerializer(queryset_fridges, many=True)
        return Response(fridge_serializer.data, status=status.HTTP_200_OK)  


def send_update_signal():
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'data_update_group',
        {'type': 'send_update_signal', 'message': "REFRESH"}
    )

