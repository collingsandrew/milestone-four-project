from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):

    readonly_fields = (
        'contact_name',
        'contact_email',
        'contact_phone_number',
        'contact_subject',
        'contact_message',
        'date_submitted',
    )

    fields = (
        'contact_name',
        'contact_email',
        'contact_phone_number',
        'contact_subject',
        'contact_message',
        'date_submitted',
        'contact_actioned',
    )

    list_display = (
        'contact_subject',
        'contact_email',
        'date_submitted',
        'contact_actioned',
    )

    ordering = ('-date_submitted',)


admin.site.register(Contact, ContactAdmin)
