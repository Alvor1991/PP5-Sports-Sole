# Generated by Django 5.1 on 2024-09-20 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(blank=True, choices=[('Men', 'Men'), ('Women', 'Women')], max_length=6, null=True),
        ),
    ]
