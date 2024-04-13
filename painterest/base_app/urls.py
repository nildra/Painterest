from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path("", views.test, name="main"),
    path("home/", views.home, name="homes"),
    path("upload/", views.upload_image, name="upload"),
    path("post/", views.post, name="post")

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)