from math import prod
from django.shortcuts import render
from .models import *

# Create your views here.
def HomeView(request):
    news = Gallery.objects.all().order_by("-date_taken")[:3]
    context = {
        'news':news
    }
    return render (request, 'home.html', context)

def CategoryView(request):
    category = Category.objects.filter(availability=True)
    context = {
        'category':category
    }
    return render (request, 'category.html', context)

def MenuView(request, slug):
    if(Category.objects.filter(slug=slug, availability=True)):
        products = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        context = {
            'products':products,
            'category_name':category_name,
        }
        return render(request, 'menu.html', context)

def LocationView(request):
    return render(request, 'location.html')


def GalleryView(request):
    gallery = Gallery.objects.all().order_by("-date_taken")
    context = {
        'gallery':gallery
    }
    return render(request, 'gallery.html', context)
