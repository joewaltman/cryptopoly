# Generated by Django 2.0.6 on 2018-06-17 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20180618_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='foursquarevenue',
            name='visited',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
