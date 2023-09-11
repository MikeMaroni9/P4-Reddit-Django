from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class Home(ListView):
    model = Post
    template_name = 'index.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
