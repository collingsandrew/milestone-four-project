from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'contact_name',
            'contact_email',
            'contact_phone_number',
            'contact_subject',
            'contact_message'
        ]

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove
        labels, and set autofocus on the first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'contact_name': 'Full Name',
            'contact_email': 'Email Address',
            'contact_phone_number': 'Phone Number (optional)',
            'contact_subject': 'Subject',
            'contact_message': 'Your Message',
        }

        # Set autofocus on the name field
        self.fields['contact_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            # Set placeholders for all fields
            placeholder = f'{placeholders[field]} *' if self.fields[
                field].required else placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder

            # Add CSS class to each field
            self.fields[field].widget.attrs['class'] = (
                'border-black rounded-0'
            )

            # Remove labels
            self.fields[field].label = False
