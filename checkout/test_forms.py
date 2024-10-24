from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    def test_form_is_valid(self):
        """
        test the form is valid with valid data
        """
        form = OrderForm(data={
            'full_name': 'test name',
            'email': 'test@test.com',
            'phone_number': '11111111111',
            'street_address1': 'test address 1',
            'town_or_city': 'test town',
            'country': 'GB',
        })

        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        """
        test the form is invalid with invalid data
        """
        form = OrderForm(data={
            'full_name': 'test name',
            'email': 'test@test.com',
            'phone_number': '11111111111',
            'street_address1': '',
            'town_or_city': 'test town',
            'country': 'GB',
        })

        self.assertFalse(form.is_valid())
