# Generated by Django 4.0.3 on 2022-05-20 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_order_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='colors',
            field=models.CharField(blank=True, choices=[('yellow', 'yellow'), ('BABYBLUE', 'BABYBLUE'), ('GREEN', 'GREEN')], default='GREEN', max_length=10, null=True),
        ),
    ]
