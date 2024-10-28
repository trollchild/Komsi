from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import BlogPost, Project, Service, Contact
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

MAX_INSTA_POSTS = 2


def index(request):
    etusivu = "etusivu"
    return render(request, 'home.html', context={'etusivu':etusivu})

def Korjausrakentaminen(request):
    Korjausrakentaminen = "Korjausrakentaminen"
    return render(request, 'Kattotyot.html', context={'Korjausrakentaminen':Korjausrakentaminen})

def Lumenpudotus(request):
    Lumenpudotus = "Lumenpudotus"
    return render(request, 'Lumenpudotus.html', context={'Lumenpudotus':Lumenpudotus})

def Projektit(request):
    Projektit = "Projektit"
    return render(request, 'Projektit.html', context={'Projektit':Projektit})

def Sitemap(request):
    return render(request, 'sitemap.xml',)


def Yhteydenotto(request):

    if request.method == "POST":
        # get form values
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            send_mail(
                subject,
                f'Name: {name}\nEmail: {email}\n\n{message}',
                settings.EMAIL_HOST_USER,  # Sender's email
                [settings.EMAIL_HOST_USER],  # List of recipients
                fail_silently=False,
            )
            return JsonResponse({'success': True})
        except Exception as e:
            print(e)
            return JsonResponse({'success': False, 'error': str(e)})

    yhteydenotto = "yhteydenotto"
    contacts = Contact.objects.all()
    return render(request, 'Yhteydenotto.html', context={'yhteydenotto':yhteydenotto,'contacts': contacts})
