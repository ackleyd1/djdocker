from django.urls import path, include
from django.conf import settings
from django.contrib import admin

from core.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('platforms/', include('platforms.urls', namespace='platforms')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
