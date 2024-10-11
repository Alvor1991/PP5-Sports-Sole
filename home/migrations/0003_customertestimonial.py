# Generated by Django 5.1 on 2024-10-11 12:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_newslettersubscriber_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerTestimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('testimonial', models.TextField()),
                ('rating', models.IntegerField(help_text='Rating from 1 to 5', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
