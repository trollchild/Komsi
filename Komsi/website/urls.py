from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('Korjausrakentaminen/', views.Korjausrakentaminen, name='Korjausrakentaminen'),
    path('Lumenpudotus/', views.Lumenpudotus, name='Lumenpudotus'),
    path('projects/', views.project_listing_page, name='project_listing_page'),
    path('projects/<str:project_slug>/', views.project_detail, name='project_detail'),
    path('blogs/', views.blog_listing_page, name='blog_listing_page'),
    path('blogs/<str:blog_slug>/', views.blog_post_detail, name='blog_post_detail'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]
