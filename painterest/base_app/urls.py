from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path("", views.home, name="home"),
    path("post/", views.post, name="post"),
    path("test/", views.test, name="test"),
    path("profile/", views.profile, name="profile"),
    path("search/", views.test, name="test"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'base_app.views.error_404_view'

