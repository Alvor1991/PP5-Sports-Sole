from django.contrib import admin
from .models import NewsletterSubscriber, CustomerTestimonial

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'signup_date', 'is_active')
    list_filter = ('is_active', 'signup_date')
    search_fields = ('email',)
    date_hierarchy = 'signup_date'

@admin.register(CustomerTestimonial)
class CustomerTestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'date')
    list_filter = ('rating', 'date')
    search_fields = ('name', 'testimonial')
    date_hierarchy = 'date'