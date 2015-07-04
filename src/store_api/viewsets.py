from rest_framework import viewsets

from store_data.models import Movie


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
