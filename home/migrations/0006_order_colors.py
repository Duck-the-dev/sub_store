# Generated by Django 4.0.3 on 2022-05-20 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='colors',
            field=models.CharField(blank=True, choices=[('yellow', 'yellow'), ('BABYBLUE', 'BABYBLUE'), ('GREEN', 'GREEN')], max_length=10, null=True),
        ),
    ]
