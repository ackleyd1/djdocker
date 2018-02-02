from django.views.generic import TemplateView

from games.models import Game

class HomeView(TemplateView):
    """View for the home page. Can search all games in the database."""
    template_name = 'core/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        q = self.request.GET.get('q')
        if q:
            games = Game.objects.filter(name__unaccent__icontains=q)
        return context
