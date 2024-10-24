from django.test import TestCase
from contact.models import Contact


class TestContactModel(TestCase):

    def setUp(self):
        """
        create test object
        """
        self.contact = Contact.objects.create(
            contact_name='Test Name',
            contact_email='test@test.com',
            contact_phone_number='11111111111',
            contact_subject='Test Subject',
            contact_message='This is a test message',
            contact_actioned=False
        )

    def test_contact_str(self):
        """
        test string return value for model
        """
        expected_str = "Test Name - Test Subject"
        self.assertEqual(str(self.contact), expected_str)
