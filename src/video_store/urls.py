from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

import store_api.urls
import store_ui.urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(store_api.urls.urlpatterns)),
    url(r'^.*$', include(store_ui.urls.urlpatterns))
]
