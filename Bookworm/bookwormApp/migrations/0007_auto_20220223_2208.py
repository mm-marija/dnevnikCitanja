# Generated by Django 3.1.7 on 2022-02-23 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookwormApp', '0006_customuser_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profilePic',
            field=models.ImageField(default='', upload_to='https://www.delfi.rs/_img/artikli/2014/02/saptac_vv.jpg'),
        ),
    ]
