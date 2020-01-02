from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse('<h1> Blog Home </h1>')

def about(request):
    # return HttpResponse('<h1> blog about </h1>')
    return render(request, 'blog/about.html', { 'title': 'About' })