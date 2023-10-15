from django.urls import path

from places.views import get_place_details, index

urlpatterns = [
    path('', index, name='index'),
    path('places/<int:place_id>', get_place_details, name='place_details'),
]
