from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import NewsletterSignupForm, ContactForm
from .models import CustomerTestimonial, FAQ
from products.models import Product

def index(request):
    """ A view to return the index page with newsletter signup and contact forms """
    testimonials = CustomerTestimonial.objects.all().order_by('-date')[:3]
    faqs = FAQ.objects.all().order_by('order')[:5]
    new_arrivals = Product.objects.filter(tags__name__in=["arrivals"])[:4]

    contact_success = False  # Track success for the contact form
    signup_success = False   # Track success for the newsletter form

    # Handle newsletter signup form
    if request.method == 'POST' and 'newsletter_signup' in request.POST:
        newsletter_form = NewsletterSignupForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            signup_success = True  # Trigger Bootstrap success message for newsletter signup
    else:
        newsletter_form = NewsletterSignupForm()

    # Handle contact form submission
    if request.method == 'POST' and 'contact_form' in request.POST:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # Get form data
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            
            # Send the email using Django's send_mail function
            send_mail(
                subject=f"Contact Form Submission from {name}",
                message=message,
                from_email=email,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
            )
            contact_form = ContactForm()  # Reset the form after successful submission
            contact_success = True  # Trigger Bootstrap success message for contact form
    else:
        contact_form = ContactForm()

    context = {
        'newsletter_form': newsletter_form,
        'contact_form': contact_form,
        'testimonials': testimonials,
        'faqs': faqs,
        'new_arrivals': new_arrivals,
        'signup_success': signup_success,  # For Bootstrap success message
        'contact_success': contact_success,  # For Bootstrap success message
    }

    return render(request, 'home/index.html', context)

