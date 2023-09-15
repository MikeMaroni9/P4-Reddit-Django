from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


"""
Status for Posts, Draft or Published. It is set to be Published by default. 
"""
STATUS = ((0, "Draft"), (1, "Published"))


"""
Form for creating a New Post
"""
class Post(models.Model):
    title = models.CharField(max_length=200, unique = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS,default = 1)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index')

    def number_of_likes(self):
        return self.likes.count()


"""
Form for creating a New Comment
"""
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"