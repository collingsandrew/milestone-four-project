from django.test import TestCase
from .models import Product


class TestProductViews(TestCase):

    def setUp(self):
        """
        create active and inactive products
        """
        Product.objects.create(name='Active Product 1', description="active", price=1.99, stock=1, is_active=True)
        Product.objects.create(name='Active Product 2', description="active", price=1.99, stock=1, is_active=True)
        Product.objects.create(name='Inactive Product 1', description="inactive", price=1.99, stock=1, is_active=False)

    def test_view_filter_active_products(self):
        """
        test view filters active products only
        """
        response=self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

        products = response.context['products']

        self.assertEqual(len(products), 2)
        for product in products:
            self.assertTrue(product.is_active)

        product_names = [product.name for product in products]
        self.assertNotIn('Inactive Product 1', product_names)

    def test_get_products_page(self):
        """
        test get products page
        """
        response=self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
