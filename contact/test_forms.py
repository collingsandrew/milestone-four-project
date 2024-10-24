from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_form_is_valid(self):
        """
        test the form is valid with valid data
        """
        form = ContactForm(data={
            'contact_name': 'Test Name',
            'contact_email': 'test@test.com',
            'contact_phone_number': '11111111111',
            'contact_subject': 'Test Subject',
            'contact_message': 'This is a test message.'
        })

        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        """
        test form with invalid data
        """
        form = ContactForm(data={
            'contact_name': '',
            'contact_email': 'test@test.com',
            'contact_phone_number': '11111111111',
            'contact_subject': 'Test Subject',
            'contact_message': 'This is a test message.'
        })

        self.assertFalse(form.is_valid())
