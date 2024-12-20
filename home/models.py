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
    )
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating} stars"


class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    category = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question


class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Message from {self.name} ({self.email}) "
            f"on {self.date_submitted}"
        )
