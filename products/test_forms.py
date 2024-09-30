from django.test import TestCase
from .forms import ProductForm
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

        category_field = form.fields['category']
        self.assertEqual(
            category_field.choices,
            [(self.category.id, self.category.get_friendly_name())]
        )

        for field_name, field in form.fields.items():
            self.assertIn(
                'border-black rounded-0',
                field.widget.attrs['class']
            )
