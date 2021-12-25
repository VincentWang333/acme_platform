from django.urls import path
from .views import CarListViewSet, FridgeListViewSet, DeviceListViewSet



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('devices/', DeviceListViewSet.as_view()),
    path('devices/<str:track_id>', DeviceListViewSet.as_view()),
    path('devices/cars/', CarListViewSet.as_view()),
    path('devices/fridges/', FridgeListViewSet.as_view())
]
