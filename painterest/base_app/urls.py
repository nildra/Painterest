from django.urls import path
from . import views

urlpatterns = [
    path("", views.test, name="main"),
    path("home/", views.home, name="homes"),
    path("post/", views.post, name="post")
]