# Generated by Django 3.1.7 on 2022-03-01 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookwormApp', '0021_auto_20220301_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zanr',
            name='slikaZanr',
        ),
    ]
