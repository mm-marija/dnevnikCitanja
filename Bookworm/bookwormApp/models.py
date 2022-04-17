from django.db import models
from django.contrib.auth.models import AbstractUser


MESECI = (("Januar", "JANUAR"), ("Februar", "FEBRUAR"), ("Mart", "MART"), ("April", "APRIL"), ("Maj", "MAJ"), ("Jun", "JUN"),
    ("Jul", "JUL"), ("Avgust", "AVGUST"), ("Septembar", "SEPTEMABR"), ("Oktobar", "OKTOBAR"), ("Novembar", "NOVEMBAR"),
    ("Decembar", "DECEMBAR"))


OCENE = ((1, 1), (1.5, 2), (2, 3), (2.5, 4), (3, 5), (3.5, 6), (4, 7), (4.5, 8), (5, 9))

class CustomUser(AbstractUser):
    pass
    firstName = models.CharField(max_length=200, default="")
    lastName = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.username

class Zanr(models.Model):
    naziv = models.CharField(max_length=200)
    icon = models.ImageField(blank=True,max_length=800)

    def __str__(self):
        return self.naziv


class Knjiga(models.Model):
    naslov = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    zanr = models.ManyToManyField(Zanr)
    mesec = models.CharField(max_length=12, choices=MESECI, null=True, blank=True)
    ocena = models.DecimalField(blank=True, choices=OCENE, null = True, max_digits=30, decimal_places=1)
    procitano = models.BooleanField(default=False)
    kupljeno = models.BooleanField(default=False)
    korisnik = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.naslov + self.autor

class Citat(models.Model):
    nazivKnjige = models.ForeignKey(Knjiga, on_delete=models.CASCADE, null=True, blank=True)
    tekst = models.CharField(max_length=600)
    def __str__(self):
        return self.tekst
