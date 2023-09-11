from django.urls import path
from .views import Home, PostDetail, AddPost

urlpatterns = [
    path('', Home.as_view(), name="index"),
    path('detail/<int:pk>', PostDetail.as_view(), name="postdetail"),
    path('newpost/', AddPost.as_view(), name="addpost"),
]


