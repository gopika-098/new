# Generated by Django 5.0.1 on 2024-03-27 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_anchor_registration_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anchor_registration',
            name='experience',
        ),
        migrations.AddField(
            model_name='anchor_registration',
            name='pro_pic',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
