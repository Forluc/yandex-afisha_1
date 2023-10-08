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
        response_json = response.json()

        place, created = Place.objects.get_or_create(
            title=response_json['title'],
            description_short=response_json['description_short'],
            description_long=response_json['description_long'],
            latitude=response_json['coordinates']['lat'],
            longitude=response_json['coordinates']['lng'],
        )

        for pic_number, image_url in enumerate(response_json['imgs']):
            response_json = requests.get(image_url)
            response_json.raise_for_status()

            image = Images.objects.create(place=place)
            image.image.save(
                f'{place.title}_{pic_number}.jpg',
                ContentFile(response_json.content),
                save=True
            )
        if created:
            self.stdout.write('New place loaded.')
