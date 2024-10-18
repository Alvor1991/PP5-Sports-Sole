from django.contrib import admin
from .models import Product, Category, Size
from taggit.managers import TaggableManager


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
    filter_horizontal = ('sizes',)
    fields = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'detail_image',
        'tags',
        'sizes'
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SizeAdmin(admin.ModelAdmin):
    list_display = (
        'size',
    )


# Register models
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
