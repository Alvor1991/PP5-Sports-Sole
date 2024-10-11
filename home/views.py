from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterSignupForm

def index(request):
    """ A view to return the index page """
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for subscribing to our newsletter!')
            return redirect('home')
    else:
        form = NewsletterSignupForm()
    
    context = {
        'form': form,
    }
    return render(request, 'home/index.html', context)

def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for subscribing to our newsletter!')
            return redirect('home')
    else:
        form = NewsletterSignupForm()
    return render(request, 'home/newsletter_signup.html', {'form': form})