from django.contrib import admin
from .models import NewsletterSubscriber, CustomerTestimonial, FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'order')
    list_filter = ('category',)
    search_fields = ('question', 'answer')
    ordering = ('order',)

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