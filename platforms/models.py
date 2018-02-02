from django.db import models
from django.urls import reverse

from core.models import TimeStampedModel

from .utils import platform_image_upload

class Platform(TimeStampedModel):
    """Model for a gaming Platform."""
    name = models.CharField(max_length=128)
    slug = models.SlugField(db_index=True, unique=True, max_length=128, blank=True)
    image = models.ImageField(upload_to=platform_image_upload, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_admin_url(self):
        return reverse('platforms:admin:detail', kwargs={'platform_slug': self.slug})
