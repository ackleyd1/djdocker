from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

from core.mixins import StaffRequiredMixin
from platforms.models import Platform
from platforms.forms import PlatformUpdateForm

class PlatformListView(StaffRequiredMixin, ListView):
    """List of Platform objects in database"""
    model = Platform
    template_name = 'platforms/admin/platform_list.html'
    context_object_name = 'platforms'

class PlatformCreateView(StaffRequiredMixin, CreateView):
    model = Platform
    template_name = 'platforms/admin/platform_create.html'
    fields = '__all__'

    def get_success_url(self):
      return reverse('platforms:admin:detail', kwargs={'platform_slug': self.object.slug})

class PlatformDetailView(DetailView):
    model = Platform
    template_name = 'platforms/admin/platform_detail.html'
    context_object_name = 'platform'
    slug_url_kwarg = 'platform_slug'

class PlatformUpdateView(UpdateView):
    model = Platform
    template_name = 'platforms/admin/platform_update.html'
    context_object_name = 'platform'
    slug_url_kwarg = 'platform_slug'
    form_class = PlatformUpdateForm

    def get_success_url(self):
      return reverse('platforms:admin:detail', kwargs={'platform_slug': self.object.slug})
