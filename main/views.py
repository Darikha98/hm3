from django.shortcuts import render, redirect
from django.http import  HttpResponse

import random
# Create your views here.
from django.template.context_processors import request
from django.views.generic import UpdateView, ListView, DetailView, CreateView

from main.models import BlogPost


def dariha(request):
    num = random.randint(1, 100)

    return HttpResponse(num)

def bloglist(request):
    blogs = BlogPost.objects.all()
    context = {'blogs':blogs}
    return render(request, 'blog.html', context)

class BlogListView(ListView):
    model = BlogPost
    fields = ['title', 'description','likes', 'repost', 'image']
    template_name ='blog.html'
    context_object_name = 'blogs'

def blogDetail(request, id):
    blog = BlogPost.objects.get(id=id)
    context = {'blog': blog}
    return render(request, 'blogDetail.html', context)
class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blogDetail.html'
    context_object_name = 'blog'

def creatBlog(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        BlogPost.objects.create(title =title, description= description, image = image)
        return redirect('/blog/')
    if request.method=="GET":
        return render(request, 'blogCread.html')

class BlogCreateView(CreateView):
    model = BlogPost
    template_name ='blogCread.html'
    fields = ['title', 'description', 'image']

class BlogChange(UpdateView):
    model = BlogPost
    fields = ['title', 'description', 'image']
    template_name = 'blogUpdate.html'


