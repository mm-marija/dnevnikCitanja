# Generated by Django 3.1.7 on 2022-02-23 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookwormApp', '0008_auto_20220223_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profilePic',
            field=models.ImageField(default='https://www.delfi.rs/_img/artikli/2014/02/saptac_vv.jpg', upload_to='https://www.delfi.rs/_img/artikli/2014/02/saptac_vv.jpg'),
        ),
    ]
