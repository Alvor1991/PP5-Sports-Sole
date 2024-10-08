from django.contrib import admin
from .models import Product, Category, Size


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'detail_image',
    )
    ordering = ('sku',)
    filter_horizontal = ('sizes',)  # This allows you to select sizes for products in a more user-friendly manner


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SizeAdmin(admin.ModelAdmin):
    list_display = (
        'size',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)  # Register Size in the admin

