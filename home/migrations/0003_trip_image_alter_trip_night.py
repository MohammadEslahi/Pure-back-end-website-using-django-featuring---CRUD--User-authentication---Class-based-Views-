# Generated by Django 5.0.2 on 2024-03-28 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_trip_night'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trip',
            name='night',
            field=models.IntegerField(),
        ),
    ]