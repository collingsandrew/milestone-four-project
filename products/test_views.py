from django.test import TestCase
from .models import Product


class TestProductViews(TestCase):

    def setUp(self):
        """
        create active and inactive products
        """
        self.active_product_1=Product.objects.create(
            name='Active Product 1',
            description="active",
            price=1.99,
            stock=1,
            is_active=True
        )
        self.active_product_2=Product.objects.create(
            name='Active Product 2',
            description="active",
            price=1.99,
            stock=1,
            is_active=True
        )
        self.inactive_product=Product.objects.create(
            name='Inactive Product',
            description="inactive",
            price=1.99,
            stock=1,
            is_active=False
        )

    def test_products_view_filter_active_products(self):
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
        self.assertNotIn('Inactive Product', product_names)

    def test_get_products_page(self):
        """
        test get products page
        """
        response=self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_detail_page(self):
        """
        Test get product detail page for active products,
        and inactive products give 404 response
        """
        product = self.active_product_1

        response = self.client.get(f'/products/{product.id}/')

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'products/product_detail.html')

        self.assertEqual(response.context['product'], product)
    
        inactive_product = self.inactive_product
        response = self.client.get(f'/products/{inactive_product.id}/')
        self.assertEqual(response.status_code, 404)
