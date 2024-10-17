# Sports Sole

Sports Sole is your go-to online platform for high-quality sneakers designed to meet the needs of athletes, casual wearers, and sneaker enthusiasts alike. Whether you're searching for performance running shoes, stylish casual sneakers, or durable basketball shoes, Sports Sole offers a wide selection of top brands and the latest models. At Sports Sole, we’re committed to helping you find the perfect pair for every step.

Visit the deployed website [here]().

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

* Provide a user-friendly interface for clients to book sports therapy appointments.

* Implement a responsive design to ensure accessibility across various devices.

* Allow clients to manage their bookings easily through a personal dashboard.

* Ensure secure authentication and data handling.

#### User Stories

1. As a user, I can register an account so that I can book and manage my appointments online.

2. As an admin, I can manage website content so that I can keep info up-to-date and relevant for users.

3. As a user, I can access the website on any device so that I have a seamless experience on all devices.

4. As a user, I can view the home page to get an overview of services so I can learn more about the website.

5. As a user, I can view info about the therapist so that I can learn about their credentials and expertise.

6. As a user, I can view a list of available treatments so that I can choose the appropriate therapy session.

7. As a user, I can create an appointment so that I can schedule a therapy session.

8. As a user, I can view a list of my appointments so that I can see my scheduled therapy sessions.

9. As a user, I can update my appointments so that I can change the details of a scheduled session.

10. As a user, I can delete my appointments so that I can cancel a session I no longer need.

#### Strategy Table

Opportunity / Problem | Importance | Viability / Feasibility
--- | --- | ---
Responsive design | 5 | 5
Account registration | 5 | 5
Browse treatments | 5 | 5
Book appointments | 5 | 5
Manage appointments | 5 | 5
User appointments dashboard | 5 | 4
**Future Implementations:**
Integration with payment gateway | 3 | 2
Email notifications for booking confirmations | 3 | 2
Expand to include blog for sharing tips | 2 | 2
Expand to include more therapists | 2 | 2
**Total** | **40** | **37**


### Scope

According to the strategy table, not all features can be implemented in the first release of the project. For this reason, the project will be divided in multiple phases, as shown below:

| **First Phase**                   | **Second Phase**                                     |
|-----------------------------------|------------------------------------------------------|
| Responsive design                 | Integration with payment gateway                     |
| Account registration              | Email notifications for booking confirmations        |
| Browse and view treatments        | Blog page for sharing tips                           |
| Book and manage appointments      | Ability to add more therapists to the site           |

#### Kanban board

GitHub Projects was used as a project management tool with a Kanban board to track these user stories and monitor progress. **Story points** were assigned to these user stories, using the Fibonacci sequence (3, 5, 8) to represent the relative complexity and effort involved in each task:

**Start**
![User Stories Progress - Start](assets/readme_files/start.png)

**Week 1**
![User Stories Progress - Week 1](assets/readme_files/week1.png)

**Week 2**
![User Stories Progress - Week 2](assets/readme_files/week2.png)

**Week 3**
![User Stories Progress - Week 3](assets/readme_files/week3.png)


### Structure

#### Flowchart

The website is organized using a [Mermaid](https://mermaid.js.org/) Flowchart to illustrate the user journey and interactions, ensuring intuitive navigation and a seamless user experience. The chart outlines the interactions available to both logged-in and logged-out users, illustrating how they navigate through the site's features.

![Sports Therapy Booking website map](assets/readme_files/flowchart.png)

##### User Flow

###### Non-Logged-In Users:
* **Home Page**: an overview of the services offered, client testimonials, and quick links to book an appointment.
* **About Page**: detailed info about the therapist's credentials and philosophy. It also includes a contact form.
* **Treatments Page**: all available treatments with descriptions and pricing, along with a FAQ section.
* **Login Page**: allows users to log in to access personalized features like appointment management.
* **Book Appointment**: direct access to booking form; redirects users to log in before booking an appointment.

###### Logged-In Users:
* **Home Page**: same for non-logged-in users.
* **About Page**: same for non-logged-in users.
* **Treatments Page**: same for non-logged-in users.
* **My Appointments Page**: allows users to view, edit, or delete their scheduled appointments.
* **Logout**: allows users to log out of their account securely.
* **Book Appointment**: direct accesses to booking form; users can schedule their appointments.

#### Database Model

The database model was designed using [drawsql](https://drawsql.app/) and is managed with [PostgreSQL](https://www.postgresql.org/), a relational database.

![Sports Therapy Management database model](assets/readme_files/erdiagram.png)

##### Home App

###### ClientTestimonial Model

The `ClientTestimonial` model manages and displays client feedback on the website.

* **Client Name**: A `CharField` that stores the name of the client providing the testimonial.
* **Testimonial Text**: A `TextField` containing testimonials provided by users.
* **Active**: A `BooleanField` indicating whether the testimonial is currently active and displayed on the website. 
* **Date Added**: A `DateTimeField` of when the testimonial was added, allowing for tracking of feedback.

##### About App

###### About Model

The `About` model is designed to manage and present detailed information about the therapist.

* **Title**: A `CharField` that stores the title of the "About Me" section.
* **Content**: A `TextField` containing the main content of the "About Me" section.

###### ContactRequest Model

The `ContactRequest` model allows for efficient handling of client inquiries and communication.

* **Name**: A `CharField` storing the name of the individual making the contact request.
* **Email**: An `EmailField` capturing the email address of the requester.
* **Message**: A `TextField` containing the message or inquiry sent by the individual.
* **Read**: A `BooleanField` indicating whether the message has been read. Defaults to `False`.
* **Created On**: A `DateTimeField` that records when the contact request was created.

##### Treatments App

###### Treatment Model

Each treatment offered by the therapist is detailed in the `Treatment` model.

* **Name**: A `CharField` storing the name of the treatment.
* **Description**: A `TextField` providing a detailed description of the treatment.
* **Services Offered**: An optional `TextField` detailing the services provided as part of the treatment.
* **Benefits**: An optional `TextField` outlining the benefits of the treatment.
* **Price**: A `DecimalField` indicating the price of the treatment, up to two decimal places.
* **Image**: A `CloudinaryField` to store an optional image associated with the treatment.
* **Button Text**: A `CharField` providing default text for call-to-action buttons related for booking appointments.

**FAQ Model**

The `FAQ` model is used to manage frequently asked questions.

* **Question**: A `CharField` storing the frequently asked questions.
* **Answer**: A `TextField` containing the answer to the question.

##### Appointments App

###### Appointment Model

The `Appointment` model facilitates the scheduling & management of therapy sessions.

* **User**: A foreign key from the `User` model that stores the client who has booked the appointment.
* **Date**: The date of the appointment, stored as a `DateField`.
* **Time**: The time of the appointment, stored as a `TimeField`.
* **Treatment**: A `CharField` representing the type of treatment selected for the appointment.

### Skeleton

#### Wireframes

[Balsamiq](https://balsamiq.com/) was used to create a layout of the website in the planning phase. Here are my initial designs: 

Page | Desktop Version | Mobile Version
--- | --- | ---
Login | ![Desktop Login wireframe image](assets/wireframes/login.png) | ![Mobile Login wireframe image](assets/wireframes/login_mobile.png)
Sign Up | ![Desktop Sign Up wireframe image](assets/wireframes/signup.png) | ![Mobile Sign Up wireframe image](assets/wireframes/signup_mobile.png)
Home | ![Desktop Home wireframe image](assets/wireframes/index.png) | ![Mobile Home wireframe image](assets/wireframes/index_mobile.png)
Products | ![Desktop About wireframe image](assets/wireframes/products.png) | ![Mobile About wireframe image](assets/wireframes/home_mobile.png)
Product Detail | ![Desktop Treatments wireframe image](assets/wireframes/product_detail.png) | ![Mobile Treatments wireframe image](assets/wireframes/products_mobile.png)
Bag | ![Book Appointment wireframe image](assets/wireframes/bag.png) | ![Mobile Book Appointment wireframe image](assets/wireframes/bag_mobile.png)
Checkout | ![View Appointments wireframe image](assets/wireframes/checkout.png) | ![Mobile View Appointments wireframe image](assets/wireframes/checkout_mobile.png)
My profile | ![View Appointments wireframe image](assets/wireframes/profile.png) | ![Mobile View Appointments wireframe image](assets/wireframes/profile_mobile.png)
Admin Add Product | ![View Appointments wireframe image](assets/wireframes/add_product.png) | ![Mobile View Appointments wireframe image](assets/wireframes/add_product_mobile.png)



## User Experience (UX)

### Strategy

#### Project Goals

* Provide a user-friendly interface for clients to book sports therapy appointments.

* Implement a responsive design to ensure accessibility across various devices.

* Allow clients to manage their bookings easily through a personal dashboard.

* Ensure secure authentication and data handling.

#### User Stories

##### Viewing and Navigation

1. As a shopper, I want to view a list of sneakers so that I can choose the ones I’d like to purchase.

2. As a shopper, I want to see detailed info for each sneaker (price, description, available sizes) so that I can make informed purchasing decisions.

3. As a shopper, I want to be notified about special offers and discounts so that I can save money on my purchases.

4. As a shopper, I want to easily view the total cost of my selected items so that I can avoid spending more than I intend.

##### Registration and User Accounts

5. As a site user, I want to register for an account easily so that I can view my order history and profile information.
6. As a site user, I want to log in or log out quickly so that I can access my personal account when needed.
7. As a site user, I want to recover my password easily so that I can regain access to my account if I forget it.
8. As a site user, I want to receive an email confirmation after registering so that I can verify my registration was successful.
9. As a site user, I want to have a personalized user profile so that I can view my past orders and manage my account information.

##### Sorting and Searching

10. As a shopper, I want to sort sneakers by price, rating, or category so that I can find the best products that fit my preferences.
11. As a shopper, I want to sort sneakers by category (e.g., running shoes, casual shoes) so that I can easily find sneakers specific to my needs.
12. As a shopper, I want to search for sneakers by name or description so that I can quickly locate the product I’m interested in.
13. As a shopper, I want to filter products across multiple categories (e.g., men's running shoes, women’s casual shoes) to find products that suit my interests

##### Purchasing and Checkout

14. As a shopper, I want to easily select the size and quantity of the sneakers I’m purchasing so that I ensure I’m ordering the correct item.
15. As a shopper, I want to view the final cost, including taxes and shipping, so that I understand exactly what I will pay.
16. As a shopper, I want to complete my purchase quickly and securely so that my personal and payment information is protected.


# Agile Development Plan

## User Stories and Epics

### Epic 1: Viewing and Navigation
1. View a List of Sneakers (#1)
2. See Detailed Information for Sneakers (#2)
3. Quickly Identify Deals and Discounts (#3)
4. View the Total Cost of Selected Items (#4)

### Epic 2: Registration and User Accounts
5. Register for an Account (#5)
6. Log In or Log Out of My Account (#6)
7. Recover My Password (#7)
8. Receive an Email Confirmation After Registering (#8)
9. Have a Personalized User Profile (#9)

### Epic 3: Sorting and Searching
10. Sort Sneakers by Price, Rating, or Category (#10)
11. Sort Sneakers by Category (#11)
12. Search for Sneakers by Name or Description (#12)
13. Filter Products Across Multiple Categories (#13)

### Epic 4: Purchasing and Checkout
14. Select Size and Quantity of Sneakers (#14)
15. View Final Cost Including Taxes and Shipping (#15)
16. Complete My Purchase Securely (#16)

### Epic 5: Marketing and Customer Engagement
17. Newsletter Signup (#17)
18. Client Testimonial Management (#21)
19. FAQ Management (#22)
20. Contact Form (#23)

### Epic 6: Admin and Store Management
21. Add Product (#18)
22. Edit/Update Product (#19)
23. Delete Product (#20)

## MoSCoW Prioritization

### Must Have
- View a List of Sneakers (#1)
- See Detailed Information for Sneakers (#2)
- Register for an Account (#5)
- Log In or Log Out of My Account (#6)
- Select Size and Quantity of Sneakers (#14)
- Complete My Purchase Securely (#16)
- Add Product (#18)
- Edit/Update Product (#19)
- Delete Product (#20)

### Should Have
- View the Total Cost of Selected Items (#4)
- Recover My Password (#7)
- Receive an Email Confirmation After Registering (#8)
- Have a Personalized User Profile (#9)
- Search for Sneakers by Name or Description (#12)
- View Final Cost Including Taxes and Shipping (#15)

### Could Have
- Quickly Identify Deals and Discounts (#3)
- Sort Sneakers by Price, Rating, or Category (#10)
- Sort Sneakers by Category (#11)
- Filter Products Across Multiple Categories (#13)
- Newsletter Signup (#17)
- Client Testimonial Management (#21)
- FAQ Management (#22)
- Contact Form (#23)

### Won't Have (this iteration)
- Customer loyalty program
- Advanced analytics dashboard for store owners

## Sprint Planning

### Sprint 1: Basic Product Viewing and User Authentication
Duration: 2 weeks
User Stories: #1, #2, #5, #6
Milestone: Basic product catalog and user account functionality

### Sprint 2: Product Management and User Profiles
Duration: 2 weeks
User Stories: #18, #19, #20, #7, #8, #9
Milestone: Admin product management and enhanced user account features

### Sprint 3: Shopping Bag and Checkout Process - Part 1
Duration: 2 weeks
User Stories: #4, #14, #15
Milestone: Functional shopping bag and initial checkout process

### Sprint 4: Checkout Process - Part 2
Duration: 2 weeks
User Stories: #16
Milestone: Secure checkout process completion

### Sprint 5: Sorting, Searching, and Additional Features
Duration: 2 weeks
User Stories: #10, #11, #12, #13, #3
Milestone: Implemented search, sorting, and special offers features

### Sprint 6: Marketing Features and Final Polishing
Duration: 2 weeks
User Stories: #17, #21, #22, #23
Tasks: Implement marketing features, bug fixes, performance optimization, and final testing

## Implementation Process

Progress, challenges faced, and solutions implemented to demonstrate agile methodology application.


# Final Comprehensive Django Sports Sole User Flow Chart

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


