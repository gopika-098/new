# Generated by Django 5.0.1 on 2024-03-04 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_ufeed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anchor_registration',
            name='previous_work',
            field=models.FileField(upload_to=''),
        ),
    ]
