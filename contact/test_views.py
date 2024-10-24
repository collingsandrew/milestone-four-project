from django.test import TestCase
from django.urls import reverse


class TestContactViews(TestCase):

    def test_get_contact_page(self):
        """
        test viewing the contact page
        """
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
