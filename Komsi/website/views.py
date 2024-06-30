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


def contact(request):

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
    return render(request, 'contact.html', context={'yhteydenotto':yhteydenotto,'contacts': contacts})


def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', context={'services': services})


def career(request):

    has_next = False
    blogs = BlogPost.objects.all()
    if blogs.count() > MAX_INSTA_POSTS:
        blogs = blogs[:MAX_INSTA_POSTS]
        has_next = True
    context = {'blogs': blogs, 'has_next': has_next}
    return render(request, 'blog-listing.html', context)


def blog_listing_page(request):

    has_next = False
    blogs = BlogPost.objects.all().order_by('-id')
    if blogs.count() > MAX_INSTA_POSTS:
        blogs = blogs[:MAX_INSTA_POSTS]
        has_next = True
    print(blogs)
    context = {'posts': blogs, 'has_next': has_next}
    return render(request, 'blog.html', context)


def get_blog_posts(request):
    # Get all objects from the model
    object_list = BlogPost.objects.all().order_by('-id')

    # Number of objects to display per page
    objects_per_page = MAX_INSTA_POSTS
    paginator = Paginator(object_list, objects_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver the last page
        objects = paginator.page(paginator.num_pages)

    serialized_data = []

    for obj in objects:
        post = {
            "id": obj.id,
            "title": obj.title,
            "image": obj.image.url,
            "content": obj.content,
        }
        serialized_data.append(post)

    data = {
        'posts': serialized_data,
        'has_previous': objects.has_previous(),
        'has_next': objects.has_next(),
        'number': objects.number,
        "last_number": objects.paginator.num_pages
    }
    return JsonResponse(data)


def blog_post_detail(request, blog_slug):
    post = get_object_or_404(BlogPost, slug=blog_slug)
    posts = BlogPost.objects.all()
    # Fetch the next and previous posts based on the timestamp field
    next_post = BlogPost.objects.filter(timestamp__gt=post.timestamp).order_by('timestamp').first()
    previous_post = BlogPost.objects.filter(timestamp__lt=post.timestamp).order_by('-timestamp').first()

    context = {
        'posts':posts,
        'post': post,
        'next_post': next_post,
        'previous_post': previous_post,
    }

    return render(request, 'blog-single.html', context)


def project_listing_page(request):

    referenssit = "referenssit"
    has_next = False
    projects = Project.objects.all()
    print(projects)
    context = {'referenssit': referenssit,'projects': projects, 'has_next': has_next}
    return render(request, 'projects.html', context)


"""
def get_projects(request):
    # Get all objects from the model
    object_list = Project.objects.all()

    # Number of objects to display per page
    objects_per_page = MAX_INSTA_POSTS
    paginator = Paginator(object_list, objects_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver the last page
        objects = paginator.page(paginator.num_pages)

    serialized_data = []

    for obj in objects:
        post = {
            "id": obj.id,
            "title": obj.title,
            "image": obj.image.url,
            "content": obj.content,
        }
        serialized_data.append(post)

    data = {
        'posts': serialized_data,
        'has_previous': objects.has_previous(),
        'has_next': objects.has_next(),
        'number': objects.number,
        "last_number": objects.paginator.num_pages
    }
    return JsonResponse(data)
"""


def project_detail(request, project_slug):
    post = get_object_or_404(Project, slug=project_slug)

    # Fetch the next and previous posts based on the timestamp field
    next_post = Project.objects.filter(id__gt=post.id).order_by('id').first()
    previous_post = Project.objects.filter(id__lt=post.id).order_by('-id').first()

    context = {
        'project': post,
        'next_post': next_post,
        'previous_post': previous_post,
    }

    return render(request, 'project-details.html', context)
