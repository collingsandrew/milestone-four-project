# Book Nookery

Book Nookery is an online bookshop crafted for book lovers to browse and purchase books with ease. The site allows shoppers to explore a selection of books by category, and view detailed information on each book. Users can easily contact the shop with questions and leave reviews on books they've read.

For registered users, the site provides a personalised account experience, offering quick registration, login, profile management, and access to order history. Shoppers can save books to a wishlist, search by title, author, or description, and sort results by various criteria, such as price, to find specific genres or books within their budget.

The checkout process is streamlined, allowing shoppers to review and adjust items in their cart, securely enter payment details, and receive order confirmations. For shop owners, the platform supports simple inventory management, including adding, updating, and removing books, along with real-time stock display.

[View live webpage](https://book-nookery-7651786d7c47.herokuapp.com/)

## Project Goal

The primary goal of Book Nookery from the site owner’s perspective is:

- To add, edit, and delete books with relevant details (price, description, author, image, format, stock, and category) on the website
- To enable users to make purchases of books on the website
- To display low-stocked items to users
- To provide an accessible means for users to contact the shop with any enquiries

The primary goal of Book Nookery from a site user’s perspective:

- To register for an account on the website
- To easily log in and out of the website
- To recover/change a forgotten password with ease
- To have a personalised profile that includes my order history, delivery details, and saved information
- To view a selection of books by category on the website
- To view detailed information about individual books (price, description, author, cover image, ratings, and stock availability)
- To add items to a shopping bag, adjust quantities, and complete a purchase
- To sort books by price, category, or other attributes for easier browsing
- To search for a book by title, author, or description and view the search results
- To create and manage a wishlist, allowing me to save or remove books

## Data

The data in this project includes:
- Username, email, and password for account management.
- Default contact details like phone number, addresses, town or city, county, postcode, and country.
- Messages from users, including name, email, phone number, subject, message, submission date, and status.
- Information about books, including name, SKU, ISBN, format, author, publisher, publication date, description, edition, number of pages, image, price, stock level, weight, dimensions, favourite status, and active status.
- Names and friendly names of book categories for easy browsing and grouping of books.
- User reviews for products, including user ID, product ID, review title, text, rating, and date.
- Products wishlisted by users for future reference, linking user ID to product ID.
- Details of purchases, including order number, customer info, order date, delivery cost, total amount, and payment ID.
- Specific products in an order, detailing product ID, quantity, and total cost for each item.

Users
- Create an account with an email, username, and password, and receive confirmation after signing up.
- Access their account to manage profiles, order history, and personal info.
- Easily change personal details and default address.
- Reach out to the store for questions, whether or not they have an account.

Products
- View available books, organised by categories for easy searching.
- Access detailed information about each book, including price, description, author, ratings, and cover image.
- Save books of interest for later.

Reviews
- Share reviews on books to help other shoppers.
- Read reviews from others to make informed choices.

Orders
- Review and adjust items in the shopping bag before checkout, including changing quantities and removing items.
- Complete purchases securely by entering payment information and receiving order confirmation.
- View past orders, including details like totals, delivery info, and individual products.

Categories
- Group books into categories to make it easier for users to find specific genres of books.

## Database

A relational database was implemented for Book Nookery, consisting of several tables: User, UserProfile, Contact, Category, Reviews, WishList, Product, OrderLineItem, and Order. PostgreSQL serves as the relational database, utilising one-to-many and many-to-many relationships with primary and foreign keys to efficiently manage connections between the tables. Each table is designed to handle specific aspects of the application, ensuring organised data storage and retrieval.

### Schema

<details>
<summary>Table Schema</summary>
<img src="documentation/images/Book Nookery Table Schema.png">
</details>

### Models

User Model
- id (PK): The primary key, uniquely identifying each user.
- username: The user's chosen username.
- email: The user's email address.
- password: A hashed string for user authentication.

UserProfile Model
- id (PK): The primary key for the user profile, uniquely identifying each profile.
- user_id: A foreign key linking to the User model, establishing a one-to-one relationship between a user and their profile.
- default_phone_number: The user's contact number.
- default_street_address1: The first line of the user's default street address.
- default_street_address2: The second line of the user's default street address.
- default_town_or_city: The town or city of the user's address.
- default_county: The county of the user's address.
- default_postcode: The postcode code for the user's address.
- default_country: The country of the user's address.

Contact Model
- id (PK): The primary key for contact entries.
- contact_name: The name of the user contacting the site.
- contact_email: The email address of the user.
- contact_phone_number: The phone number of the user.
- contact_subject: The subject of the contact message.
- contact_message: The message sent by the user.
- date_submitted: The date and time when the contact message was sent.
- contact_actioned: A boolean indicating whether the contact message has been addressed.

Category Model
- id (PK): The primary key for categories.
- name: The name of the category (e.g., Fiction, Non-fiction).
- friendly_name: A user-friendly version of the category name for display purposes.

Product Model
- id (PK): The primary key for products.
- category_id (FK): A foreign key linking to the Category model, indicating the product's category.
- name: The name of the product (book title).
- sku: A unique identifier for the product.
- isbn: The International Standard Book Number for books.
- format_type: The format of the product (e.g., hardcover, paperback).
- author: The author of the product.
- publisher: The publisher of the product.
- publication_date: The date the product was published.
- description: A detailed description of the product.
- edition: The edition of the product.
- num_of_pages: The number of pages in the book.
- image: An image of the product.
- image_url: The URL for the product image.
- price: The price of the product.
- stock: The stock number of the product.
- weight: The weight of the product.
- dimensions: The dimensions of the product.
- is_favourite: A boolean indicating if the product is marked as a favourite by the site.
- is_active: A boolean indicating if the product is currently available for sale.

Reviews Model
- id (PK): The primary key for reviews.
- user_id (FK): A foreign key linking to the User model, indicating who wrote the review.
- product_id (FK): A foreign key linking to the Product model, indicating which product is being reviewed.
- review_title: A short title of the review.
- review_text: The main text content of the review.
- rating: A decimal value representing the user's rating (e.g., 1 to 5 stars).
- review_date: The date the review was submitted.

WishList Model
- id (PK): The primary key for the wishlist.
- user_id (FK): A foreign key linking to the User model, indicating which user owns the wishlist.
- product_id (m2m): A many-to-many relationship linking to the Product model, allowing multiple products to be added to the wishlist by the user.

OrderLineItem Model
- id (PK): The primary key for order line items.
- order_id (FK): A foreign key linking to the Order model, indicating which order this item belongs to.
- product_id (FK): A foreign key linking to the Product model, indicating which product is being ordered.
- quantity: The quantity of the product being ordered.
- line_item_total: The total cost for this line item.

Order Model
- id (PK): The primary key for orders.
- user_profile_id (FK): A foreign key linking to the UserProfile model, indicating which user profile made the order.
- order_number: A unique identifier for the order.
- full_name: The full name of the customer placing the order.
- email: The email address of the customer.
- phone_number: The phone number of the customer.
- street_address1: The first line of the shipping address.
- street_address2: The second line of the shipping address.
- town_or_city: The town or city for shipping.
- county: The county for shipping.
- postcode: The postcode code for shipping.
- country: The country for shipping.
- date: The date the order was placed.
- delivery_cost: The cost of delivery.
- order_total: The total cost of the order.
- grand_total: The total amount charged.
- original_bag: A text representation of the user's shopping bag.
- stripe_pid: The payment identifier from Stripe.

## Security

Security features have been implemented to protect user credentials and prevent unauthorised access. This includes using Django's built-in password hashing to safeguard user passwords. The @login_required decorator is employed to ensure that only logged-in users can view specific pages.

## CRUD

Site User (customer)

- Create an account
- Create a review for a product
- Read/view reviews
- Read/view products
- Update profile information
- Update bag items
- Delete bag items
- Delete wish list items

Site Owner/Staff

- Create/add new products
- Read/view products
- Update products
- Delete products

## User Experience

### Site Contents

- A navbar and footer with relevant links to explore the site.
- A home page with a welcome to the site.
- A login page for a user to log in.
- A sign up page for a user to sign up for an account.
- Password management pages generated by Django Allauth.
- A profile page for the user to view past orders and update their personal information.
- Product pages that can be filtered by genre, new releases and favourites or all products.
- Product detail page for each product.
- A wishlist page for registered users to save books for future reference.
- A bag page that shows everything a user has added to their bag.
- A checkout page for a user to make an order.
- A checkout success page to confirm a user's order.
- An add review page where registered users can add reviews to a product.
- A contact page which gives the means for a user to contact the store.
- An add product page for the site owner to add a product to the store.
- An edit product page for the site owner to edit a product currently on the store.
- Relevant error pages.

### Target Audience

Book Nookery aims to offer a diverse range of books spanning various genres, from fiction to educational materials, catering to a broad target audience:

- Avid readers and book enthusiasts
- Students
- Young adults and teenagers
- Professionals
- Hobbyists

### User Stories

#### Browsing & Viewing Books
|ID| As A    | I Want To Be Able To                                       | So That I Can                                                              |
|--|---------|------------------------------------------------------------|----------------------------------------------------------------------------|
|1 | Shopper | Browse a selection of books                                | Pick some to buy                                                           |
|2 | Shopper | View books by specific categories                          | Easily find the ones I’m interested in without sifting through everything  |
|3 | Shopper | See detailed information about each book                   | Check the price, description, author, ratings, and cover image             |
|4 | Shopper | Easily check the total cost of my items                    | Stay within my budget                                                      |
|5 | Shopper | Contact the store easily, whether I have an account or not | Get answers to any questions I have                                        |
|6 | Shopper | View and leave reviews on books                            | Share my thoughts and help others make decisions                           |

#### Registration & User Accounts
|ID| As A      | I Want To Be Able To                              | So That I Can                                                                |
|--|-----------|---------------------------------------------------|------------------------------------------------------------------------------|
|7 | Site User | Quickly create an account                         | Have a personal profile and access my information                            |
|8 | Site User | Log in and log out with ease                      | Manage my account details                                                    |
|9 | Site User | Change my password easily                         | Keep my account secure and up to date                                        |
|10| Site User | Receive confirmation after signing up             | Know my account was created successfully                                     |
|11| Site User | Have a personalised profile                       | View my order history, order confirmations, and save my personal information |

#### Sorting & Searching
|ID| As A    | I Want To Be Able To                                        | So That I Can                                                   |
|--|---------|-------------------------------------------------------------|-----------------------------------------------------------------|
|12| Shopper | Save and view my wish listed books                          | Easily find them when I’m ready to make a purchase              |
|13| Shopper | Sort books within a category                                | Find a specific genre of books I am looking for                 |
|14| Shopper | Sort books by different sorting lists                       | Find the best prices easily                                     |
|15| Shopper | Search for a book by title, author, or description          | Quickly locate the one I want to buy                            |
|16| Shopper | Clearly see my search results and the number of books found | Determine if the book I’m looking for is available              |

#### Purchasing & Checkout
|ID| As A    | I Want To Be Able To                                 | So That I Can                                                 |
|--|---------|------------------------------------------------------|---------------------------------------------------------------|
|17| Shopper | Review the items in my cart                          | See the total cost and confirm what I’m about to buy          |
|18| Shopper | Adjust the items in my bag                           | Easily make changes before completing my purchase             |
|19| Shopper | Enter my payment information quickly                 | Complete the checkout process smoothly                        |
|20| Shopper | Feel confident that my payment information is secure | Proceed with my purchase without worries                      |
|21| Shopper | See a confirmation of my order after checkout        | Ensure everything is correct                                  |

#### Admin & Store Management
|ID| As A        | I Want To Be Able To                            | So That I Can                                                                |
|--|-------------|-------------------------------------------------|------------------------------------------------------------------------------|
|22| Store Owner | Add new books to the store                      | Make them available for customers to purchase                                |
|23| Store Owner | Update book details                             | Change prices, descriptions, authors, formats, images, and stock information |
|24| Store Owner | Remove books from the store                     | Stop selling titles that are no longer available                             |
|25| Store Owner | Track and display the amount of stock available | Ensure customers know how many copies are available                          |
|26| Store Owner | Ensure errors redirect users to relevant pages  | Maintain user engagement and assist them with navigation                     |

