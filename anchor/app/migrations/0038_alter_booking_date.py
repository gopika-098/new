# Generated by Django 5.0.1 on 2024-05-27 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_delete_afeed_rename_bname_ufeed_anchorname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='DATE',
            field=models.DateField(),
        ),
    ]
