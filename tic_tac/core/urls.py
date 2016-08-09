from django.conf.urls import include, url
from django.contrib import admin
from django.views.debug import default_urlconf

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^social/', include('allauth.urls')),
    url(r'^', include('games.urls', namespace='games')),
]

# rest api

urlpatterns += [
    url(r'^api/v0/blog/', include('api.v0.common.urls', namespace='api-blog')),
]
