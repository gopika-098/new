# Generated by Django 5.0.1 on 2024-03-05 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_anchor_registration_previous_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='afeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wname', models.CharField(max_length=55)),
                ('bname', models.CharField(max_length=555)),
                ('feed', models.CharField(max_length=55)),
            ],
        ),
    ]
