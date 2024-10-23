from django.db import models


class Contact(models.Model):

    contact_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    contact_email = models.EmailField(
        max_length=254,
        null=False,
        blank=False,
    )

    contact_phone_number = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )

    contact_subject = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    contact_message = models.TextField(
        max_length=1000,
        null=False,
        blank=False,
    )

    date_submitted = models.DateTimeField(
        auto_now_add=True
    )

    contact_actioned = models.BooleanField(
        default=False
    )

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.contact_name} - {self.contact_subject}"
