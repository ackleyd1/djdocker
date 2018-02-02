"""
Contains models for our games app:
Franchise
Game
GameListing
GameListingImage
"""

import uuid

from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db import DataError

from core.models import TimeStampedModel

from .utils import game_image_upload, gamelisting_image_upload, CONDITIONS

class Franchise(TimeStampedModel):
    """Model for video game franchises, used to suggest products."""
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Game(TimeStampedModel):
    """Model that represents a Game released for a platform."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    slug = models.SlugField(db_index=True, max_length=256, blank=True, unique=True)
    epid = models.CharField(max_length=32, null=True, blank=True, unique=True)
    image = models.ImageField(upload_to=game_image_upload, null=True, blank=True)
    verified = models.BooleanField(default=False)

    # relations
    platform = models.ForeignKey('platforms.Platform', on_delete=models.CASCADE)
    franchise = models.ForeignKey('Franchise', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Override save method to update unique slug based on the other fields."""
        slug = self.platform.slug + '-' + slugify(self.name)
        if Game.objects.filter(slug=slug).exclude(id=self.id).exists():
            raise DataError('Game with slug %s already exists' % slug)
        super().save(*args, **kwargs)

class GameListing(TimeStampedModel):
    """Model for a game to be added to a user's collection."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    condition = models.CharField(choices=CONDITIONS, max_length=32)
    active = models.BooleanField(default=False)

    # relations
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.game.name, self.condition)

class GameListingImage(TimeStampedModel):
    """Model for users to upload images of the game they are adding to their collection."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to=gamelisting_image_upload)

    # relations
    gamelisting = models.ForeignKey('GameListing', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
