from django.views.generic import TemplateView

from platforms.models import Platform
from games.models import Game

from .mixins import StaffRequiredMixin

class HomeView(TemplateView):
    """View for the home page. Can search all games in the database."""
    template_name = 'core/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['platforms'] = Platform.objects.all()
        q = self.request.GET.get('q')
        platform = self.request.GET.get('platform')
        if q:
            games = Game.objects.filter(name__unaccent__icontains=q)
            if platform and platform != 'all':
                games = games.filter(platform__slug=platform)
            # context['games'] = games.select_related('platform').annotate(gamesale_count=Count('gamesale'), min_price=Min('gamelisting__price')).order_by('-gamesale_count')
        return context
