from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path("", views.home, name="home"),
    path("upload/", views.upload_image, name="upload"),
    path("post/", views.post, name="post"),
    path("test/", views.test, name="test"),
    path("login/", views.test, name="login"),
    path("profile/", views.test, name="test"),
    path("search/", views.test, name="test"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'base_app.views.error_404_view'