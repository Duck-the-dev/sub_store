# Generated by Django 4.0.3 on 2022-05-23 13:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_delete_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='address2',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='', max_length=254, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(blank=True, choices=[('Giza', 'Giza'), ('Cairo', 'Cairo')], default='Giza', max_length=10, null=True),
        ),
    ]
