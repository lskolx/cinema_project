from .models import Film
from django_filters.rest_framework import FilterSet



class FilmGenreCountryFilter(FilterSet):
    
    class Meta:
        model = Film
        fields = ('genre', )

