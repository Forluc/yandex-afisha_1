from django.urls import path
from .views import places

app_name = 'places'

urlpatterns = [
    path('', places, name='index')
]
