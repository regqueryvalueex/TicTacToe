from django.urls import reverse
from django.urls import reverse_lazy
from django.views import generic
from . import models
from . import forms


class GameView(generic.DetailView):
    template_name = 'games/game.html'
    model = models.Game


class NewGameView(generic.CreateView):
    template_name = 'games/new-game.html'
    model = models.Game
    form_class = forms.NewGameForm
    context_object_name = 'game'

    def get_success_url(self):
        return reverse('games:game', kwargs={'pk': self.object.pk})
