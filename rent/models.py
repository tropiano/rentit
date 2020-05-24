from django.db import models
import django_filters
# Create your models here.


class House(models.Model):
    city = models.CharField(max_length=200)
    mq = models.IntegerField(default=0)
    rooms = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    image = models.CharField(max_length=200)
    link = models.CharField(max_length=500)


CITY_CHOICE = (
    ('La Spezia', 'La Spezia'),
    ('Trieste', 'Trieste'),
    ('Trento', 'Trento'),
    ('Pescara', 'Pescara'),
    ('Catania', 'Catania')
)


class HouseFilter(django_filters.FilterSet):

    city = django_filters.ChoiceFilter(
        lookup_expr='iexact', choices=CITY_CHOICE, empty_label="All Italy")

    price = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte')

    class Meta:
        model = House
        fields = ['city', 'price']
