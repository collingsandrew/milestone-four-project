from django.test import TestCase
from django.urls import reverse

from products.models import Product


class TestBagViews(TestCase):

    def setUp(self):
        """
        create test product
        """
        self.product = Product.objects.create(
            name='test_item',
            price=1.99,
            stock=7
        )

    def test_get_bag_page(self):
        """
        test get bag page
        """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_product_to_bag(self):
        """
        test adding a product to bag with sufficient stock
        """
        # add product to bag
        response = self.client.post(
            reverse('add_to_bag', args=[self.product.id]),
            {
                'quantity': 2,
                'redirect_url': '/'
            }
        )

        bag = self.client.session['bag']
        # check if product is in the bag
        self.assertEqual(bag[str(self.product.id)], 2)

    def test_add_product_to_bag_exceeding_stock(self):
        """
        test adding a product to the bag that exceeds the products stock
        """
        # add product to bag
        response = self.client.post(
            reverse('add_to_bag', args=[self.product.id]),
            {
                'quantity': 10,
                'redirect_url': '/'
            }
        )

        bag = self.client.session['bag']
        # check if product is not in the bag
        self.assertNotIn(self.product.id, bag)

    def test_remove_product_from_bag(self):
        """
        test removing a product from the bag
        """
        # add product to bag
        response = self.client.post(
            reverse('add_to_bag', args=[self.product.id]),
            {
                'quantity': 1,
                'redirect_url': '/'
            }
        )

        # remove product from bag
        response = self.client.post(
            reverse('remove_from_bag', args=[self.product.id])
        )
        self.assertEqual(response.status_code, 200)
