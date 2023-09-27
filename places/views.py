from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from places.models import Place


def index(request):
    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }
    places = Place.objects.all()
    for place in places:
        geo_json["features"].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse('place_details', kwargs={'place_id': place.id})
                }
            }
        )
    return render(request, 'index.html', context={'geo_json': geo_json})


def get_place_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_details = {
        "title": place.title,
        "imgs": [image.image.url for image in place.image.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude
        }
    }

    return JsonResponse(
        place_details,
        json_dumps_params={'ensure_ascii': False, 'indent': 4}
    )
