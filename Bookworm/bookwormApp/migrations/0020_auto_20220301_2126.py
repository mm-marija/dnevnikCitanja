# Generated by Django 3.1.7 on 2022-03-01 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookwormApp', '0019_zanr_slikazanr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zanr',
            name='slikaZanr',
            field=models.ImageField(blank=True, height_field=80, upload_to='', width_field=80),
        ),
    ]