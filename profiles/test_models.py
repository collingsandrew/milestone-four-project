from django.test import TestCase
from django.contrib.auth.models import User

class TestUserProfileModel(TestCase):

    def setUp(self):
        """
        create test user
        """
        self.user = User.objects.create_user(
            username='test',
            password='test123'
        )
        self.profile = self.user.userprofile
    
    def test_userprofile_str(self):
        '''
        test string return value for model
        '''
        self.assertEqual(str(self.profile), 'test')
