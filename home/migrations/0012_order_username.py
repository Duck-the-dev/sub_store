# Generated by Django 4.0.3 on 2022-05-29 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_order_address_order_address2_order_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.CharField(default='', max_length=120),
        ),
    ]
