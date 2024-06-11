# Generated by Django 5.0.1 on 2024-03-24 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_passwordreset'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anchor_registration',
            old_name='type_of_anchor',
            new_name='account_number',
        ),
        migrations.RenameField(
            model_name='anchor_registration',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='anchor_registration',
            name='biodata',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anchor_registration',
            name='last_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PasswordReset',
        ),
    ]
