from django.test import TestCase
from .models import Category, Product


class TestProductModels(TestCase):

    def setUp(self):

        # create a test category
        self.category = Category.objects.create(
            name='test-category',
            friendly_name='test friendly category name'
        )

        # create a test product
        self.product = Product.objects.create(
            name='test book',
            price=1.99,
            stock=1
        )

    def test_get_category_friendly_name(self):
        """
        test get category friendly name
        """
        self.assertEqual(
            self.category.get_friendly_name(),
            'test friendly category name'
        )

    def test_product_str(self):
        """
        test get product name string
        """
        self.assertEqual(str(self.product), 'test book')
