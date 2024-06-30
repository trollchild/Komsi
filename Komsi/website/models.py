from django.db import models
from django.utils.text import slugify


# Create your models here.


class Images(models.Model):
    title = models.CharField(max_length=255, verbose_name="Otsikko")
    image = models.ImageField(upload_to='poject_gallery/', null=True)

    def __str__(self) -> str:
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=150, unique=True)
    content = models.TextField()
    meta_description = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='blog_images/', blank=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=150, unique=True)
    content = models.TextField()
    meta_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='projects/', null=True)
    gallery = models.ManyToManyField(Images, null=True, blank=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=150, unique=True)
    content = models.TextField()
    meta_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='services/', null=True)
    video_url = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    image = models.ImageField(upload_to='contacts/', null=True)
    contact_type = models.IntegerField(default=1)


class WebsiteContent(models.Model):
    content_name = models.CharField(max_length=100)
    title = models.CharField(max_length=255, verbose_name="Otsikko")
    content = models.TextField(null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='website_content/', null=True, blank=True)

    def __str__(self) -> str:
        return self.content_name
