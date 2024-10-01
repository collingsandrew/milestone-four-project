from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


class TestProfileViews(TestCase):
    def setUp(self):
        """
        create test user and order
        """
        self.user = User.objects.create_user(
            username='test',
            password='test123'
        )
        self.profile = self.user.userprofile
        self.order = Order.objects.create(
            order_number='12345',
            user_profile=self.user.userprofile,
            full_name='testname',
            email='testemail',
            phone_number='1234567890',
            postcode='12345',
            town_or_city='testtown',
            street_address1='teststreet1',
            street_address2='teststreet2',
            county='testcountry',
            date='24/01/01',
            delivery_cost=1.99,
            order_total=10.99,
            grand_total=11.98,
            original_bag='test',
            stripe_pid='test',
            )
        self.client.login(username='test', password='test123')

    def test_get_profile_view(self):
        """
        test get profile page
        """
        response=self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_valid_profile_form(self):
        """
        test profile form is valid on post
        """
        data = {
            'default_phone_number': '1234567890',
            'default_postcode': '12345',
            'default_town_or_city': 'test town',
            'default_street_address1': 'test street 1',
            'default_street_address2': 'test street 2',
            'default_county': 'test county',
        }
        # submit form
        response = self.client.post(reverse('profile'), data)
        self.profile.refresh_from_db()
        # check postcode equals new value
        self.assertEqual(self.profile.default_postcode, '12345')
        self.assertContains(response, 'Profile updated successfully')

    def test_get_order_history(self):
        """
        test get order history
        """
        # get order 12345
        response = self.client.get(reverse('order_history', args=['12345']))
        # check http response and directed to correct template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertContains(
            response,
            'This is a past confirmation for order number 12345.'
        )
