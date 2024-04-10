from django.shortcuts import render, HttpResponse
from .models import UsersDB

# Create your views here.
def test(request):
    return render(request, "main.html")

def home(request):
    items = UsersDB.objects.all()
    return render(request, "home.html", {"elements": items})