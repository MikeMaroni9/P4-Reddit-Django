from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import generic, View
from .models import Post,Comment
from django.http import HttpResponseRedirect
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
    fields = 'title', 'content', 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddComment(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = 'body',
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.name = self.request.user
        form.instance.post_id = self.kwargs.get('pk')
        return super().form_valid(form)


class EditPost (UpdateView):
    model = Post
    template_name = "edit_post.html"
    fields = ['title', 'content']

class DeletePost (DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('index')
    
class PostLike(View):
    
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('postdetail', args=[pk]))

#Profile for NavBar
def profile(request):
    return render(request, 'profile.html')