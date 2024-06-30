from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views
from Homepage import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Referenssit', views.Referenssit, name='Referenssit'),
    path('Hallityomaaview', views.Hallityomaaview, name='Hallityomaaview'),
    path('Rengashalliview', views.Rengashalliview, name='Rengashalliview'),
    path('Rivitaloremonttiview', views.Rivitaloremonttiview, name='Rivitaloremonttiview'),
    path('Rivitalonsahkourakointiview', views.Rivitalonsahkourakointiview, name='Rivitalonsahkourakointiview'),
    path('Lumiesteidenasennusview', views.Lumiesteidenasennusview, name='Lumiesteidenasennusview'),
    path('ReferenssitEnglish', views.ReferenssitEnglish, name='ReferenssitEnglish'),
    path('Yhteydenotto', views.Yhteydenotto, name='Yhteydenotto'),
    path('YhteydenottoEnglish', views.YhteydenottoEnglish, name='YhteydenottoEnglish'),
    path('Sendcontactform', views.Sendcontactform, name='Sendcontactform'),
    path('HomePosted', views.HomePosted, name='HomePosted'),
    path('Tietoa', views.Tietoa, name='Tietoa'),
    path('TietoaEnglish', views.TietoaEnglish, name='TietoaEnglish'),
    path('English', views.English, name='English'),
    path('sitemap', views.sitemap, name='sitemap'),
    path('Cookies', views.Cookies, name='Cookies'),
    path('Yleisesti', views.Yleisesti, name='Yleisesti'),
    path('Ajankohtaista', views.Ajankohtaista, name='Ajankohtaista'),
    path('Tyopaikat', views.Tyopaikat, name='Tyopaikat'),
    path('Uudisrakentaminenview', views.Uudisrakentaminenview, name='Uudisrakentaminenview'),
    path('Hietaniemenkadultaview', views.Hietaniemenkadultaview, name='Hietaniemenkadultaview'),
    path('Sahkopalvelut', views.Sahkopalvelut, name='Sahkopalvelut'),
    path('sahkotyot_vantaa', views.sahkotyot_vantaa, name='sahkotyot_vantaa'),
    path('Emannantieview', views.Emannantieview, name='Emannantieview'),
    path('Jyskview', views.Jyskview, name='Jyskview'),
    path('SoukkaSaunaview', views.SoukkaSaunaview, name='SoukkaSaunaview'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
