# Generated by Django 5.0.1 on 2024-05-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_rename_pro_pic_anchor_registration_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='DATE',
            field=models.CharField(max_length=10),
        ),
    ]
