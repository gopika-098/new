# Generated by Django 5.0.1 on 2024-04-03 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_anchor_registration_about_your_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=50)),
                ('PHONE', models.CharField(max_length=50)),
                ('ADDRESS', models.CharField(max_length=50)),
                ('EMAIL', models.CharField(max_length=50)),
                ('DATE', models.IntegerField(max_length=10)),
                ('ANCHOR', models.CharField(max_length=50)),
            ],
        ),
    ]
