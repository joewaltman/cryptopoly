# Generated by Django 2.0.6 on 2018-06-17 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_foursquarevenue_visited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foursquarevenue',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foursquarevenue',
            name='visited',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
