from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    Represents a product category.
    """
    
    class Meta:
        verbose_name_plural = 'Categories'
   
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """
        Returns the internal name of the category.
        """
        return self.name

    def get_friendly_name(self):
        """
        Returns the user-friendly name of the category.
        """
        return self.friendly_name


class Size(models.Model):
    """
    Represents a size for a product.
    """
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size


class Product(models.Model):
    """
    Represents a product in the store.
    """
    GENDER_CHOICES = [
        ('Men', 'Men'),
        ('Women', 'Women'),
    ]

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    detail_image = models.ImageField(upload_to='products/', null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    sizes = models.ManyToManyField(Size, related_name='products')

    def __str__(self):
        """
        Returns the name of the product.
        """
        return self.name
