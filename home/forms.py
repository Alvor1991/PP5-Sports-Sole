from django import forms
from .models import NewsletterSubscriber


class NewsletterSignupForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your email'
                }
            )
        }


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }
        )
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Message'
            }
        ),
        required=True
    )
