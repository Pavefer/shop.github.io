import django_filters

from .models import *

class AnimalFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ('name', )