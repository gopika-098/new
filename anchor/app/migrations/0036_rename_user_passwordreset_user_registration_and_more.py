# Generated by Django 5.0.1 on 2024-05-23 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_remove_anchor_registration_photo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passwordreset',
            old_name='user',
            new_name='user_registration',
        ),
        migrations.RemoveField(
            model_name='anchor_registration',
            name='account_number',
        ),
        migrations.RemoveField(
            model_name='anchor_registration',
            name='video',
        ),
    ]
