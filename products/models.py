from django.db import models


class Category(models.Model):
    """
    Represents a product category.
    """
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


class Product(models.Model):
    """
    Represents a product in the store.
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """
        Returns the name of the product.
        """
        return self.name
