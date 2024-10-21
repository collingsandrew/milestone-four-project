from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from products.models import Product
from wishlist.models import Wishlist
from profiles.models import UserProfile


class TestWishlistViews(TestCase):

    def setUp(self):
        """
        create a test user and product
        """

        self.user = User.objects.create_user(
            username='test',
            password='test123'
        )
        self.profile = self.user.userprofile
        self.product = Product.objects.create(
            name='test_product',
            price=1.99,
            stock=7
        )

        self.client.login(username='test', password='test123')

    def test_view_wishlist(self):
        """
        test viewing the user's wishlist page
        """
        response = self.client.get(reverse('view_wishlist'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist/wishlist.html')

    def test_add_to_wishlist(self):
        """
        test adding a product to the user's wishlist
        """
        # add the product details page as the current page the user is on
        redirect_url = reverse('product_detail', args=[self.product.id])
        response = self.client.get(
            reverse(
                'add_to_wishlist', args=[self.product.id]
            ),
            HTTP_REFERER=redirect_url
        )

        # check the view redirects to the product details page
        self.assertRedirects(response, redirect_url)
        # check the product has been added to the user's wishlist
        wishlist = Wishlist.objects.get(user_profile=self.profile)
        self.assertIn(self.product, wishlist.products.all())

    def test_remove_from_wishlist(self):
        """
        test deleting a product from the user's wishlist
        """
        # create wishlist and add product
        wishlist = Wishlist.objects.create(user_profile=self.profile)
        wishlist.products.add(self.product)

        # remove the product from the wishlist
        response = self.client.get(
            reverse('remove_from_wishlist', args=[self.product.id])
        )
        # check the user is redirected back to their wishlist
        self.assertRedirects(response, reverse('view_wishlist'))
        # check the product is no longer in the wishlist
        self.assertNotIn(self.product, wishlist.products.all())
