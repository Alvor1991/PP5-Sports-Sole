from django.shortcuts import render, redirect
from .forms import NewsletterSignupForm
from .models import CustomerTestimonial

def index(request):
    """ A view to return the index page """
    # Get the 3 most recent testimonials
    testimonials = CustomerTestimonial.objects.all().order_by('-date')[:3]

    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/index.html', {'form': form, 'testimonials': testimonials, 'signup_success': True})
    else:
        form = NewsletterSignupForm()
    
    context = {
        'form': form,
        'testimonials': testimonials,
    }
    return render(request, 'home/index.html', context)

def newsletter_signup(request):
    """ Separate view to handle newsletter signup """
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/newsletter_signup.html', {'form': form, 'signup_success': True})
    else:
        form = NewsletterSignupForm()
    return render(request, 'home/newsletter_signup.html', {'form': form})
