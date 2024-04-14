from django.shortcuts import render, redirect, HttpResponse
from .models import UsersDB
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate, logout, views as auth_views
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.tokens import UserCreationForm, default_token_generator
from django.urls import reverse_lazy



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
            # Sauvegarder l'utilisateur
            form.save()
            
            # Rediriger vers la page de confirmation
            return redirect('inscription_reussie.html')

    else:
        form = UserCreationForm()
        messages.error(request, "Erreur lors de l'inscription.")
    return render(request, 'index_signup.html', {'form': form})

def inscription_reussie(request):
    messages.success(request, 'Hey inscription réussie.')
    return render(request, 'index_login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        user = authenticate(request=request, username=username, email=email)

        if user is not None:
            login(request, user)
            messages.success(request, 'Identifiants corrects.')
            return redirect('main.html')  # Redirect to main page after successful login
        else:
            messages.error(request, 'Identifiants incorrects.')

    return render(request, 'index_login.html')

    
def my_logout(request):
    logout(request)
    messages.success(request, 'Vous venez de vous déconnecter !')
    return render('logout.html') # Redirect to login page after logout


class ForgotPasswordView(PasswordResetView):
    template_name = 'forgot_password.html'
    email_template_name = 'registration/password_reset_email.html'  # page où l'e-mail de réinitialisation a été envoyé à l'utilisateur
    subject_template_name = 'registration/password_reset_subject.txt'  # sujet de l'e-mail de réinitialisation
    success_url = reverse_lazy('index_login.html')  # URL de redirection après l'envoi de l'e-mail de réinitialisation

    def form_valid(self, form):
        messages.success(self.request, "Un e-mail de réinitialisation de mot de passe a été envoyé. Veuillez vérifier votre boîte de réception.")
        return super().form_valid(form)