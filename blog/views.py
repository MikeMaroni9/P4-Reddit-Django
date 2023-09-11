from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class Home(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 6

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = 'title', 'content', 'author',
