# Generated by Django 3.1.7 on 2022-03-01 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookwormApp', '0020_auto_20220301_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zanr',
            name='slikaZanr',
            field=models.ImageField(blank=True, max_length=600, upload_to=''),
        ),
    ]
