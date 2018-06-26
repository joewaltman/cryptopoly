# Generated by Django 2.0.6 on 2018-06-17 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoursquareVenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('venue_id', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=20)),
                ('address', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]