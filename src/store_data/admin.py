from django.contrib import admin

from store_data.models import Movie


class MovieAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, MovieAdmin)
