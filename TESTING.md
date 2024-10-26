# Sports Therapy Website Testing

[Back to the README.md file](https://github.com/Alvor1991/PP4-SportsTherapy)  

[View the live website here](https://pp4-physio-4e914098e1ff.herokuapp.com)  

## Table of Contents

1. [Testing User Stories](#testing-user-stories)
2. [Code Validation](#code-validation)
3. [Accessibility](#accessibility)
4. [Tools Testing](#tools-testing)
5. [Manual Testing](#manual-testing)

***

## Testing User Stories

### 1. View a List of Sneakers**
* AC1: User can see a list of sneakers on the main products page.
* AC2: Sneakers are displayed with basic information (name, image, price).
* AC3: User can navigate through multiple pages of sneakers if applicable.

### 2. See Detailed Information for Sneakers**
* AC1: User can click on a sneaker to view its detailed information.
* AC2: Detailed view shows price, description, rating, and available sizes.
* AC3: User can see sneaker images clearly.

### 3. Quickly Identify Deals and Discounts**
* AC1: Special offers are clearly marked on the product list.
* AC2: User can easily navigate to a dedicated special offers section.
* AC3: Discounts or deal prices are prominently displayed.

### 4. View the Total Cost of Selected Items**
* AC1: Running total is visible in the shopping bag icon.
* AC2: Total updates immediately when adding or removing items.
* AC3: User can view a detailed breakdown in the shopping bag.

### 5. Register for an Account**
* AC1: User can access a registration form from the main navigation.
* AC2: Form validates input and creates account with valid information.
* AC3: User receives confirmation of successful registration.

### 6. Log In or Log Out of My Account**
* AC1: Registered user can log in with correct credentials.
* AC2: Logged-in user can easily log out from any page.
* AC3: User's login status is clearly indicated in the navigation.

### 7. Recover My Password**
* AC1: User can request password reset from login page.
* AC2: Reset instructions are sent to user's email.
* AC3: User can set a new password and access their account.

### 8. Receive an Email Confirmation After Registering**
* AC1: User receives an email shortly after registration.
* AC2: Email contains confirmation link or welcome message.
* AC3: User can verify their email address if required.

### 9. Have a Personalized User Profile**
* AC1: Logged-in user can access their profile page.
* AC2: Profile displays order history and saved information.
* AC3: User can update their default delivery information.

### 10. Sort Sneakers by Price, Rating, or Category**
* AC1: User can sort sneakers by price (low to high, high to low).
* AC2: User can sort sneakers by rating.
* AC3: User can sort sneakers by category.

### 11. Sort Sneakers by Category**
* AC1: User can navigate to a specific sneaker category.
* AC2: Sorting options are available within the category view.
* AC3: Category-specific sorting (if applicable) is available.

### 12. Search for Sneakers by Name or Description**
* AC1: Search bar is easily accessible from all pages.
* AC2: Search returns relevant results based on sneaker name or description.
* AC3: User can view the number of search results.

### 13. Filter Products Across Multiple Categories**
* AC1: User can select multiple categories to filter sneakers.
* AC2: Filtered results show sneakers from all selected categories.
* AC3: User can easily add or remove categories from the filter.

### 14. Select Size and Quantity of Sneakers**
* AC1: Size options are clearly displayed on the product page.
* AC2: Quantity can be easily adjusted before adding to bag.
* AC3: Selected size and quantity are confirmed when adding to bag.

### 15. View Final Cost Including Taxes and Shipping**
* AC1: Final cost breakdown is shown before completing purchase.
* AC2: Taxes and shipping costs are clearly itemized.
* AC3: User can see how costs change based on delivery options.

### 16. Complete My Purchase Securely**
* AC1: Checkout process guides user through payment steps.
* AC2: Payment form is clear and easy to fill out.
* AC3: User receives clear confirmation of successful purchase.

### 17. Newsletter Signup**
* AC1: Newsletter signup form is easily accessible.
* AC2: User can enter email and subscribe with one click.
* AC3: Confirmation of subscription is provided to the user.

### 18. Add Product**
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
* AC3: Testimonials are displayed on the appropriate page(s).

### 22. FAQ Management

* AC1: Admin can add new FAQ entries.
* AC2: Existing FAQs can be updated or deleted.
* AC3: FAQs are organized and easily accessible to users.

### 23. Contact Form

* AC1: Users can easily find and access the contact form.
* AC2: Form includes fields for name, email, and message.
* AC3: User receives confirmation when message is sent successfully.

### 24. Wishlist/Favorites Feature

* AC1: Given I am viewing a product, I can click a button to add it to my wishlist (receiving a toast success message), or if the item is already in my wishlist, I will receive a toast message indicating this.
* AC2: When I access my profile, I can view all my wishlist items in a dedicated section.
* AC3: Given I am viewing my wishlist in my profile, I can remove items using a button beneath each product.

### 25. Post-Purchase Product Review System

* AC1: Given I have received my order, I receive an email invitation to review my purchased items.
* AC2: When clicking the review link in the email, I can rate the product and write my review.
* AC3: When viewing products, I can see verified purchase reviews from other customers to help inform my decision.

## Code Validation

### HTML

The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the HTML code of the project to ensure there were no syntax errors.

W3C Markup Validator found the following errors in `base.html`:

<div style="display: flex; justify-content: space-between;">
    <img src="assets/testing_files/base_html_error1.png" alt="base.html validation errors image" width="45%" style="margin-bottom: 20px;">
    <img src="assets/testing_files/base_html_error2.png" alt="base.html validation errors image" width="45%" style="margin-bottom: 20px;">
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

W3C Markup Validator found the following errors in `treatments.html`:

![treatments.html validation errors image](assets/testing_files/treatment_errors.png)

* To resolve the error, I wrapped content with a div instead of p and removed redundant closing tags.


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


#### Login Page

<table>
   <tr>
       <th colspan=2>Feature</th>
       <th>Users</th>
       <th>Test</th>
       <th>Outcome</th>
       <th>Pass/Fail</th>
   </tr>
   <tr>
       <td rowspan=4>Login Form</td>
       <td rowspan=2>Form Input</td>
       <td rowspan=2>All</td>
       <td>Functionality</td>
       <td>Form accepts username/email and password, validates input</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Form is clearly laid out and responsive</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td rowspan=2>Submit Button</td>
       <td rowspan=2>All</td>
       <td>Functionality</td>
       <td>Logs user in when credentials are correct</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Button is prominent with hover effect</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td rowspan=4>Additional Links</td>
       <td rowspan=2>Forgot Password</td>
       <td rowspan=2>All</td>
       <td>Functionality</td>
       <td>Links to password reset page</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Link is clearly visible with hover effect</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td rowspan=2>Register Link</td>
       <td rowspan=2>All</td>
       <td>Functionality</td>
       <td>Links to registration page</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Link is clearly visible with hover effect</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
</table>

#### Registration Page

<table>
   <tr>
       <th colspan=2>Feature</th>
       <th>Users</th>
       <th>Test</th>
       <th>Outcome</th>
       <th>Pass/Fail</th>
   </tr>
   <tr>
       <td rowspan=6>Registration Form</td>
       <td rowspan=2>Form Fields</td>
       <td rowspan=2>All</td>
       <td>Functionality</td>
       <td>All required fields validate correctly (email, username, password)</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Form fields are clearly labeled and responsive</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td rowspan=2>Password Validation</td>
       <td rowspan=2>All</td>
       <td>Functionality</td>
       <td>Ensures passwords match and meet requirements</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Password requirements clearly displayed</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td rowspan=2>Submit Button</td>
       <td rowspan=2>All</td>
       <td>Functionality</td>
       <td>Creates account and sends verification email</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Button is prominent with hover effect</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td rowspan=4>Additional Features</td>
       <td rowspan=2>Email Verification</td>
       <td rowspan=2>All</td>
       <td>Functionality</td>
       <td>Verification email sent and link works correctly</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Verification messages clearly displayed</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td rowspan=2>Login Link</td>
       <td rowspan=2>All</td>
       <td>Functionality</td>
       <td>Links to login page for existing users</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Link is clearly visible with hover effect</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
</table>

#### Base HTML 

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=16>Navigation Bar</td>
        <td rowspan=2>Sports Sole logo</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the logo redirects to the Home page</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Responsive on smaller screens</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Search Bar</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Search input works and returns relevant results</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Search bar is clearly visible and responsive</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>My Account Dropdown</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Dropdown menu shows appropriate options for logged in/out users</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Dropdown menu styled consistently and responsive</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Shopping Bag</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Shows correct total and links to shopping bag page</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Updates visually when items added/removed</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Main Nav Menu</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>All navigation links work correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Responsive design works on all screen sizes</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Home Page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=4>Hero Section</td>
        <td rowspan=2>Shop Now button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Redirects to products page when clicked</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Button is responsive and hover effect works</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Hero Image</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Image loads correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Image is responsive on all screen sizes</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=4>New Arrivals</td>
        <td rowspan=2>Product Cards</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Links to correct product details pages</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Cards display correctly and are responsive</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Products Page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=6>Product Filters</td>
        <td rowspan=2>Category Filtering</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Filters products by selected category</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Filter options clearly displayed and responsive</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Sort Selector</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Sorts products by price, rating, name as selected</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Dropdown styled consistently and responsive</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Price Filtering</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Filters products within selected price range</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Price filter options clearly displayed</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=4>Product Cards</td>
        <td rowspan=2>Product Information</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Displays correct product details and links to product page</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Cards display consistently and are responsive</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Edit/Delete Links</td>
        <td rowspan=2>Admin</td>
        <td>Functionality</td>
        <td>Edit and delete options visible only to admin</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Links styled appropriately and visible</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Product Detail Page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=4>Product Images</td>
        <td rowspan=2>Main Image</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Image loads correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Image is responsive and maintains aspect ratio</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Additional Images</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Additional product images load and display correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Images are responsive and well-organized</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=6>Product Controls</td>
        <td rowspan=2>Size Selector</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Size selection works correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Dropdown styled consistently</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Quantity Selector</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Quantity can be adjusted within valid range</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Controls are clear and responsive</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Add to Bag Button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Adds selected product to shopping bag</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Button is prominent and shows hover effect</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Keep Shopping</td>
        <td rowspan=2>Return Link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Returns to products page</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Link is clearly visible with hover effect</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Shopping Bag Page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=6>Product Information</td>
        <td rowspan=2>Product Details</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Shows correct product image, name, size, and price</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Information clearly laid out and responsive</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Quantity Adjuster</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Updates quantity correctly, min/max limits work</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Controls are clear and easy to use</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Remove Link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Removes item from bag when clicked</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Link is clearly visible with hover effect</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=6>Bag Summary</td>
        <td rowspan=2>Subtotal</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Displays correct subtotal for all items</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Clearly displayed and updates dynamically</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Delivery Cost</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Calculates delivery cost correctly, shows free delivery threshold</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Delivery information clearly displayed</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Grand Total</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Shows correct total including delivery</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Total prominently displayed and updates correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=4>Action Buttons</td>
        <td rowspan=2>Keep Shopping</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Returns to products page</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Button clearly visible with hover effect</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Secure Checkout</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Proceeds to checkout when clicked</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Button prominent with hover effect</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Checkout Page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=8>Order Form</td>
        <td rowspan=2>Personal Details</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Form validates full name, email, phone number correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Fields clearly labeled and responsive</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Delivery Information</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Address fields validate and save correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Address fields properly formatted and clear</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Save Info Checkbox</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Saves delivery info to profile when checked</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Checkbox clearly visible with label</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Login/Register Link</td>
        <td rowspan=2>Unregistered</td>
        <td>Functionality</td>
        <td>Links to login/register page</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Links clearly visible and styled</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=6>Payment Section</td>
        <td rowspan=2>Stripe Element</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Card input validates and processes payment</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Payment element styled consistently</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Error Messages</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Shows relevant error messages for invalid inputs</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Error messages clearly visible</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Loading Overlay</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Shows during payment processing</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Overlay visible and prevents double submission</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=6>Order Summary</td>
        <td rowspan=2>Item Details</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Shows correct items, quantities, and sizes</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Summary clearly laid out and readable</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Order Total</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Displays correct subtotal, delivery, and grand total</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Totals clearly displayed and formatted</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Action Buttons</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Adjust Bag and Complete Order buttons work correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Buttons prominently displayed with hover effects</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Profile Page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=6>Default Delivery Information</td>
        <td rowspan=2>Form Fields</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>All fields can be updated and saved correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Form is clearly laid out and responsive</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Update Button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Successfully updates delivery information</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Button is prominent with hover effect</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Country Selector</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Shows and selects countries correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Dropdown styled consistently with form</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=8>Order History</td>
        <td rowspan=2>Order List</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Shows all past orders with correct details</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Orders displayed in clear, organized manner</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Order Details Link</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Links to detailed view of past orders</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Links are clearly visible with hover effect</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Order Number</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Shows truncated order number with full number on hover</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Order numbers formatted consistently</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Order Information</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Displays correct date, items, and total for each order</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Information clearly laid out and readable</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=4>Success Messages</td>
        <td rowspan=2>Update Success</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Shows confirmation when profile is updated</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Message is clearly visible and properly styled</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Toast Messages</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Shows relevant toast messages for actions</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Toasts appear and disappear smoothly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Product Management

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=8>Add Product Form</td>
        <td rowspan=2>Category Selection</td>
        <td rowspan=2>Admin</td>
        <td>Functionality</td>
        <td>Correctly selects and assigns product category</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Dropdown is clearly visible and functional</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Product Details</td>
        <td rowspan=2>Admin</td>
        <td>Functionality</td>
        <td>All fields validate and save correctly (name, description, price)</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Form fields clearly labeled and organized</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Image Upload</td>
        <td rowspan=2>Admin</td>
        <td>Functionality</td>
        <td>Successfully uploads and displays product images</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Upload controls clearly visible and functional</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Submit Button</td>
        <td rowspan=2>Admin</td>
        <td>Functionality</td>
        <td>Successfully adds new product to database</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Button is prominent with hover effect</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=8>Edit Product</td>
        <td rowspan=2>Form Population</td>
        <td rowspan=2>Admin</td>
        <td>Functionality</td>
        <td>Form populates with current product information</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Existing data clearly displayed in form</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Image Update</td>
        <td rowspan=2>Admin</td>
        <td>Functionality</td>
        <td>Can update or remove existing images</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Current and new image preview displayed correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Update Button</td>
        <td rowspan=2>Admin</td>
        <td>Functionality</td>
        <td>Successfully updates product information</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Button clearly visible with hover effect</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Cancel Button</td>
        <td rowspan=2>Admin</td>
        <td>Functionality</td>
        <td>Returns to product detail page without changes</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Button clearly visible with hover effect</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=4>Delete Product</td>
        <td rowspan=2>Delete Button</td>
        <td rowspan=2>Admin</td>
        <td>Functionality</td>
        <td>Successfully removes product from database</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Delete button clearly visible in red</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Confirmation</td>
        <td rowspan=2>Admin</td>
        <td>Functionality</td>
        <td>Confirms before deleting product</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Confirmation message clearly visible</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=4>Access Control</td>
        <td rowspan=2>URL Access</td>
        <td rowspan=2>Non-Admin</td>
        <td>Functionality</td>
        <td>Redirects non-admin users attempting to access admin URLs</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Error messages displayed appropriately</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Admin Links</td>
        <td rowspan=2>Admin</td>
        <td>Functionality</td>
        <td>Admin-only links visible only to admin users</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Admin controls consistently styled</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Newsletter Management

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=6>Newsletter Signup</td>
        <td rowspan=2>Email Input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Validates email format and prevents duplicates</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Input field clearly visible and responsive</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Submit Button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Successfully subscribes user to newsletter</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Button prominent with hover effect</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Success Message</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Displays confirmation of successful signup</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Success message clearly visible</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Testimonials Management

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=8>Display Testimonials</td>
        <td rowspan=2>Testimonial Cards</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Displays all approved testimonials</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Cards properly formatted and responsive</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Rating Display</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Shows correct star rating for each testimonial</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Star ratings clearly visible</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Testimonial Text</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Displays full testimonial text correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Text properly formatted and readable</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Customer Name</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Shows customer name correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Name displayed appropriately</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=6>Admin Controls</td>
        <td rowspan=2>Add Testimonial</td>
        <td rowspan=2>Admin</td>
        <td>Functionality</td>
        <td>Successfully adds new testimonials</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Add form clearly laid out</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Edit Testimonial</td>
        <td rowspan=2>Admin</td>
        <td>Functionality</td>
        <td>Successfully edits existing testimonials</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Edit controls clearly visible</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Delete Testimonial</td>
        <td rowspan=2>Admin</td>
        <td>Functionality</td>
        <td>Successfully removes testimonials</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Delete controls prominently displayed</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### FAQ Management

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=6>Display FAQs</td>
        <td rowspan=2>FAQ List</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Shows all FAQ items in correct order</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>FAQs clearly laid out and readable</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Accordion Function</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Expands/collapses FAQ answers correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Smooth animation on expand/collapse</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Category Display</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Groups FAQs by category correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Categories clearly separated and labeled</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=6>Admin Controls</td>
        <td rowspan=2>Add FAQ</td>
        <td rowspan=2>Admin</td>
        <td>Functionality</td>
        <td>Successfully adds new FAQ items</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Add form clearly laid out</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Edit FAQ</td>
        <td rowspan=2>Admin</td>
        <td>Functionality</td>
        <td>Successfully edits existing FAQs</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Edit controls clearly visible</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Delete FAQ</td>
        <td rowspan=2>Admin</td>
        <td>Functionality</td>
        <td>Successfully removes FAQ items</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Delete controls prominently displayed</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Contact Form

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=8>Form Fields</td>
        <td rowspan=2>Name Field</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Validates and requires name input</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Field clearly labeled and visible</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Email Field</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Validates email format correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Field clearly labeled and visible</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Message Field</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Accepts and requires message input</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Text area properly sized and responsive</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Submit Button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Successfully submits form when valid</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Button prominent with hover effect</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=4>Form Feedback</td>
        <td rowspan=2>Success Message</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Shows success message after submission</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Success message clearly visible</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Error Messages</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Shows appropriate error messages for invalid inputs</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Error messages clearly visible</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Toast Messages

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=8>Success Toasts</td>
        <td rowspan=2>Add to Bag</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Shows when item added to bag</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Success style applied correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Profile Update</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Shows when profile updated</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Success style applied correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Order Confirmation</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Shows after successful order</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Success style applied correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Sign In/Out</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Shows on successful login/logout</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Success style applied correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=4>Error Toasts</td>
        <td rowspan=2>Form Errors</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Shows when form submission fails</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Error style applied correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Payment Errors</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Shows when payment fails</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Error style applied correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>


#### General Site Navigation

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=6>Header Consistency</td>
        <td rowspan=2>Navigation Bar</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Remains fixed at top across all pages</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Consistent styling across all pages</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Search Function</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Available and functional on all pages</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Search bar consistently styled</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Shopping Bag Icon</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Updates and accessible from all pages</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Consistently positioned and styled</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=6>Footer Consistency</td>
        <td rowspan=2>Footer Content</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>All links functional across pages</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Consistent styling across all pages</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Newsletter Signup</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Form accessible from all pages</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Consistently styled and positioned</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Social Links</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>All social links work correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Icons consistently styled</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Responsive Design Testing

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Device/Screen Size</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=8>Navigation Elements</td>
        <td rowspan=2>Desktop (>1024px)</td>
        <td rowspan=2>Large Screens</td>
        <td>Layout</td>
        <td>Full navigation bar displayed horizontally</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Functionality</td>
        <td>All navigation elements accessible</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Tablet (768px-1024px)</td>
        <td rowspan=2>Medium Screens</td>
        <td>Layout</td>
        <td>Navigation adapts to medium screens</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Functionality</td>
        <td>All features remain accessible</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Mobile (320px-767px)</td>
        <td rowspan=2>Small Screens</td>
        <td>Layout</td>
        <td>Hamburger menu appears, mobile-friendly layout</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Functionality</td>
        <td>Menu toggles correctly, all links work</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Small Mobile (<320px)</td>
        <td rowspan=2>Extra Small</td>
        <td>Layout</td>
        <td>Content remains accessible on very small screens</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Functionality</td>
        <td>All essential features usable</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=8>Content Layout</td>
        <td rowspan=2>Product Cards</td>
        <td rowspan=2>All Sizes</td>
        <td>Layout</td>
        <td>Cards resize and reflow appropriately</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Functionality</td>
        <td>All product information remains visible</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Forms</td>
        <td rowspan=2>All Sizes</td>
        <td>Layout</td>
        <td>Forms adjust to screen width</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Functionality</td>
        <td>All form fields remain usable</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Images</td>
        <td rowspan=2>All Sizes</td>
        <td>Layout</td>
        <td>Images scale proportionally</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Functionality</td>
        <td>Images load and display correctly</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Text Content</td>
        <td rowspan=2>All Sizes</td>
        <td>Layout</td>
        <td>Text remains readable at all sizes</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Functionality</td>
        <td>No text overflow or overlap issues</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Wishlist Feature

<table>
   <tr>
       <th colspan=2>Feature</th>
       <th>Users</th>
       <th>Test</th>
       <th>Outcome</th>
       <th>Pass/Fail</th>
   </tr>
   <tr>
       <td rowspan=6>Add to Wishlist Button</td>
       <td rowspan=2>Non-Logged In Users</td>
       <td rowspan=2>All</td>
       <td>Functionality</td>
       <td>Prompts user to sign in when clicked</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Button clearly visible on product detail page</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td rowspan=2>Logged In Users</td>
       <td rowspan=2>Registered</td>
       <td>Functionality</td>
       <td>Successfully adds item to wishlist</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Button indicates when item is in wishlist</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td rowspan=2>Button Position</td>
       <td rowspan=2>All</td>
       <td>Functionality</td>
       <td>Consistent location on all product detail pages</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Button styled consistently with site theme</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td rowspan=8>Toast Notifications</td>
       <td rowspan=2>Success Message</td>
       <td rowspan=2>Registered</td>
       <td>Functionality</td>
       <td>Shows when item successfully added to wishlist</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Toast includes product image and details</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td rowspan=2>Duplicate Item Alert</td>
       <td rowspan=2>Registered</td>
       <td>Functionality</td>
       <td>Shows alert when attempting to add existing item</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Alert message clearly indicates item is already in wishlist</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td rowspan=2>View Wishlist Button</td>
       <td rowspan=2>Registered</td>
       <td>Functionality</td>
       <td>Button in toast redirects to wishlist</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Button clearly visible in toast message</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td rowspan=2>Sign In Prompt</td>
       <td rowspan=2>Non-Registered</td>
       <td>Functionality</td>
       <td>Prompts non-logged in users to sign in</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Message clearly communicates requirement</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td rowspan=8>Wishlist Display</td>
       <td rowspan=2>Profile Integration</td>
       <td rowspan=2>Registered</td>
       <td>Functionality</td>
       <td>Wishlist accessible from profile page</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Wishlist section clearly organized in profile</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td rowspan=2>Item Display</td>
       <td rowspan=2>Registered</td>
       <td>Functionality</td>
       <td>Shows all wishlisted items correctly</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Items displayed with clear images and details</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td rowspan=2>Remove Items</td>
       <td rowspan=2>Registered</td>
       <td>Functionality</td>
       <td>Can remove items from wishlist</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Remove option clearly visible</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td rowspan=2>Empty State</td>
       <td rowspan=2>Registered</td>
       <td>Functionality</td>
       <td>Shows appropriate message when wishlist empty</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
   <tr>
       <td>Style</td>
       <td>Empty state message clearly displayed</td>
       <td><span style="color:green">Pass</span></td>
   </tr>
</table>