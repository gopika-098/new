# Generated by Django 5.0.1 on 2024-05-30 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_remove_booking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='amount',
            field=models.IntegerField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
