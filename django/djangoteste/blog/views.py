from .models import Post

from django.views.generic import DetailView, ListView
from django.shortcuts import render

from blog.models import Post 


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

def index(request): 
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})