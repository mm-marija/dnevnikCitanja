# Generated by Django 3.1.7 on 2022-03-05 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookwormApp', '0031_auto_20220305_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knjiga',
            name='mesec',
            field=models.CharField(blank=True, choices=[('Januar', 'JANUAR'), ('Februar', 'FEBRUAR'), ('Mart', 'MART'), ('April', 'APRIL'), ('Maj', 'MAJ'), ('Jun', 'JUN'), ('Jul', 'JUL'), ('Avgust', 'AVGUST'), ('Septembar', 'SEPTEMABR'), ('Oktobar', 'OKTOBAR'), ('Novembar', 'NOVEMBAR'), ('Decembar', 'DECEMBAR')], max_length=12),
        ),
        migrations.AlterField(
            model_name='knjiga',
            name='ocena',
            field=models.IntegerField(blank=True, choices=[(1, 1), (1.5, 2), (2, 3), (2.5, 4), (3, 5), (3.5, 6), (4, 7), (4.5, 8), (5, 9)]),
        ),
    ]