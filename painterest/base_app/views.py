from django.shortcuts import render, HttpResponse, redirect
from .models import UsersDB
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

# Create your views here.
def test(request):
    return render(request, "main.html")

def home(request):
    items = UsersDB.objects.all()
    return render(request, "home.html", {"elements": items})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Rediriger l'utilisateur vers une page spécifique après inscription
            return redirect('inscription_reussie')  # Rediriger vers une page nommée 'inscription_reussie'
    else:
        form = UserCreationForm()
    return render(request, 'index_signup.html', {'form': form})

def deconnexion(request):
    logout(request)  # Déconnexion de l'utilisateur
    return redirect('home')  # Rediriger l'utilisateur vers la page d'accueil 