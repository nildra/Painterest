from django.shortcuts import render, HttpResponse, redirect
from .models import UsersDB
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

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
            user = form.save()  # Enregistrement de l'utilisateur dans la base de données
            # Connexion automatique de l'utilisateur après l'inscription
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # Redirection vers la page de confirmation d'inscription
            return redirect('inscription_reussie.html')  
    else:
        form = UserCreationForm()
    return render(request, 'index_signup.html', {'form': form})

def inscription_reussie(request, user_id):
    # Récupération de l'utilisateur à partir de l'identifiant et affichage de ses informations dans la page de confirmation
    user = UsersDB.objects.get(id=user_id)
    return render(request, 'inscription_reussie.html', {'user': user})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('base.html')  # Redirection vers la page d'accueil après une connexion réussie
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def deconnexion(request):
    logout(request)  # Déconnexion de l'utilisateur
    return redirect('base.html')  # Rediriger l'utilisateur vers la page d'accueil 