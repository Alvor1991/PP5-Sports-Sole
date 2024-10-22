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

* AC1: Given I am viewing a product, I can click a heart icon to add/remove it from my wishlist.
* AC2: When I access my profile, I can view all my wishlist items in one dedicated section.
* AC3: Given I am in my wishlist section, I can easily navigate to product details or remove items.

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

Warning: The type attribute is unnecessary for JavaScript resources.  
Fix: Removed type="text/javascript" from all script tags (HTML5 default).

Error: The aria-labelledby attribute must point to an element in the same document.  
Fix: Updated the id of Women’s to "womens-link" and Men’s to "mens-link" to match aria-labelledby.

Warning: Possible misuse of aria-label.  
Fix: Removed aria-label from dropdowns since aria-labelledby already handles accessibility.

Warning: The first occurrence of ID user-options was here.  
Fix: Renamed the duplicate id="user-options" to id="user-options-mobile" in the mobile navigation.

Warning: Possible misuse of aria-label.  
Fix: Removed aria-label="Search" from "fas fa-search" as it is unnecessary for purely decorative icons.

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

#### Signup Page

<table>
    <tr>
        <th>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Sign Up Form</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Form fields render correctly and accept user input.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Form fields are styled consistently with the overall design.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Sign Up Button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the button submits the form and attempts to register the user.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Button has a hover effect and is styled consistently with overall design.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Sign Up Link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the sign up page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Link has a hover effect and is styled consistently with overall design.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Login Page

<table>
    <tr>
        <th>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Login Form</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Form fields render correctly and accept user input.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Form fields are styled consistently with the overall design.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Sign In Button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the button submits the form and attempts to log the user in.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Button has a hover effect and is styled consistently with overall design.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Signup Link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the signup page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Link has a hover effect and is styled consistently with overall design.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>