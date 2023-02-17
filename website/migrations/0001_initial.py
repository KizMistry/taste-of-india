# Generated by Django 3.2.18 on 2023-02-17 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('booking_time', models.DateTimeField()),
                ('number_of_guests', models.IntegerField(choices=[(2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), ('More', '8+')], default=2)),
            ],
            options={
                'ordering': ['-booking_time'],
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('fname', models.CharField(max_length=15)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('approved', models.BooleanField(default=0)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]