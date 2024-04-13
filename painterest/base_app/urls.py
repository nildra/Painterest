from django.urls import path
from . import views

urlpatterns = [
    path("", views.test, name="main"),
    path("home/", views.home, name="homes"),
    path('signup/', views.signup, name='signup'),# Définition de l'URL nommée 'signup'
    path('login/', views.login, name='login'),# Définition de l'URL nommée 'login'
    path('logout/', views.deconnexion, name='logout') # Définition de l'URL nommée 'logout'
]