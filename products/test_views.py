from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from django.db.models import Q
from datetime import date, timedelta

from .models import Product, Category


class TestProductViews(TestCase):

    def setUp(self):
        """
        create test categories
        """
        self.category1 = Category.objects.create(name='Fiction')
        self.category2 = Category.objects.create(name='Non-Fiction')

        """
        create active and inactive products
        """

        self.active_product_1=Product.objects.create(
            name='Active Product 1',
            description="active",
            price=1.99,
            stock=1,
            author='Author 1',
            isbn='1234567890',
            category=self.category1,
            is_active=True
        )
        self.active_product_2=Product.objects.create(
            name='Active Product 2',
            description="active",
            price=1.99,
            stock=1,
            author='Author 2',
            isbn='0987654321',
            category=self.category2,
            is_active=True
        )
        self.inactive_product=Product.objects.create(
            name='Inactive Product',
            description="inactive",
            price=1.99,
            stock=1,
            is_active=False
        )

        self.url = reverse('products')

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
        test get product detail page for active products,
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

    def test_filter_by_category(self):
        """
        test products filtering by category
        """
        response = self.client.get(self.url, {'category': 'Fiction'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Active Product 1')
        self.assertNotContains(response, 'Active Product 2')
    
    def test_filter_by_search_query(self):
        """
        test products filtering by search query
        """
        response = self.client.get(self.url, {'q': 'Author 1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Active Product 1')
        self.assertNotContains(response, 'Active Product 2')

    def test_filter_by_isbn(self):
        """
        test products filtering by isbn
        """
        response = self.client.get(self.url, {'q': '1234567890'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Active Product 1')
        self.assertNotContains(response, 'Active Product 2')

    def test_sort_products(self):
        """
        test sorting products by price in ascending and descending order
        """
        response_asc = self.client.get(self.url, {'sort': 'price-asc'})
        self.assertEqual(response_asc.status_code, 200)
        products_asc = response_asc.context['products']
        self.assertLessEqual(products_asc[0].price, products_asc[1].price)

        response_desc = self.client.get(self.url, {'sort': 'price-desc'})
        self.assertEqual(response_desc.status_code, 200)
        products_desc = response_desc.context['products']
        self.assertGreaterEqual(products_desc[0].price, products_desc[1].price)

    def test_filter_favorite_products(self):
        """
        test filtering favorite products
        """
        # set product 1 as favourite
        self.active_product_1.is_favourite = True
        self.active_product_1.save()

        # check if product 1 is included in filter and product 2 is not
        response = self.client.get(self.url, {'is_favourite': 'true'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Active Product 1')
        self.assertNotContains(response, 'Active Product 2')

    def test_filter_new_release(self):
        """
        test filtering products released within 60 days
        """
        # set product 1 publication date set for 30 days ago
        self.active_product_1.publication_date = date.today() - timedelta(days=30)
        self.active_product_1.save()
        # set product 2 publication date for 90 days ago
        self.active_product_2.publication_date = date.today() - timedelta(days=90)
        self.active_product_2.save()

        # check if product 1 is included in filter and product 2 is not
        response = self.client.get(self.url, {'is_new_release': 'true'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Active Product 1')
        self.assertNotContains(response, 'Active Product 2')
