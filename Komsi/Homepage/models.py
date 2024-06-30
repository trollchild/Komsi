from django.db import models
from embed_video.fields import EmbedVideoField

#Yleisest
class referencemedia(models.Model):
    text = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)

#Kohde Teollisuushallin sähköurakointi Karhunkoropi
class HalliTyomaa(models.Model):
    text = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)

#Myymäläremontti
class Rengashalli(models.Model):
    text = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)

#Rivitalon muutostyöremontti
class Rivitaloremontti(models.Model):
    text = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)

class Lumiesteidenasennus(models.Model):
    text = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
# Create your models here.

class Ravitalonsahko(models.Model):
    text = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
# Create your models here.
#Uudisrakentaminen
class Uudisrakentaminen(models.Model):
    text = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)

#kerrostalon muutosremontti sähköurakka ja maalaus
class Hietaniemenkadulta(models.Model):
    text = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
