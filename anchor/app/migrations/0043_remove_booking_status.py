# Generated by Django 5.0.1 on 2024-05-28 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_booking_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='status',
        ),
    ]
