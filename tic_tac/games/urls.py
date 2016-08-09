from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^game-(?P<pk>\d+)/$', views.GameView.as_view(), name='game'),
    url(r'^$', views.NewGameView.as_view(), name='new-game'),
]
