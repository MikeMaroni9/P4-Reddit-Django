from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

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

class EditPost (UpdateView):
    model = Post
    template_name = "edit_post.html"
    fields = ['title', 'content']

class DeletePost (DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('index')
    