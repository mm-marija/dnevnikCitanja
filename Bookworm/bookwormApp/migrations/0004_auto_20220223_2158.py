# Generated by Django 3.1.7 on 2022-02-23 20:58

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bookwormApp', '0003_auto_20220223_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='name',
            new_name='firstName',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='firstName'),
        ),
    ]
