from django.test import TestCase
from .forms import ProductForm, ReviewForm
from .models import Category


class TestProductForm(TestCase):

    def setUp(self):

        # create test category
        self.category = Category.objects.create(
            name='test-category',
            friendly_name='test friendly'
        )

    def test_form_fields(self):
        """
        test category field renders correct choices,
        test form fields have correct classes
        """
        form = ProductForm()

        # check the category field renders the friendly name/s
        category_field = form.fields['category']
        self.assertEqual(
            category_field.choices,
            [(self.category.id, 'test friendly')]
        )

        # check the fields have the specified classes
        for field_name, field in form.fields.items():
            self.assertIn(
                'border-black rounded-0',
                field.widget.attrs['class']
            )


class TestReviewForm(TestCase):

    def test_form_is_valid(self):
        """
        test the form is valid with valid data
        """
        form = ReviewForm(data={
            'review_title': 'Test Title',
            'review_text': 'Test text',
            'rating': '5'
        })

        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        """
        test the form is invalid with invalid data
        """
        form = ReviewForm(data={
            'review_title': 'Test Title',
            'review_text': 'Test text',
            'rating': '6'
        })

        self.assertFalse(form.is_valid())
