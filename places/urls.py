from django.urls import path
from places.views import index, get_place_details

urlpatterns = [
    path('', index, name='index'),
    path('places/<int:place_id>', get_place_details, name='place_details'),
]
