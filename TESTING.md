# Sports Sole Website Testing

[Back to the README.md file](https://github.com/Alvor1991/PP5-Sports-Sole/blob/main/README.md)  

[View the live website here](https://sports-sole-d03df7b3c157.herokuapp.com/)  

## Table of Contents

1. [Testing User Stories](#testing-user-stories)
2. [Code Validation](#code-validation)
3. [Accessibility](#accessibility)
4. [Tools Testing](#tools-testing)
5. [Manual Testing](#manual-testing)

***

## Testing User Stories

### 1. View a List of Sneakers
* AC1: User can see a list of sneakers on the main products page.
* AC2: Sneakers are displayed with basic information (name, image, price).
* AC3: User can navigate through multiple pages of sneakers if applicable.

### 2. See Detailed Information for Sneakers
* AC1: User can click on a sneaker to view its detailed information.
* AC2: Detailed view shows price, description, rating, and available sizes.
* AC3: User can see sneaker images clearly.

### 3. Quickly Identify Deals and Discounts
* AC1: Special offers are clearly marked on the product list.
* AC2: User can easily navigate to a dedicated special offers section.
* AC3: Discounts or deal prices are prominently displayed.

### 4. View the Total Cost of Selected Items
* AC1: Running total is visible in the shopping bag icon.
* AC2: Total updates immediately when adding or removing items.
* AC3: User can view a detailed breakdown in the shopping bag.

### 5. Register for an Account
* AC1: User can access a registration form from the main navigation.
* AC2: Form validates input and creates account with valid information.
* AC3: User receives confirmation of successful registration.

### 6. Log In or Log Out of My Account
* AC1: Registered user can log in with correct credentials.
* AC2: Logged-in user can easily log out from any page.
* AC3: User's login status is clearly indicated in the navigation.

### 7. Recover My Password
* AC1: User can request password reset from login page.
* AC2: Reset instructions are sent to user's email.
* AC3: User can set a new password and access their account.

### 8. Receive an Email Confirmation After Registering
* AC1: User receives an email shortly after registration.
* AC2: Email contains confirmation link or welcome message.
* AC3: User can verify their email address if required.

### 9. Have a Personalized User Profile
* AC1: Logged-in user can access their profile page.
* AC2: Profile displays order history and saved information.
* AC3: User can update their default delivery information.

### 10. Sort Sneakers by Price, Rating, or Category
* AC1: User can sort sneakers by price (low to high, high to low).
* AC2: User can sort sneakers by rating.
* AC3: User can sort sneakers by category.

### 11. Sort Sneakers by Category
* AC1: User can navigate to a specific sneaker category.
* AC2: Sorting options are available within the category view.
* AC3: Category-specific sorting (if applicable) is available.

### 12. Search for Sneakers by Name or Description
* AC1: Search bar is easily accessible from all pages.
* AC2: Search returns relevant results based on sneaker name or description.
* AC3: User can view the number of search results.

### 13. Filter Products Across Multiple Categories
* AC1: User can select multiple categories to filter sneakers.
* AC2: Filtered results show sneakers from all selected categories.
* AC3: User can easily add or remove categories from the filter.

### 14. Select Size and Quantity of Sneakers
* AC1: Size options are clearly displayed on the product page.
* AC2: Quantity can be easily adjusted before adding to bag.
* AC3: Selected size and quantity are confirmed when adding to bag.

### 15. View Final Cost Including Taxes and Shipping
* AC1: Final cost breakdown is shown before completing purchase.
* AC2: Taxes and shipping costs are clearly itemized.
* AC3: User can see how costs change based on delivery options.

### 16. Complete My Purchase Securely
* AC1: Checkout process guides user through payment steps.
* AC2: Payment form is clear and easy to fill out.
* AC3: User receives clear confirmation of successful purchase.

### 17. Newsletter Signup
* AC1: Newsletter signup form is easily accessible.
* AC2: User can enter email and subscribe with one click.
* AC3: Confirmation of subscription is provided to the user.

### 18. Add Product
* AC1: Admin can access a form to add new products.
* AC2: All necessary product details can be entered.
* AC3: New product appears in the product list after adding.

### 19. Edit/Update Product

* AC1: Admin can select a product to edit.
* AC2: Edit form is pre-filled with current product information.
* AC3: Changes are reflected immediately after updating.

### 20. Delete Product

* AC1: Admin can select a product to delete.
* AC2: Confirmation is required before deletion.
* AC3: Product is removed from the site after confirmation.

### 21. Client Testimonial Management

* AC1: Admin can add new client testimonials.
* AC2: Existing testimonials can be edited or removed.
* AC3: Testimonials are displayed on the appropriate pages.

### 22. FAQ Management

* AC1: Admin can add new FAQ entries.
* AC2: Existing FAQs can be updated or deleted.
* AC3: FAQs are organized and easily accessible to users.

### 23. Contact Form

* AC1: I can easily find and access the contact form.
* AC2: Form includes fields for name, email, and message.
* AC3: I receive a confirmation when message is sent successfully.

### 24. Wishlist/Favorites Feature

* AC1: Given I am viewing a product, I can click a button to add it to my wishlist.
* AC2: When I access my profile, I can view all my wishlist items in a dedicated section.
* AC3: Given I am viewing my wishlist in my profile, I can remove items using a button beneath each product.

### 25. Post-Purchase Product Review System

* AC1: Given I have received my order, I receive an email invitation to review my purchased items.
* AC2: When clicking the review link in the email, I can rate the product and write my review.
* AC3: When viewing products, I can see verified purchase reviews from other customers to help inform my decision.

### 26. View and Purchase Discounted Products
* AC1: Given I am viewing a product page, I can see the original price crossed out and the discounted price clearly displayed.
* AC2: When I click on Special Offers, I can see all products that currently have discounts applied.
* AC3: When I add discounted items to bag, they are added at the correct reduced price. 

## Code Validation

### HTML

[W3C Markup Validator](https://validator.w3.org/) service was used to validate the HTML code and found the following errors:

<div style="display: flex; justify-content: space-between;">
    <img src="assets/testing_files/base_html_error1.png" alt="base.html validation errors image" width="60%" style="margin-bottom: 20px;">
    <img src="assets/testing_files/base_html_error2.png" alt="base.html validation errors image" width="60%" style="margin-bottom: 20px;">
</div>


| Warning/Error | Fix |
|--------------|-----|
| The type attribute is unnecessary for JavaScript resources. | Removed type="text/javascript" from all script tags (HTML5 default). |
| The aria-labelledby attribute must point to an element in the same document. | Updated the id of Women's to "womens-link" and Men's to "mens-link" to match aria-labelledby. |
| Possible misuse of aria-label. | Removed aria-label from dropdowns since aria-labelledby already handles accessibility. |
| The first occurrence of ID user-options was here. | Renamed the duplicate id="user-options" to id="user-options-mobile" in the mobile navigation. |
| Possible misuse of aria-label. | Removed aria-label="Search" from "fas fa-search" as it is unnecessary for purely decorative icons. |
| Element li not allowed as child of element nav in this context. | Wrapped `<li>` elements in `<ul class="list-inline">` within nav element. |
| Duplicate ID `id_email` found. | Changed duplicate IDs to unique values `id_email_signup` and `id_email_add` using django-widget-tweaks. |

### CSS

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) service was used to validate the CSS code of the project to ensure there were no syntax errors.

W3C CSS Validator found no errors or warnings in the CSS.

![CSS validation image](assets/testing_files/css_validation.png)

### Python

[PEP8CI](https://pep8ci.herokuapp.com/) was used to validate the Python code for PEP8 compliance. As there were many files to assess within each app, I have focused on the appointment app for this testing section. 

| Location | Errors / Warnings | Code Reviewed |
| --- | --- | --- |
| ./appointments/model.py | ![forms.py errors/warnings image](assets/testing_files/appointment_model.png) | ![forms.py code reviewed image](assets/testing_files/models_reviewed.pmg.png) |
| ./appointments/views.py | ![views.py errors/warnings image](assets/testing_files/appointments_views.png) | ![views.py code reviewed image](assets/testing_files/views_reviewed.png) |
| ./appointments/forms.py | ![urls.py errors/warnings image](assets/testing_files/appointments_forms.png) | ![urls.py code reviewed image](assets/testing_files/forms_reviewed.pmg.png) |


### JavaScript

[JSHint's JavaScript Code Quality Tool](https://jshint.com/) was used to validate the site's JavaScript code.

During development, I encountered errors related to the use of ES6 features, such as const, arrow functions, and template literals, which were flagged by environments expecting older JavaScript versions.

Despite these errors, I chose to stick with ES6 as it offers a more modern and readable syntax, improving code maintainability. The project targets modern browsers, which fully support ES6, allowing for better performance & alignment with current web development practices.

## Accessibility

Lighthouse in Chrome DevTools was used to confirm that colors & fonts used throughout the website are easy to read and accessible.

### Lighthouse Reports

Page | Lighthouse Report |
| --- | --- |
| Home | ![Index Lighthouse Report](assets/testing_files/lighthouse_index.jpg) |
| About | ![About Lighthouse Report](assets/testing_files/lighthouse_about.jpg) |
| Treatments | ![Register Lighthouse Report](assets/testing_files/lighthouse_treatments.jpg) |
| My appointments | ![Booking Lighthouse Report](assets/testing_files/lighthouse_myappointments.jpg) |
| Login | ![Login Lighthouse Report](assets/testing_files/lighthouse_login.jpg) |
| Signup | ![Signup Lighthouse Report](assets/testing_files/lighthouse_signup.jpg) |

## Tools Testing

### Responsiveness

* Chrome DevTools was used to test responsiveness in different screen sizes during the development process.

## Manual Testing

### Browser Compatibility

Browser | Outcome | Pass/Fail | 
--- | --- | --- |
Google Chrome | No appearance, responsiveness, or functionality issues.| <span style="color:green">Pass</span> |
Safari | No appearance, responsiveness, or functionality issues. | <span style="color:green">Pass</span> |
Mozilla Firefox | No responsiveness or functionality issues.| <span style="color:green">Pass</span> |

### Device Compatibility

Device | Operating System | Outcome | Pass/Fail
--- | --- | --- | --- |
MacBook Air 15" | macOS Sonoma | No appearance, responsiveness, or functionality issues. | <span style="color:green">Pass</span> |
iPhone SE | iOS 15 | No appearance, responsiveness, or functionality issues. | <span style="color:green">Pass</span> |

### Test Results

#### Login and Registration Forms

<table>
    <tr>
        <th>Feature</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan="4">Login Page</td>
        <td>Form Input</td>
        <td>Accepts valid username/email and password</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Submit Button</td>
        <td>Logs user in with correct credentials</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Forgot Password Link</td>
        <td>Links to password reset page</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Register Link</td>
        <td>Links to registration page</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan="5">Registration Page</td>
        <td>Form Fields</td>
        <td>All required fields validate correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Password Validation</td>
        <td>Ensures passwords match and meet requirements</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Submit Button</td>
        <td>Creates account and sends verification email</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Email Verification</td>
        <td>Verification email sent and link works correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Login Link</td>
        <td>Links to login page for existing users</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Base HTML Features

<table>
    <tr>
        <th>Feature</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan="5">Navigation Bar</td>
        <td>Sports Sole logo</td>
        <td>Clicking the logo redirects to the Home page</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Search Bar</td>
        <td>Search input works and returns relevant results</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>My Account</td>
        <td>Dropdown shows appropriate options for logged in/out users</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Shopping Bag</td>
        <td>Shows correct total and links to shopping bag page</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Main Navigation Menu</td>
        <td>Navigation links work correctly (Products, Men's, Women's, Special)</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan="4">Footer</td>
        <td>Contact link</td>
        <td>Redirects to contact form</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>FAQ link</td>
        <td>Redirects to FAQ section</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Newsletter Signup link</td>
        <td>Redirects to newsletter signup</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Social Links</td>
        <td>All social links work correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

<!-- HOME PAGE -->
#### Home Page Features

<table>
    <tr>
        <th>Feature</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td>Hero Section</td>
        <td>Shop Now button, Hero Image</td>
        <td>Shop Now button directs to Products, image responsive across different devices</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>New Arrivals</td>
        <td>Product Cards</td>
        <td>Links to correct product details pages</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Newsletter Signup</td>
        <td>Email Input, Submit Button, Success Message</td>
        <td>Validates correctly, subscribes user successfully, displays confirmation</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Display Testimonials</td>
        <td>Testimonial Cards, Rating Display</td>
        <td>Shows approved testimonials and ratings</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Contact Form</td>
        <td>Form Fields, Submit Button, Form Feedback</td>
        <td>Validates inputs, shows success/error messages</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Display FAQs</td>
        <td>FAQ List, Accordion Function</td>
        <td>Shows FAQs correctly and expands/collapses</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

<!-- PRODUCTS -->
#### Products Page

<table>
    <tr>
        <th>Feature</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td>Category Filters</td>
        <td>Category Selection</td>
        <td>Displays only products within selected category</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Sorting</td>
        <td>Sort Options</td>
        <td>Allows sorting by price, rating, name, and category in ascending/descending order</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Product Cards</td>
        <td>Product Image and Name</td>
        <td>Shows correct product image, name, and category</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Discounted Price Display</td>
        <td>Discount Price</td>
        <td>Displays discounted price alongside original price when applicable</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Rating Display</td>
        <td>Star Rating</td>
        <td>Shows average star rating if available</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Back to Top Button</td>
        <td>Scroll to Top</td>
        <td>Scrolls user back to the top of the page</td>
        <td>Pass</td>
    </tr>
</table>

<!-- PRODUCT DETAIL PAGE -->
#### Product Detail Page

<table>
    <tr>
        <th>Feature</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td>Product Images</td>
        <td>Display main product image or fallback image</td>
        <td>Main image and fallback image load correctly</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Product Price Display</td>
        <td>Show price and discounted price if applicable</td>
        <td>Displays correct price, with original crossed out if discounted</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Product Category Link</td>
        <td>Click category name</td>
        <td>Redirects user to filtered products by selected category</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Product Rating</td>
        <td>Display average rating</td>
        <td>Shows correct rating or "No Rating" if unavailable</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Product Description</td>
        <td>Show detailed description</td>
        <td>Displays full product description accurately</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Size Selector</td>
        <td>Select size from dropdown</td>
        <td>Dropdown shows available sizes and validates selection</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Quantity Selector</td>
        <td>Adjust quantity using increment and decrement buttons</td>
        <td>Quantity updates correctly within set limits (1–99)</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Add to Bag Button</td>
        <td>Click "Add to Bag"</td>
        <td>Adds selected size and quantity to shopping bag</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Keep Shopping Button</td>
        <td>Click "Keep Shopping"</td>
        <td>Redirects user to Products page</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Add to Wishlist Button</td>
        <td>Click "Wishlist" button</td>
        <td>Adds product to user’s wishlist or shows it is already added</td>
        <td>Pass</td>
    </tr>
</table>

<!-- SHOPPING BAG -->
#### Shopping Bag

<table>
    <tr>
        <th>Feature</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan="2">Bag Summary</td>
        <td>Bag Header</td>
        <td>Displays the bag header correctly</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Bag Totals Display</td>
        <td>Shows the total amount in the bag</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Product Details</td>
        <td>Product Information Display</td>
        <td>Shows product name, size, and price for each item</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Quantity Update</td>
        <td>Quantity Selector</td>
        <td>Allows users to update quantity directly in bag</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Remove Item</td>
        <td>Remove Button</td>
        <td>Removes item from the bag and refreshes page</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Subtotal Calculation</td>
        <td>Subtotal Display for Each Item</td>
        <td>Shows correct subtotal based on quantity and price</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Total Calculation</td>
        <td>Total Price Calculation</td>
        <td>Calculates and displays the total cost for all items</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Checkout Button</td>
        <td>Proceed to Checkout Button</td>
        <td>Directs user to the checkout page when clicked</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Back to Top Button</td>
        <td>Back-to-Top Function</td>
        <td>Scrolls user to the top of the page</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Empty Bag Message</td>
        <td>Empty State Display</td>
        <td>Displays a message and 'Keep Shopping' link if bag is empty</td>
        <td>Pass</td>
    </tr>
</table>

<!-- CHECKOUT PAGES -->
#### Checkout Pages

<table>
    <tr>
        <th>Feature</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan="2">Order Summary</td>
        <td>Display Order Summary</td>
        <td>Shows summary of items in the order with correct quantities, prices, and subtotal</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Grand Total Calculation</td>
        <td>Correctly calculates order total, delivery cost, and grand total</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Checkout Form</td>
        <td>Order Form Fields</td>
        <td>Form fields for name, email, address, and phone validate correctly</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan="2">Payment Processing</td>
        <td>Stripe Payment Element</td>
        <td>Stripe card element appears and accepts valid payment details</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Payment Confirmation</td>
        <td>Displays a confirmation message when payment is processed successfully</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Save Information</td>
        <td>Save Delivery Info Option</td>
        <td>Allows logged-in users to save delivery information for future orders</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan="2">Checkout Success</td>
        <td>Order Confirmation Message</td>
        <td>Displays order confirmation message with order number and email confirmation</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Order Details Display</td>
        <td>Shows details of the completed order, including delivery address and billing information</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Profile Update</td>
        <td>Profile Information Update</td>
        <td>Updates user profile with saved delivery information when selected</td>
        <td>Pass</td>
    </tr>
</table>

<!-- MY PROFILE PAGE -->
#### My Profile Page

<table>
    <tr>
        <th>Feature</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td>Default Delivery Info</td>
        <td>Enter form details and click update</td>
        <td>Updates are successful and stored</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Order History</td>
        <td>View list of past orders, click Order Number link</td>
        <td>Displays order history with links to order details</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan="4">Wishlist Management</td>
        <td>Wishlist Accessibility</td>
        <td>Wishlist is accessible from the profile page</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Item Display</td>
        <td>Displays all items currently in the wishlist</td>
        <td>Shows each item’s image, name, and price correctly</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Remove Items</td>
        <td>Click 'Remove' button on an item in the wishlist</td>
        <td>Removes item from the wishlist and updates display</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Empty State</td>
        <td>Remove all items, check empty state message</td>
        <td>Displays 'Your wishlist is empty' message when no items</td>
        <td>Pass</td>
    </tr>
</table>

<!-- ADMIN ADD PRODUCT PAGE -->
#### Admin Add Product Page

<table>
    <tr>
        <th>Feature</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td>Form Fields</td>
        <td>Complete all fields with valid data</td>
        <td>All fields accept valid inputs and validate correctly</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Product Image Upload</td>
        <td>Upload an image for the product</td>
        <td>Image file is successfully uploaded and displays correctly</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Product Detail Image Upload</td>
        <td>Upload a detailed image for the product</td>
        <td>Detail image file uploads successfully and displays correctly</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Cancel Button</td>
        <td>Click "Cancel" button</td>
        <td>Redirects user back to the Products page without saving changes</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Add Product Button</td>
        <td>Click "Add Product" button</td>
        <td>Submits the form and adds the new product to the product list</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>CSRF Protection</td>
        <td>Submit form without valid CSRF token</td>
        <td>Form submission is blocked to prevent CSRF attacks</td>
        <td>Pass</td>
    </tr>
</table>

<!-- ADMIN EDIT PRODUCT PAGE -->
#### Admin Edit Product Page

<table>
    <tr>
        <th>Feature</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td>Form Fields</td>
        <td>Edit all fields with valid data</td>
        <td>All fields accept updated inputs and validate correctly</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Pre-filled Data</td>
        <td>Check pre-filled form values</td>
        <td>Form loads with current product data pre-filled</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Product Image Update</td>
        <td>Upload a new image for the product</td>
        <td>New image file uploads successfully and replaces previous image</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Cancel Button</td>
        <td>Click "Cancel" button</td>
        <td>Redirects user back to the Products page without saving changes</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Update Product Button</td>
        <td>Click "Update Product" button</td>
        <td>Submits the form and updates the product with new data</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>CSRF Protection</td>
        <td>Submit form without valid CSRF token</td>
        <td>Form submission is blocked to prevent CSRF attacks</td>
        <td>Pass</td>
    </tr>
</table>

### Error Handling on Forms

<table>
    <tr>
        <th>Feature</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td>Registration Form</td>
        <td>Submit form with missing required fields</td>
        <td>Displays error message indicating required fields</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Login Form</td>
        <td>Enter incorrect credentials and submit</td>
        <td>Displays error message for invalid login</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Profile Update Form</td>
        <td>Submit form with invalid phone number format</td>
        <td>Displays error message indicating incorrect format</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Profile Update Form</td>
        <td>Submit form with empty required fields</td>
        <td>Displays error message indicating required fields</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Checkout Form</td>
        <td>Leave required fields blank and submit</td>
        <td>Displays error message for missing information</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Checkout Form</td>
        <td>Enter invalid email format</td>
        <td>Displays error message indicating invalid email format</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Contact Form</td>
        <td>Submit form with empty message field</td>
        <td>Displays error message indicating message is required</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Contact Form</td>
        <td>Enter invalid email format in email field</td>
        <td>Displays error message indicating invalid email format</td>
        <td>Pass</td>
    </tr>
</table>