from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,Comment
from django.urls import reverse_lazy
from .forms import CommentForm

class Home(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 6

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get(self, request, pk, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, pk=pk)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = 'title', 'content', 'author',

class AddComment(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = 'body', 'post','name',
    success_url = reverse_lazy('index')

class EditPost (UpdateView):
    model = Post
    template_name = "edit_post.html"
    fields = ['title', 'content']

class DeletePost (DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('index')
    