from django.db import models

from products.models import Product
from profiles.models import UserProfile


class Wishlist(models.Model):
    """
    A model for the user's wishlist.
    """
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='wishlist'
    )

    products = models.ManyToManyField(
        Product,
        blank=False
    )

    def __str__(self):
        return f"{self.user_profile.user.username}'s wishlist"
