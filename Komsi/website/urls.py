from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('Korjausrakentaminen/', views.Korjausrakentaminen, name='Korjausrakentaminen'),
    path('Lumenpudotus/', views.Lumenpudotus, name='Lumenpudotus'),
    path('Projektit/', views.Projektit, name='Projektit'),
    path('Yhteydenotto/', views.Yhteydenotto, name='Yhteydenotto'),
    path('Sitemap/', views.Sitemap, name='Sitemap'),
]
