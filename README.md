# Sports Sole

Sports Sole is your go-to online platform for high-quality sneakers designed to meet the needs of athletes, casual wearers, and sneaker enthusiasts alike. Whether you're searching for performance running shoes, stylish casual sneakers, or durable basketball shoes, Sports Sole offers a wide selection of top brands and the latest models. At Sports Sole, we’re committed to helping you find the perfect pair for every step.

Visit the deployed website [https://sports-sole-d03df7b3c157.herokuapp.com/].

## Table of Contents

1. [User Experience (UX)](#user-experience-ux)
    1. [Strategy](#strategy)
        1. [Project Goals](#project-goals)
        2. [User Stories](#user-stories)
        3. [Strategy Table](#strategy-table)
    2. [Scope](#scope)
        1. [Kanban Board](#kanban-board)
    3. [Structure](#structure)
        1. [Flowchart](#flowchart)
        3. [Database model](#database-model)
    4. [Skeleton](#skeleton)
        1. [Wireframe](#wireframe)
    5. [Surface](#surface)
        1. [Color Scheme](#color-scheme)
        2. [Typography](#typography)
2. [Features](#features)
    1. [General](#general)
    2. [Home Page](#home-page)
    3. [About Page](#about-page)
    4. [Treatments](#treatments)
    5. [My Appointments](#my-appointments)
    6. [Error Handling](#user-profile)
    7. [Authentication Pages](#authentication-pages)
3. [Technologies Used](#technologies-used)
    1. [Languages Used](#languages-used)
    2. [Libraries and Frameworks](#libraries-and-frameworks)
    3. [Packages / Dependencies Installed](#packages--dependencies-installed)
    4. [Database Management](#database-management)
    5. [Tools and Programs](#tools-and-programs)
4. [Testing](#testing)
    1. [Go to TESTING.md](https://github.com/Alvor1991/PP4-SportsTherapy/blob/main/TESTING.md)
5. [Deployment](#deployment)
6. [Finished Product](#finished-product)
7. [Credits](#credits)
8. [Known Bugs](#known-bugs)
9. [Acknowledgements](#acknowledgements)

***

## User Experience (UX)

### Strategy

#### Project Goals

Sports Sole is a B2C (Business to Consumer) e-commerce platform specializing in sports footwear. The application serves as a direct bridge between the business and individual consumers, offering a comprehensive range of sports shoes.

##### Business Model

The site operates on a B2C model where:
- Products are sold directly to end consumers
- Customer accounts allow for personalized shopping experiences
- Direct marketing through newsletter subscriptions
- Customer engagement through testimonials and FAQs

##### Target Audience

- Sports enthusiasts looking for quality footwear
- Casual shoppers seeking athletic shoes
- Customers interested in both performance and style
- People looking for specific types of sports shoes (running, basketball, etc.)

##### Marketing Strategy

1. **Email Marketing**
   - Newsletter subscription feature to build customer database
   - Keep customers informed about new products and offers

2. **Customer Engagement**
   - Customer testimonials to build trust
   - FAQ section to provide immediate answers to common queries
   - Contact form for customer support

3. **User Experience**
   - Easy navigation through product categories
   - Detailed product information and images
   - Secure user accounts and checkout process
   - Order history and profile management

##### Site Owner Goals

- Provide a professional and trustworthy e-commerce platform
- Build and maintain a loyal customer base
- Efficiently manage product inventory
- Drive sales through effective product presentation
- Gather customer data through newsletter signups

#### User Stories

Shopper Stories:
1. View a List of Sneakers
2. See Detailed Information for Sneakers
3. Quickly Identify Deals and Discounts
4. View the Total Cost of Selected Items
5. Register for an Account
6. Log In or Log Out of My Account
7. Recover My Password
8. Receive an Email Confirmation After Registering
9. Have a Personalized User Profile
10. Sort Sneakers by Price, Rating, or Category
11. Sort Sneakers by Category
12. Search for Sneakers by Name or Description
13. Filter Products Across Multiple Categories
14. Select Size and Quantity of Sneakers
15. View Final Cost Including Taxes and Shipping
16. Complete My Purchase Securely
17. Newsletter Signup
23. Contact Form
24. Wishlist/Favorites Feature
25. Post-Purchase Product Review System

Admin Stories:

18. Add Product
19. Edit/Update Product
20. Delete Product
21. Client Testimonial Management
22. FAQ Management

#### Kanban board

**Sprint 1 - Basic Product Viewing and User**

<img src="assets/readme_files/sprint1.png" alt="User Stories Progress - Sprint 1" height="500px">

**Sprint 2 - Product Management and User Profiles**  

<img src="assets/readme_files/sprint2.png" alt="User Stories Progress - Sprint 2" height="500px">

**Sprint 3 - Shopping Bag and Checkout Process**  

<img src="assets/readme_files/sprint3.png" alt="User Stories Progress - Sprint 3" height="500px">

**Sprint 4 - Checkout Process - Part**  

<img src="assets/readme_files/sprint4.png" alt="User Stories Progress - Sprint 4" height="500px">

**Sprint 5 - Sorting, Searching, and Additional Features**  

<img src="assets/readme_files/sprint5.png" alt="User Stories Progress - Sprint 5" height="500px">

**Sprint 6 - Marketing Features and Final Polishing**  

<img src="assets/readme_files/sprint6.png" alt="User Stories Progress - Sprint 6" height="500px">

### Structure

#### Flowchart

The website is organized using a [Mermaid](https://mermaid.js.org/) Flowchart to illustrate the user journey and interactions, ensuring intuitive navigation and a seamless user experience. The chart outlines the interactions available to both logged-in and logged-out users, illustrating how they navigate through the site's features.

![Sorts Sole website map](assets/readme_files/flowchart.png)

##### User Flow

#### Database Model

The database model was designed using [drawsql](https://drawsql.app/) and is managed with [PostgreSQL](https://www.postgresql.org/), a relational database.

![Sports Sole database model](assets/readme_files/erdiagram.png)

### Skeleton

#### Wireframes

[Balsamiq](https://balsamiq.com/) was used to create a layout of the website in the planning phase. Here are my initial designs: 

Page | Desktop Version | Mobile Version
--- | --- | ---
Login | ![Desktop Login wireframe image](assets/wireframes/login.png) | ![Mobile Login wireframe image](assets/wireframes/login_mobile.png)
Sign Up | ![Desktop Sign Up wireframe image](assets/wireframes/signup.png) | ![Mobile Sign Up wireframe image](assets/wireframes/signup_mobile.png)
Home | ![Desktop Home wireframe image](assets/wireframes/index.png) | ![Mobile Home wireframe image](assets/wireframes/index_mobile.png)
Products | ![Desktop About wireframe image](assets/wireframes/products.png) | ![Mobile About wireframe image](assets/wireframes/products_mobile.png)
Product Detail | ![Desktop Treatments wireframe image](assets/wireframes/product_detail.png) | ![Mobile Treatments wireframe image](assets/wireframes/product_detail_mobile.png)
Bag | ![Book Appointment wireframe image](assets/wireframes/bag.png) | ![Mobile Book Appointment wireframe image](assets/wireframes/bag_mobile.png)
Checkout | ![View Appointments wireframe image](assets/wireframes/checkout.png) | ![Mobile View Appointments wireframe image](assets/wireframes/checkout_mobile.png)
My profile | ![View Appointments wireframe image](assets/wireframes/profile.png) | ![Mobile View Appointments wireframe image](assets/wireframes/profile_mobile.png)
Admin Add Product | ![View Appointments wireframe image](assets/wireframes/add_product.png) | ![Mobile View Appointments wireframe image](assets/wireframes/add_product_mobile.png)


## Agile Development Plan

### Epics and User Stories

| Epic ID | Epic Name | User Stories |
|---------|-----------|--------------|
| E1 | Viewing and Navigation | 1. View a List of Sneakers (#1)<br>2. See Detailed Information for Sneakers (#2)<br>3. Quickly Identify Deals and Discounts (#3)<br>4. View the Total Cost of Selected Items (#4) |
| E2 | Registration and User Accounts | 5. Register for an Account (#5)<br>6. Log In or Log Out of My Account (#6)<br>7. Recover My Password (#7)<br>8. Receive an Email Confirmation After Registering (#8)<br>9. Have a Personalized User Profile (#9)<br>24. Wishlist/Favorites feature (#24) |
| E3 | Sorting and Searching | 10. Sort Sneakers by Price, Rating, or Category (#10)<br>11. Sort Sneakers by Category (#11)<br>12. Search for Sneakers by Name or Description (#12)<br>13. Filter Products Across Multiple Categories (#13) |
| E4 | Purchasing and Checkout | 14. Select Size and Quantity of Sneakers (#14)<br>15. View Final Cost Including Taxes and Shipping (#15)<br>16. Complete My Purchase Securely (#16) |
| E5 | Marketing and Customer Engagement | 17. Newsletter Signup (#17)<br>18. Client Testimonial Management (#21)<br>19. FAQ Management (#22)<br>20. Contact Form (#23) |
| E6 | Admin and Store Management | 21. Add Product (#18)<br>22. Edit/Update Product (#19)<br>23. Delete Product (#20) |
| E7 | Future Enhancements | 25. Post-Purchase Product Review System (#25) |


### MoSCoW Prioritization

| Priority    | User Stories                                                                                           |
|-------------|-------------------------------------------------------------------------------------------------------|
| Must Have   | 1. View a List of Sneakers (#1)<br>2. See Detailed Information for Sneakers (#2)<br>3. Register for an Account (#5)<br>4. Log In or Log Out of My Account (#6)<br>5. Select Size and Quantity of Sneakers (#14)<br>6. Complete My Purchase Securely (#16)<br>7. Add Product (#18)<br>8. Edit/Update Product (#19)<br>9. Delete Product (#20) |
| Should Have | 1. View the Total Cost of Selected Items (#4)<br>2. Recover My Password (#7)<br>3. Receive an Email Confirmation After Registering (#8)<br>4. Have a Personalized User Profile (#9)<br>5. Search for Sneakers by Name or Description (#12)<br>6. View Final Cost Including Taxes and Shipping (#15) |
| Could Have | 1. Quickly Identify Deals and Discounts (#3)<br>2. Sort Sneakers by Price, Rating, or Category (#10)<br>3. Sort Sneakers by Category (#11)<br>4. Filter Products Across Multiple Categories (#13)<br>5. Newsletter Signup (#17)<br>6. Client Testimonial Management (#21)<br>7. FAQ Management (#22)<br>8. Contact Form (#23)<br>9. Wishlist/Favorites feature (#24) |
| Won't Have | 1. Post-Purchase Product Review System (#25) |

### Sprint Planning

| Sprint     | Duration   | User Stories                        | Milestone                                               |
|------------|------------|-------------------------------------|---------------------------------------------------------|
| Sprint 1   | 2 weeks    | #1, #2, #5, #6                      | Basic product catalog and user account functionality     |
| Sprint 2   | 2 weeks    | #18, #19, #20, #7, #8, #9           | Admin product management and enhanced user account features |
| Sprint 3   | 2 weeks    | #4, #14, #15                        | Functional shopping bag and initial checkout process     |
| Sprint 4   | 2 weeks    | #16                                 | Secure checkout process completion                      |
| Sprint 5   | 2 weeks    | #10, #11, #12, #13, #3              | Implemented search, sorting, and special offers features |
| Sprint 6   | 2 weeks    | #17, #21, #22, #23, #24             | Implement marketing features, wishlist functionality, bug fixes, and final testing |

### Implementation Process

Progress, challenges faced, and solutions implemented to demonstrate agile methodology application.

#### Sports Sole User Flow Chart

## Persistent Elements (Available on All Pages)

### Header
- Logo (links to Home)
- Search Bar
- My Account Dropdown
  - For non-authenticated users:
    -> Register
    -> Login
  - For authenticated users:
    -> My Profile
    -> Logout
  - For superusers:
    -> Product Management
- Shopping Bag (with total amount)
- Free Delivery Threshold Banner

### Main Navigation
- Home
- All Products
  -> By Price
  -> By Rating
  -> By Category
  -> All Products
- Women's
  -> Running Shoes
  -> Training and Gym Shoes
  -> Basketball Shoes
  -> Casual Sneakers
  -> All Women's Sneakers
- Men's
  -> Running Shoes
  -> Training and Gym Shoes
  -> Basketball Shoes
  -> Casual Sneakers
  -> All Men's Sneakers
- Special Offers
  -> New Arrivals
  -> Clearance

### Footer
- Quick Links (Home, Shop,)
- Customer Service (Contact, FAQ)
- Social Media Links
- Newsletter Signup

## Page-Specific Flows

### 1. Home Page (index.html)
- Hero Section with "Shop Now" CTA
- New Arrivals Section
- Customer Testimonials
- Newsletter Signup Form
- Contact Form
- FAQ Section

### 2. Products Page (products.html)
- Product Listing with Filtering and Sorting Options
- Category Badges
- Pagination (if implemented)
- For superusers: Edit/Delete product options

### 3. Product Detail Page (product_detail.html)
- Product Image (with zoom option if implemented)
- Product Information (name, price, category, rating)
- Size Selection
- Quantity Selection
- Add to Bag functionality
- For superusers: Edit/Delete product options

### 4. Shopping Bag Page (bag.html)
- List of Items in Bag
- Update Quantity functionality
- Remove Item functionality
- Subtotal for each item
- Order Total, Delivery Cost, Grand Total
- "Keep Shopping" and "Secure Checkout" options

### 5. Checkout Page (checkout.html)
- Order Summary
- Delivery Information Form
- Payment Information (Stripe integration)
- Option to save delivery info to profile (for authenticated users)
- Complete Order functionality

### 6. Checkout Success Page
- Order confirmation details
- Order history

### 7. Profile Page (profile.html)
- Default Delivery Information Form
- Order History Table

### 8. Product Management (for superusers)
- Add Product Form
- Edit Product Form

## User Interactions
- Receive and view toast messages for various actions
- Use of "Back to Top" button on longer pages
- Responsive design elements (e.g., collapsible navigation on mobile)

## Authentication Flows
- Registration Process
- Login Process
- Password Recovery Process

This comprehensive flow chart now accurately represents the full user experience on your Django Sports Sole website, incorporating all the elements from your provided templates and accounting for various user types and interactions.
