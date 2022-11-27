# Generated by Django 4.1.3 on 2022-11-26 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotelBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('hotel_location', models.CharField(max_length=100)),
                ('hotel_owner', models.CharField(max_length=100)),
                ('hotel_restriction', models.BooleanField(default=False)),
                ('is_available', models.BooleanField(default=False)),
                ('charge', models.IntegerField(blank=True)),
                ('duration', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
