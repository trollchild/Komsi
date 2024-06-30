from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from .forms import ContactForm
from .models import referencemedia, HalliTyomaa, Rengashalli, Ravitalonsahko, Rivitaloremontti, Lumiesteidenasennus, Uudisrakentaminen, Hietaniemenkadulta, Item


def HomePosted(request):
    HomePosted = "HomePosted"
    Etusivu = "Etusivu"
    context = {'Etusivu':Etusivu, 'HomePosted':HomePosted,}
    return render(request, 'Index.html', context)

def Home(request):

    Etusivu = "Etusivu"
    context = {'Etusivu':Etusivu, }
    return render(request, 'Index.html', context)

def English(request):
    Etusivu = "Etusivu"
    English = "English"
    context = {'Etusivu':Etusivu, 'English':English}
    return render(request, 'Index.html', context)

def Referenssit(request):

    Gallery = referencemedia.objects.all()
    Referenssit = "Referenssit"
    context = {'Referenssit':Referenssit,'Gallery':Gallery,}
    return render(request, 'Referenssit.html', context)

def Ajankohtaista(request):
    Ajankohtaista = "Ajankohtaista"
    Gallery = referencemedia.objects.all()
    Referenssit = "Referenssit"
    context = {'Gallery':Gallery,'Ajankohtaista':Ajankohtaista,}
    return render(request, 'Ajankohtaisia_asioita.html', context)

def Yleisesti(request):
    yleisesti = "yleisesti"
    Gallery = referencemedia.objects.all()
    Referenssit = "Referenssit"
    context = {'Referenssit':Referenssit,'Gallery':Gallery,'yleisesti':yleisesti,}
    return render(request, 'Kuvia.html', context)

def Hallityomaaview(request):
    Hallityomaaview = "Hallityomaaview"
    Gallery = HalliTyomaa.objects.all()

    Referenssit = "Referenssit"
    context = {'Referenssit':Referenssit,'Gallery':Gallery,'Hallityomaaview':Hallityomaaview,}
    return render(request, 'Kuvia.html', context)

def Rengashalliview(request):
    #Myymäläremontti
    Rengashalliview = "Rengashalliview"
    Gallery = Rengashalli.objects.all()

    Referenssit = "Referenssit"
    context = {'Referenssit':Referenssit,'Gallery':Gallery,'Rengashalliview':Rengashalliview,}
    return render(request, 'Kuvia.html', context)

def Rivitaloremonttiview(request):
    Rivitaloremonttiview = "Rivitaloremonttiview"
    Gallery = Rivitaloremontti.objects.all()

    Referenssit = "Referenssit"
    context = {'Referenssit':Referenssit,'Gallery':Gallery,'Rivitaloremonttiview':Rivitaloremonttiview,}
    return render(request, 'Kuvia.html', context)

def Rivitalonsahkourakointiview(request):
    Rivitalonsahkourakointiview = "Rivitalonsahkourakointiview"
    Gallery = Ravitalonsahko.objects.all()

    Referenssit = "Referenssit"
    context = {'Referenssit':Referenssit,'Gallery':Gallery,'Rivitalonsahkourakointiview':Rivitalonsahkourakointiview,}
    return render(request, 'Kuvia.html', context)

def Hietaniemenkadultaview(request):
    Hietaniemenkadultaa = "Hietaniemenkadulta"
    Gallery = Hietaniemenkadulta.objects.all()

    Referenssit = "Referenssit"
    context = {'Referenssit':Referenssit,'Gallery':Gallery,'Hietaniemenkadultaa':Hietaniemenkadultaa,}
    return render(request, 'Kuvia.html', context)

def Emannantieview(request):
    Emannantie = "Emannantie"

    Referenssit = "Referenssit"
    context = {'Referenssit':Referenssit,'Emannantie':Emannantie,}
    return render(request, 'Kuvia.html', context)

def SoukkaSaunaview(request):
    SoukkaSauna = "SoukkaSauna"

    Referenssit = "Referenssit"
    context = {'Referenssit':Referenssit,'SoukkaSauna':SoukkaSauna,}
    return render(request, 'Kuvia.html', context)


def Jyskview(request):
    Jysk = "Jysk"

    Referenssit = "Referenssit"
    context = {'Referenssit':Referenssit,'Jysk':Jysk,}
    return render(request, 'Kuvia.html', context)


def Uudisrakentaminenview(request):
    Uudisrakentaminenview = "Uudisrakentaminenview"
    Gallery = Uudisrakentaminen.objects.all()

    Referenssit = "Referenssit"
    context = {'Referenssit':Referenssit,'Gallery':Gallery,'Uudisrakentaminenview':Uudisrakentaminenview,}
    return render(request, 'Kuvia.html', context)

def Lumiesteidenasennusview(request):
    Lumiesteidenasennusview = "Lumiesteidenasennusview"
    Gallery = Lumiesteidenasennus.objects.all()

    Referenssit = "Referenssit"
    context = {'Referenssit':Referenssit,'Gallery':Gallery,'Lumiesteidenasennusview':Lumiesteidenasennusview,}
    return render(request, 'Kuvia.html', context)

def ReferenssitEnglish(request):

    Gallery = referencemedia.objects.all()
    English = "English"
    Referenssit = "Referenssit"
    context = {'Referenssit':Referenssit,'Gallery':Gallery,'English':English,}
    return render(request, 'Referenssit.html', context)


def Yhteydenotto(request):

    TheForm = ContactForm()
    Yhteydenotto = "Yhteydenotto"

    context = {'Yhteydenotto':Yhteydenotto, 'TheForm': TheForm,}
    return render(request, 'Yhteystiedot.html', context)

def YhteydenottoEnglish(request):

    TheForm = ContactForm()
    Yhteydenotto = "Yhteydenotto"
    English = "English"
    context = {'Yhteydenotto':Yhteydenotto, 'TheForm': TheForm,'English':English,}
    return render(request, 'Yhteystiedot.html', context)

def Tietoa(request):
    Tietoa = "Tietoa"
    context = {'Tietoa':Tietoa,}
    return render(request, 'Tietoa.html', context)

def Tyopaikat(request):
    Tyopaikat = "Tyopaikat"
    context = {'Tyopaikat':Tyopaikat,}
    return render(request, 'Tyopaikat.html', context)


def TietoaEnglish(request):
    English = "English"
    Tietoa = "Tietoa"
    context = {'Tietoa':Tietoa, 'English':English,}
    return render(request, 'Tietoa.html', context)

def sitemap(request):
    context = {}
    return render(request, 'sitemap.xml', context)

def Cookies(request):
    context = {}
    return render(request, 'Cookies.html', context)

def Sendcontactform(request):

    TheForm = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Message from Komsi website"
            body = {
                    'firstname': form.cleaned_data['firstname'],
                    'lastname': form.cleaned_data['lastname'],
                    'sender': form.cleaned_data['sender'],
                    'phone': form.cleaned_data['phone'],
                    'message': form.cleaned_data['message'],
                    }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'niklas.pettersson@lanach.fi', ['niklas.pettersson@lanach.fi',])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("HomePosted")

    context = {'TheForm': TheForm, }
    return render(request, "index.html", context)


def Sahkopalvelut(request):
    video = Item.objects.all()
    Tietoa = "Tietoa"
    context = {'video':video,'Tietoa':Tietoa}
    return render(request, 'Sahkopalvelut1.html', context)

def sahkotyot_vantaa(request):
    video = Item.objects.all()
    Tietoa = "Tietoa"
    context = {'video':video,'Tietoa':Tietoa}
    return render(request, 'sahkotyot_vantaa.html', context)
