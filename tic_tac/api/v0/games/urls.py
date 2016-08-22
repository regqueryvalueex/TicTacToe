from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'game/(?P<pk>\d+)/$', views.RetrieveGameAPI.as_view(), name='game-detail'),
]
