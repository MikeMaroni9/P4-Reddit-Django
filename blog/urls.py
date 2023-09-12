from django.urls import path
from .views import Home, PostDetail, AddPost, EditPost, DeletePost

urlpatterns = [
    path('', Home.as_view(), name="index"),
    path('detail/<int:pk>', PostDetail.as_view(), name="postdetail"),
    path('newpost/', AddPost.as_view(), name="addpost"),
    path('detail/edit/<int:pk>', EditPost.as_view(), name="editpost"),
    path('detail/<int:pk>/delete', DeletePost.as_view(), name="deletepost"),
]


