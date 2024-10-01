from django.test import TestCase
from .forms import UserProfileForm

class TestUserProfileForm(TestCase):

    def setUp(self):
        self.placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

    def test_form_field_attributes(self):
        """
        check the form field placeholders and classes
        """
        form = UserProfileForm()

        self.assertTrue(
            form.fields['default_phone_number'].widget.attrs['autofocus'])

        # check if placeholders are shown
        for field in form.fields:
            if field != 'default_country':
                if form.fields[field].required:
                    placeholder = f"{self.placeholders[field]} *"
                    self.assertEqual(
                        form.fields[field].widget.attrs['placeholder'],
                        placeholder
                    )
                else:
                    placeholder = self.placeholders[field]
                    self.assertEqual(
                        form.fields[field].widget.attrs['placeholder'],
                        placeholder
                    )

            # check if specified classes are present
            self.assertEqual(
                form.fields[field].widget.attrs['class'],
                'rounded-0 profile-form-input'
            )

            # check that the fields have no labels
            self.assertFalse(form.fields[field].label)
