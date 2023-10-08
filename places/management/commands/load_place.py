from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Images
import requests


class Command(BaseCommand):
    help = 'Load place from json'

    def add_arguments(self, parser):
        parser.add_argument('json', help='Json url')

    def handle(self, *args, **options):
        response = requests.get(options['json'])
        response.raise_for_status()
        response = response.json()

        place, created = Place.objects.get_or_create(
            title=response['title'],
            description_short=response['description_short'],
            description_long=response['description_long'],
            latitude=response['coordinates']['lat'],
            longitude=response['coordinates']['lng'],
        )

        for pic_number, image_url in enumerate(response['imgs']):
            response = requests.get(image_url)
            response.raise_for_status()

            image = Images.objects.create(place=place)
            image.image.save(
                f'{place.title}_{pic_number}.jpg',
                ContentFile(response.content),
                save=True
            )
        if created:
            self.stdout.write('New place loaded.')
