from django.db import models


class Movie(models.Model):
    uuid = models.UUIDField()
    title = models.CharField(max_length=255)
    shelf_id = models.PositiveIntegerField()
    tmdb_id = models.PositiveIntegerField()
