from django.shortcuts import render
from .forms import NewsletterSignupForm, ContactForm
from .models import CustomerTestimonial, FAQ, ContactSubmission
from products.models import Product


def index(request):
    """ Return the index page with newsletter signup and contact forms """
    testimonials = CustomerTestimonial.objects.all().order_by('-date')[:3]
    faqs = FAQ.objects.all().order_by('order')[:5]
    new_arrivals = Product.objects.filter(tags__name__in=["arrivals"])[:4]

    contact_success = False
    signup_success = False

    # Handle newsletter signup form
    if request.method == 'POST' and 'newsletter_signup' in request.POST:
        newsletter_form = NewsletterSignupForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()  # Save to database
            signup_success = True
            newsletter_form = NewsletterSignupForm()
        else:
            print("Newsletter form errors:", newsletter_form.errors)
    else:
        newsletter_form = NewsletterSignupForm()

    # Handle contact form submission (this is working fine)
    if request.method == 'POST' and 'contact_form' in request.POST:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            ContactSubmission.objects.create(
                name=contact_form.cleaned_data['name'],
                email=contact_form.cleaned_data['email'],
                message=contact_form.cleaned_data['message']
            )
            contact_success = True
            contact_form = ContactForm()
    else:
        contact_form = ContactForm()

    context = {
        'newsletter_form': newsletter_form,
        'contact_form': contact_form,
        'testimonials': testimonials,
        'faqs': faqs,
        'new_arrivals': new_arrivals,
        'signup_success': signup_success,
        'contact_success': contact_success,
    }

    return render(request, 'home/index.html', context)
