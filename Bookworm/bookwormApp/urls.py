from django.urls import path
from .views import SignUpView
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('procitano', views.procitaneKnjige, name='procitaneKnjige'),
    path('obrisi/<int:id>', views.obrisiKnjigu, name="obrisiKnjigu"),
    path('dodaj_knjigu', views.dodajKnjigu, name="dodajKnjigu"),
    path('izmeni_knjigu/<int:id>', views.izmeniKnjigu, name="izmeniKnjigu"),
    path('dodaj_citat/<int:id>', views.dodajCitat, name="dodajCitat"),
    path('vidiCitate/<int:id>', views.vidiCitate, name="vidiCitate"),
    path('obrisiCitat/<int:id>', views.obrisiCitat, name="obrisiCitat"),
    path('dodaj_za_citanje', views.dodajZaCitanje, name="dodajZaCitanje"),
    path('lista_za_citanje', views.listaZaCitanje, name="listaZaCitanje"),
    path('procitanaKnjiga/<int:id>', views.procitanaKnjiga, name="procitanaKnjiga"),
    path('lista_zelja', views.listaZelja, name="listaZelja"),
    path('dodaj_za_zelju', views.dodajZelju, name="dodajZelju"),
    path('kupljena_knjiga/<int:id>', views.kupljenaKnjiga, name="kupljenaKnjiga"),
    path('po_mesecima', views.poMesecima, name="poMesecima"),
    path('po_zanrovima', views.poZanrovima, name="poZanrovima"),
]
