from rest_framework import routers

import viewsets

router = routers.DefaultRouter()
router.include_format_suffixes = False
router.register(r'movie', viewsets.MovieViewSet, base_name='movie')

urlpatterns = router.urls
