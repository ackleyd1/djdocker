from django.urls import path

from .views import PlatformListView, PlatformCreateView, PlatformDetailView, PlatformUpdateView

app_name="platforms"

urlpatterns = [
    path('', PlatformListView.as_view(), name='list'),
    path('create', PlatformCreateView.as_view(), name='create'),
    path('<slug:platform_slug>', PlatformDetailView.as_view(), name='detail'),
    path('<slug:platform_slug>/update', PlatformUpdateView.as_view(), name='update'),
]
