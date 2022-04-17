from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from bookwormApp.models import CustomUser, Knjiga, Zanr, Citat
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from .forms import CustomUserCreationForm
import json
from django.core import serializers
from collections import Counter
import numpy as np




class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def procitaneKnjige(request):
    if request.user.is_authenticated:
        knjige = Knjiga.objects.all()
        knjige = knjige.filter(korisnik=request.user)
        context = {"knjige": knjige}
        return render(request, 'knjige/procitaneKnjige.html', context)
    else:
        return HttpResponseRedirect(reverse('home'))

def listaZaCitanje(request):
    if request.user.is_authenticated:
        knjige = Knjiga.objects.all()
        knjige = knjige.filter(korisnik=request.user)
        context = {"knjige": knjige}
        return render(request, 'knjige/listaZaCitanje.html', context)
    else:
        return HttpResponseRedirect(reverse('home'))

def listaZelja(request):
    if request.user.is_authenticated:
        knjige = Knjiga.objects.all()
        knjige = knjige.filter(korisnik=request.user)
        context = {"knjige": knjige}
        return render(request, 'knjige/listaZelja.html', context)
    else:
        return HttpResponseRedirect(reverse('home'))


def obrisiKnjigu(request, id):
	knjiga = get_object_or_404(Knjiga, pk=id)
	knjiga.delete()
	return HttpResponseRedirect(reverse('procitaneKnjige'))

def dodajKnjigu(request):
    if request.method == 'POST':
        zanrK = request.POST.getlist('zanr')
        ocenaK = request.POST['ocena']
        ocenaK = float(ocenaK)
        knjiga = Knjiga(
            mesec = request.POST['mesec'],
            naslov = request.POST['naslov'],
            autor = request.POST['autor'],
            ocena = ocenaK,
            korisnik = request.user,
            procitano = True
        )
        knjiga.save()
        for z in zanrK:
            knjiga.zanr.add(z)
        knjiga.save()
        return HttpResponseRedirect(reverse('procitaneKnjige'))
    else:
        zanrovi = Zanr.objects.all()
        context = {"zanrovi": zanrovi}
        return render(request, 'knjige/dodajKnjigu.html', context)


def izmeniKnjigu(request, id):
    if request.method == 'POST':
        knjiga = get_object_or_404(Knjiga,pk=id)
        ocenaK = request.POST['ocena']
        ocenaK = float(ocenaK)
        knjiga.naslov = request.POST['naslov']
        knjiga.autor = request.POST['autor']
        obrZanr = request.POST.getlist('obrZanr')
        zanrK = request.POST.getlist('zanr')
        for z in zanrK:
            knjiga.zanr.add(z)
        knjiga.mesec = request.POST['mesec']
        knjiga.ocena = ocenaK
        for obr in obrZanr:
            knjiga.zanr.remove(obr)
        knjiga.save()
        return HttpResponseRedirect(reverse('procitaneKnjige'))
    else:
        zanrovi = Zanr.objects.all()
        knjiga = get_object_or_404(Knjiga, pk=id)
        context = {"knjiga": knjiga, "zanrovi": zanrovi}
        return render(request, 'knjige/izmeniKnjigu.html', context)


def dodajCitat(request,id):
    knjiga = get_object_or_404(Knjiga,pk=id)
    if request.method == 'POST':
        citat = Citat(
            nazivKnjige = knjiga,
            tekst = request.POST['tekst']
        )
        citat.save()
        return HttpResponseRedirect(reverse('procitaneKnjige'))
    else:
        context = {"knjiga": knjiga}
        return render(request, 'knjige/dodajCitat.html', context)


def vidiCitate(request, id):
    if request.user.is_authenticated:
        knjiga = get_object_or_404(Knjiga, pk=id)
        citati = Citat.objects.all()
        citati = citati.filter(nazivKnjige=knjiga)
        context = {"citati": citati, "knjiga": knjiga}
        return render(request, 'knjige/vidiCitate.html', context)
    else:
        return HttpResponseRedirect(reverse('procitaneKnjige'))


def obrisiCitat(request, id):
	citat = get_object_or_404(Citat, pk=id)
	citat.delete()
	return HttpResponseRedirect(reverse('procitaneKnjige'))

def dodajZaCitanje(request):
    if request.method == 'POST':
        zanrK = request.POST.getlist('zanr')
        knjiga = Knjiga(
            naslov = request.POST['naslov'],
            autor = request.POST['autor'],
            korisnik = request.user
        )
        knjiga.kupljeno = True
        knjiga.save()
        for z in zanrK:
            knjiga.zanr.add(z)
        knjiga.save()
        return HttpResponseRedirect(reverse('listaZaCitanje'))
    else:
        zanrovi = Zanr.objects.all()
        context = {"zanrovi": zanrovi}
        return render(request, 'knjige/dodajKnjiguZaCitanje.html', context)

def dodajZelju(request):
    if request.method == 'POST':
        zanrK = request.POST.getlist('zanr')
        knjiga = Knjiga(
            naslov = request.POST['naslov'],
            autor = request.POST['autor'],
            korisnik = request.user
        )
        knjiga.save()
        for z in zanrK:
            knjiga.zanr.add(z)
        knjiga.save()
        return HttpResponseRedirect(reverse('listaZelja'))
    else:
        zanrovi = Zanr.objects.all()
        context = {"zanrovi": zanrovi}
        return render(request, 'knjige/dodajZaZelju.html', context)

def procitanaKnjiga(request, id):
    if request.method == 'POST':
        ocenaK = request.POST['ocena']
        ocenaK = float(ocenaK)
        knjiga = get_object_or_404(Knjiga,pk=id)
        knjiga.procitano = True
        knjiga.ocena = ocenaK
        knjiga.mesec = request.POST['mesec']
        knjiga.save()
        return HttpResponseRedirect(reverse('procitaneKnjige'))
    else:
        zanrovi = Zanr.objects.all()
        knjiga = get_object_or_404(Knjiga, pk=id)
        context = {"knjiga": knjiga, "zanrovi": zanrovi}
        return render(request, 'knjige/procitanaKnjiga.html', context)

def kupljenaKnjiga(request, id):
    knjiga = get_object_or_404(Knjiga, pk=id)
    knjiga.kupljeno = True
    knjiga.save()
    return HttpResponseRedirect(reverse('listaZaCitanje'))


def poMesecima(request):
    knjige = Knjiga.objects.all()
    knjige = knjige.filter(korisnik=request.user)
    labels = []
    meseci = []
    data = []
    for k in knjige:
        if k.mesec != None:
            meseci.append(k.mesec)
    c = Counter(meseci)
    for i in c.values():
        data.append(i)
    for j in c:
        labels.append(j)
    context = {"knjige": knjige, "labels": labels, "data": data}
    return render(request, 'knjige/poMesecima.html', context)

def poZanrovima(request):
    knjige = Knjiga.objects.all()
    knjige = knjige.filter(korisnik=request.user)
    labels = []
    zanrovi = []
    data = []
    for k in knjige:
        if k.zanr != None and k.procitano == True:
            for z in k.zanr.all():
                zanrovi.append(z.naziv)
    c = Counter(zanrovi)
    for i in c.values():
        data.append(i)
    for j in c:
        labels.append(j)
    context = {"knjige": knjige, "labels": labels, "data": data}
    return render(request, 'knjige/poZanrovima.html', context)
