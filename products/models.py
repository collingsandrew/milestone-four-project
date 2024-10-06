from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(
        max_length=254
    )

    friendly_name = models.CharField(
        max_length=254,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=254
    )

    sku = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True
    )

    isbn = models.CharField(
        max_length=13,
        unique=True,
        blank=True,
        null=True
    )

    format_type = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    author = models.CharField(
        max_length=254,
        blank=True,
        null=True
    )

    publisher = models.CharField(
        max_length=254,
        blank=True,
        null=True
    )

    publication_date = models.DateField(
        blank=True,
        null=True
    )

    description = models.TextField()

    edition = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    num_of_pages = models.IntegerField(
        blank=True,
        null=True
    )

    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True
    )

    image = models.ImageField(
        null=True,
        blank=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.IntegerField(
        default=0
    )

    weight = models.IntegerField(
        blank=True,
        null=True
    )

    dimensions = models.CharField(
        max_length=254,
        blank=True,
        null=True
    )

    is_favourite = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


class Review(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='review'
    )

    review_title = models.CharField(
        max_length=255
    )

    review_text = models.TextField()

    rating = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )

    review_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username}'s review for {self.product.name}"
