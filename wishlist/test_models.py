from django.test import TestCase
from django.contrib.auth.models import User

from profiles.models import UserProfile
from wishlist.models import Wishlist


class TestWishlistModel(TestCase):

    def setUp(self):
        """
        create test user, product and wishlist
        """
        self.user = User.objects.create_user(
            username='test',
            password='test123'
        )
        self.profile = self.user.userprofile
        self.wishlist = Wishlist.objects.create(
            user_profile=self.profile
        )

    def test_wishlist_str(self):
        '''
        test string return value for model
        '''
        expected_str = f"{self.profile.user.username}'s wishlist"
        self.assertEqual(str(self.wishlist), expected_str)
