# Generated by Django 5.0.1 on 2024-05-19 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_rename_name_booking_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('PHONE', models.CharField(max_length=50)),
                ('ADDRESS', models.CharField(max_length=50)),
                ('EMAIL', models.CharField(max_length=50)),
                ('DATE', models.CharField(max_length=10)),
                ('ANCHOR', models.CharField(max_length=50)),
                ('ACTION', models.CharField(max_length=50)),
                ('payment', models.CharField(max_length=50)),
            ],
        ),
    ]
