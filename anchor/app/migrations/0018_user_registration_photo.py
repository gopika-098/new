# Generated by Django 5.0.1 on 2024-04-03 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_log_in_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='photo',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
