from django.db import models


class Movie(models.Model):
    uuid = models.UUIDField()
    shelf_id = models.PositiveIntegerField()
    tmdb_id = models.PositiveIntegerField()
