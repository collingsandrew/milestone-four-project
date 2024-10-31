# Book Nookery Testing

[View live webpage](https://book-nookery-7651786d7c47.herokuapp.com/)

Throughout the development of Book Nookery, I performed continuous testing using Chrome Developer Tools and manual testing to ensure optimal functionality. I also wrote unit tests to make sure the code worked well and was free of errors.

Google Developer Tools was used to test the site on various device sizes.

## Automated Testing

### Unit Tests

### HTML Validation

[W3C](https://validator.w3.org/) Markup Validation Service was used to validate the HTML of the site.
Some pages on the site encountered errors, but these issues were due to the backend forms or libraries, rather than my custom HTML.

<details>
<summary>Home</summary>
<img src="documentation/testing/validation/home-validation.png">
</details>
<details>
<summary>Login</summary>
<img src="documentation/testing/validation/login-validation.png">
</details>
<details>
<summary>Register</summary>
<img src="documentation/testing/validation/register-validation.png">
</details>
<details>
<summary>Profile</summary>
<img src="documentation/testing/validation/profile-validation.png">
</details>
<details>
<summary>Products</summary>
<img src="documentation/testing/validation/products-validation.png">
</details>
<details>
<summary>Product Detail</summary>
<img src="documentation/testing/validation/product-detail-validation.png">
</details>
<details>
<summary>Add Product</summary>
<img src="documentation/testing/validation/add-product-validation.png">
</details>
<details>
<summary>Edit Product</summary>
<img src="documentation/testing/validation/edit-product-validation.png">
</details>
<details>
<summary>Wishlist</summary>
<img src="documentation/testing/validation/wishlist-validation.png">
</details>
<details>
<summary>Add Review</summary>
<img src="documentation/testing/validation/add-review-validation.png">
</details>
<details>
<summary>Shopping Bag</summary>
<img src="documentation/testing/validation/bag-validation.png">
</details>
<details>
<summary>Checkout</summary>
<img src="documentation/testing/validation/checkout-validation.png">
</details>
<details>
<summary>Order Confirmation</summary>
<img src="documentation/testing/validation/order-confirmation-validation.png">
</details>
<details>
<summary>Contact</summary>
<img src="documentation/testing/validation/contact-validation.png">
</details>

### CSS Validation

[W3C](https://jigsaw.w3.org/css-validator/) Jigsaw CSS Validation Service was used to validate the CSS of the site.
The CSS file base.css passed with no errors.

<details>
<summary>base.css</summary>
<img src="documentation/testing/validation/css-validation.png">
</details>

### JavaScript Validation

[JS Hint](https://jshint.com/) JS Validation Service was used to validate the Javascript files. All pass with no issues.

<details>
<summary>base.js</summary>
<img src="documentation/testing/validation/base-js-validation.png">
</details>
<details>
<summary>products.js</summary>
<img src="documentation/testing/validation/products-js-validation.png">
</details>
<details>
<summary>stripe_elements.js</summary>
<img src="documentation/testing/validation/stripe-elements-js-validation.png">
</details>
<details>
<summary>country_field.js</summary>
<img src="documentation/testing/validation/country-field-js-validation.png">
</details>

### Python Validation

[pep8ci Python Linter](https://pep8ci.herokuapp.com/) was used to check the python code of the site, all files returned no errors.

#### Home

<details>
<summary>views.py</summary>
<img src="documentation/testing/python/home-views-python.png">
</details>
<details>
<summary>urls.py</summary>
<img src="documentation/testing/python/home-urls-python.png">
</details>
<details>
<summary>test_views.py</summary>
<img src="documentation/testing/python/home-test-views-python.png">
</details>

#### Bag

<details>
<summary>views.py</summary>
<img src="documentation/testing/python/bag-views-python.png">
</details>
<details>
<summary>urls.py</summary>
<img src="documentation/testing/python/bag-urls-python.png">
</details>
<details>
<summary>contexts.py</summary>
<img src="documentation/testing/python/bag-contexts-python.png">
</details>
<details>
<summary>test_views.py</summary>
<img src="documentation/testing/python/bag-test-views-python.png">
</details>

#### Checkout

<details>
<summary>admin.py</summary>
<img src="documentation/testing/python/checkout-admin-python.png">
</details>
<details>
<summary>forms.py</summary>
<img src="documentation/testing/python/checkout-forms-python.png">
</details>
<details>
<summary>models.py</summary>
<img src="documentation/testing/python/checkout-models-python.png">
</details>
<details>
<summary>signals.py</summary>
<img src="documentation/testing/python/checkout-signals-python.png">
</details>
<details>
<summary>test_forms.py</summary>
<img src="documentation/testing/python/checkout-test-forms-python.png">
</details>
<details>
<summary>urls.py</summary>
<img src="documentation/testing/python/checkout-urls-python.png">
</details>
<details>
<summary>views.py</summary>
<img src="documentation/testing/python/checkout-views-python.png">
</details>
<details>
<summary>webhook_handler.py</summary>
<img src="documentation/testing/python/checkout-webhook-handler-python.png">
</details>
<details>
<summary>webhooks.py</summary>
<img src="documentation/testing/python/checkout-webhooks-python.png">
</details>

#### Contact

<details>
<summary>admin.py</summary>
<img src="documentation/testing/python/contact-admin-python.png">
</details>
<details>
<summary>forms.py</summary>
<img src="documentation/testing/python/contact-forms-python.png">
</details>
<details>
<summary>models.py</summary>
<img src="documentation/testing/python/contact-models-python.png">
</details>
<details>
<summary>test_forms.py</summary>
<img src="documentation/testing/python/contact-test-forms-python.png">
</details>
<details>
<summary>test_models.py</summary>
<img src="documentation/testing/python/contact-test-models-python.png">
</details>
<details>
<summary>test_views.py</summary>
<img src="documentation/testing/python/contact-test-views-python.png">
</details>
<details>
<summary>urls.py</summary>
<img src="documentation/testing/python/contact-urls-python.png">
</details>
<details>
<summary>views.py</summary>
<img src="documentation/testing/python/contact-views-python.png">
</details>

#### Products

<details>
<summary>admin.py</summary>
<img src="documentation/testing/python/products-admin-python.png">
</details>
<details>
<summary>forms.py</summary>
<img src="documentation/testing/python/products-forms-python.png">
</details>
<details>
<summary>models.py</summary>
<img src="documentation/testing/python/products-models-python.png">
</details>
<details>
<summary>test_forms.py</summary>
<img src="documentation/testing/python/products-test-forms-python.png">
</details>
<details>
<summary>test_models.py</summary>
<img src="documentation/testing/python/products-test-models-python.png">
</details>
<details>
<summary>test_views.py</summary>
<img src="documentation/testing/python/products-test-views-python.png">
</details>
<details>
<summary>urls.py</summary>
<img src="documentation/testing/python/products-urls-python.png">
</details>
<details>
<summary>views.py</summary>
<img src="documentation/testing/python/products-views-python.png">
</details>

#### Profiles

<details>
<summary>forms.py</summary>
<img src="documentation/testing/python/profiles-forms-python.png">
</details>
<details>
<summary>models.py</summary>
<img src="documentation/testing/python/profiles-models-python.png">
</details>
<details>
<summary>test_forms.py</summary>
<img src="documentation/testing/python/profiles-test-forms-python.png">
</details>
<details>
<summary>test_models.py</summary>
<img src="documentation/testing/python/profiles-test-models-python.png">
</details>
<details>
<summary>test_views.py</summary>
<img src="documentation/testing/python/profiles-test-views-python.png">
</details>
<details>
<summary>urls.py</summary>
<img src="documentation/testing/python/profiles-urls-python.png">
</details>
<details>
<summary>views.py</summary>
<img src="documentation/testing/python/profiles-views-python.png">
</details>

#### Wishlist

<details>
<summary>models.py</summary>
<img src="documentation/testing/python/wishlist-models-python.png">
</details>
<details>
<summary>test_models.py</summary>
<img src="documentation/testing/python/wishlist-test-models-python.png">
</details>
<details>
<summary>test_views.py</summary>
<img src="documentation/testing/python/wishlist-test-views-python.png">
</details>
<details>
<summary>urls.py</summary>
<img src="documentation/testing/python/wishlist-urls-python.png">
</details>
<details>
<summary>views.py</summary>
<img src="documentation/testing/python/wishlist-views-python.png">
</details>

### Lighthouse Testing

Google Developer Tools, specifically the Lighthouse feature, was used to test the site's performance, accessibility, best practices, and SEO. Desktop scores were strong across all metrics; however, mobile performance scored lower than expected. This was primarily due to essential CSS and JavaScript files. Improving site performance is something I would like to look further into as I recognise how this could affect user experience and retention.

#### Home

<details>
<summary>Desktop</summary>
<img src="documentation/testing/lighthouse/home-desktop-lighthouse.png">
</details>
<details>
<summary>Mobile</summary>
<img src="documentation/testing/lighthouse/home-mobile-lighthouse.png">
</details>

#### Login

<details>
<summary>Desktop</summary>
<img src="documentation/testing/lighthouse/login-desktop-lighthouse.png">
</details>
<details>
<summary>Mobile</summary>
<img src="documentation/testing/lighthouse/login-mobile-lighthouse.png">
</details>

#### Register

<details>
<summary>Desktop</summary>
<img src="documentation/testing/lighthouse/signup-desktop-lighthouse.png">
</details>
<details>
<summary>Mobile</summary>
<img src="documentation/testing/lighthouse/signup-mobile-lighthouse.png">
</details>

#### Profile

<details>
<summary>Desktop</summary>
<img src="documentation/testing/lighthouse/profile-desktop-lighthouse.png">
</details>
<details>
<summary>Mobile</summary>
<img src="documentation/testing/lighthouse/profile-mobile-lighthouse.png">
</details>

#### Products

<details>
<summary>Desktop</summary>
<img src="documentation/testing/lighthouse/products-desktop-lighthouse.png">
</details>
<details>
<summary>Mobile</summary>
<img src="documentation/testing/lighthouse/products-mobile-lighthouse.png">
</details>

#### Product Detail

<details>
<summary>Desktop</summary>
<img src="documentation/testing/lighthouse/product-detail-desktop-lighthouse.png">
</details>
<details>
<summary>Mobile</summary>
<img src="documentation/testing/lighthouse/product-detail-mobile-lighthouse.png">
</details>

#### Add Product

<details>
<summary>Desktop</summary>
<img src="documentation/testing/lighthouse/add-product-desktop-lighthouse.png">
</details>
<details>
<summary>Mobile</summary>
<img src="documentation/testing/lighthouse/add-product-mobile-lighthouse.png">
</details>

#### Edit Product

<details>
<summary>Desktop</summary>
<img src="documentation/testing/lighthouse/edit-product-desktop-lighthouse.png">
</details>
<details>
<summary>Mobile</summary>
<img src="documentation/testing/lighthouse/edit-product-mobile-lighthouse.png">
</details>

#### Wishlist

<details>
<summary>Desktop</summary>
<img src="documentation/testing/lighthouse/wishlist-desktop-lighthouse.png">
</details>
<details>
<summary>Mobile</summary>
<img src="documentation/testing/lighthouse/wishlist-mobile-lighthouse.png">
</details>

#### Add Review

<details>
<summary>Desktop</summary>
<img src="documentation/testing/lighthouse/add-review-desktop-lighthouse.png">
</details>
<details>
<summary>Mobile</summary>
<img src="documentation/testing/lighthouse/add-review-mobile-lighthouse.png">
</details>

#### Shopping Bag

<details>
<summary>Desktop</summary>
<img src="documentation/testing/lighthouse/bag-desktop-lighthouse.png">
</details>
<details>
<summary>Mobile</summary>
<img src="documentation/testing/lighthouse/bag-mobile-lighthouse.png">
</details>

#### Checkout

<details>
<summary>Desktop</summary>
<img src="documentation/testing/lighthouse/checkout-desktop-lighthouse.png">
</details>
<details>
<summary>Mobile</summary>
<img src="documentation/testing/lighthouse/checkout-mobile-lighthouse.png">
</details>

#### Order Confirmation

<details>
<summary>Desktop</summary>
<img src="documentation/testing/lighthouse/order-confirm-desktop-lighthouse.png">
</details>
<details>
<summary>Mobile</summary>
<img src="documentation/testing/lighthouse/order-confirm-mobile-lighthouse.png">
</details>

#### Contact

<details>
<summary>Desktop</summary>
<img src="documentation/testing/lighthouse/contact-desktop-lighthouse.png">
</details>
<details>
<summary>Mobile</summary>
<img src="documentation/testing/lighthouse/contact-mobile-lighthouse.png">
</details>

### Accessibility

[WAVE Web Accessibility Tool](https://wave.webaim.org/) was used to test for accessibility errors.

Some pages displayed errors due to the use of 'unlabelled=True' in Django crispy forms. I modified the Django templates to remove these tags. However, despite labels being present in the form controls within the page source code, errors remain for this reason. Aside from these specific errors, all other pages are error-free.

Not all pages could be tested, as some require user login, which the WAVE accessibility tester does not support.

<details>
<summary>Home</summary>
<img src="documentation/testing/wave/home-wave.png">
</details>
<details>
<summary>Login (form control label errors)</summary>
<img src="documentation/testing/wave/login-wave.png">
</details>
<details>
<summary>Register (form control label errors)</summary>
<img src="documentation/testing/wave/signup-wave.png">
</details>
<details>
<summary>Products</summary>
<img src="documentation/testing/wave/products-wave.png">
</details>
<details>
<summary>Product Detail</summary>
<img src="documentation/testing/wave/product-detail-wave.png">
</details>
<details>
<summary>Contact (form control label errors)</summary>
<img src="documentation/testing/wave/contact-wave.png">
</details>