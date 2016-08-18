from django.urls import reverse
from django.core.cache import cache
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

    def get_context_data(self, *args, **kwargs):
        context = super(NewGameView, self).get_context_data(**kwargs)
        open_games_ids = cache.get('open_games', set())
        context['open_games'] = models.Game.objects.filter(id__in=open_games_ids)
        return context
