# Generated by Django 4.1.1 on 2022-10-13 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vintage_app', '0002_remove_order_meal_customer_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='count',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
