# Generated by Django 5.0.1 on 2024-02-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anchor_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.IntegerField()),
                ('license_no', models.CharField(max_length=10)),
                ('experience', models.IntegerField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='employee_registration',
        ),
        migrations.AddField(
            model_name='user_registration',
            name='address',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
