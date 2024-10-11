from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    signup_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

class CustomerTestimonial(models.Model):
    name = models.CharField(max_length=100)
    testimonial = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating from 1 to 5"
    )
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating} stars"
