from django.urls import path, include

app_name="platforms"

urlpatterns = [
    path('admin/', include('platforms.admin.urls', namespace='admin')),
]
