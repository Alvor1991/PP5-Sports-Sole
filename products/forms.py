from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    Form for adding and updating product information,
    excluding the 'sizes' field and using custom widgets for image fields.
    """
    class Meta:
        model = Product
        # Exclude the sizes field from the form
        exclude = ['sizes']

    image = forms.ImageField(
        label='Product Image',
        required=False,
        widget=CustomClearableFileInput
    )

    detail_image = forms.ImageField(
        label='Product Detail Image',
        required=False,
        widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
