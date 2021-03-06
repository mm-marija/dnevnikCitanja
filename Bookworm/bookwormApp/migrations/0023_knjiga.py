# Generated by Django 3.1.7 on 2022-03-01 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookwormApp', '0022_remove_zanr_slikazanr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Knjiga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naslov', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=200)),
                ('mesec', models.CharField(choices=[('Januar', 'JANUAR'), ('Februar', 'FEBRUAR'), ('Mart', 'MART'), ('April', 'APRIL'), ('Maj', 'MAJ'), ('Jun', 'JUN'), ('Jul', 'JUL'), ('Avgust', 'AVGUST'), ('Septembar', 'SEPTEMABR'), ('Oktobar', 'OKTOBAR'), ('Novembar', 'NOVEMBAR'), ('Decembar', 'DECEMBAR')], default='Januar', max_length=12)),
                ('ocena', models.IntegerField(blank=True, choices=[(1, 1.5), (2, 2.5), (3, 3.5), (4, 4.5), (5, 5.0)], default=1)),
                ('korisnik', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('zanr', models.ManyToManyField(to='bookwormApp.Zanr')),
            ],
        ),
    ]
