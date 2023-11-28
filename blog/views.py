from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views import generic, View
from django.contrib.auth.forms import UserChangeForm
from .models import Post, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import CommentForm, EditProfileForm

"""
Main view of the page, displays index page and paginates the pages if posts > 6
"""


class Home(ListView):
    model = Post
    template_name = "index.html"
    paginate_by = 6


"""
Detailed view of each individual post, displays a post, author, date.
Likes for the post. Also includes comment section,
 where logged in users can leave their comments.
"""


class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get(self, request, pk, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, pk=pk)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        post_filter = post.get_post_filter_display()
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "post_filter": post_filter,
            },
        )


"""
View for creating a New Post. Logged in users have the ability to:
 create a new post from the nav bar or admin section for admins.
"""


class AddPost(CreateView):
    model = Post
    template_name = "add_post.html"
    fields = (
        "title",
        "content",
        "post_filter",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


"""
View for adding a comments to the selected post.
User ID is automatically applied and displayed,
so does the comment is placed underneath the correct post.
"""


class AddComment(CreateView):
    model = Comment
    template_name = "add_comment.html"
    fields = ("body",)
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.name = self.request.user
        form.instance.post_id = self.kwargs.get("pk")
        return super().form_valid(form)


"""
For a logged in authorized user that matches the author of the post:
Ability to  EDIT the POST.
"""


class EditPost(UpdateView):
    model = Post
    template_name = "edit_post.html"
    fields = [
        "title",
        "content",
        "post_filter",
    ]


"""
For a logged in authorized user that matches the author of the post:
Ability to  DELETE the POST.
"""


class DeletePost(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("index")


"""
Ability for the logged in user to leave a like under a POST.
"""


class PostLike(View):
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse("postdetail", args=[pk]))


"""
Profile page added to the navigation bar,displayed only for the logged in user.
Ability to see user details, as well as edit them.
Username, Email, First Name,Last Name.
"""


def profile(request):
    return render(request, "profile.html")


def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = EditProfileForm(instance=request.user)
        args = {"form": form}
        return render(request, "edit_profile.html", args)


class EditComment(UpdateView):
    model = Comment
    template_name = "edit_comment.html"
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy("postdetail", args=[self.object.post.id])


class DeleteComment(DeleteView):
    model = Comment
    template_name = "delete_comment.html"

    def get_success_url(self):
        return reverse_lazy("postdetail", args=[self.object.post.id])
