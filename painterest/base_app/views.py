from django.shortcuts import render, HttpResponse, redirect
from .models import UsersDB, PostsDB, CommentsDB
from .forms import ImageForm
import os
from django.conf import settings
from base_app.forms import LoginForm, RegisterForm
import json

def test(request):
    return render(request, "test.html")

def error_404_view(request, exception):
    return render(request, "404.html", status=404)

def home(request):
    items = PostsDB.objects.all()
    islogged = request.session.has_key('islogged')
    return render(request, "home.html", {"posts": items, "islogged": islogged})


def post(request):
    username_logged = None
    islogged = request.session.has_key('islogged')
    if islogged:
        username_logged = request.session['username']

    if request.method == 'POST':

        if request.POST.get('hidde_home_idpost', None):
            id_post_var = request.POST.get('hidde_home_idpost', None)
            post = PostsDB.objects.get(id_post=id_post_var)
        elif request.POST.get('idpost_post', None):
            id_post_var = request.POST.get('idpost_post', None)
            user = UsersDB.objects.get(username=username_logged)
            post = PostsDB.objects.get(id_post=id_post_var)
            comment_description = request.POST.get('comment', None)
            comment = CommentsDB(id_username= user, id_post=post, comment_description=comment_description)#, date=timezone.now())
            comment.save()
        comment = CommentsDB.objects.filter(id_post=id_post_var)

        reponse= render(request, "post.html", {"comments": comment, "idpost_post": id_post_var, "post_pathImg": post.pathImg, "post_title": post.title, "post_description": post.description, "post_date": post.date, "post_like": post.like, "islogged": islogged, "username": username_logged })
        return reponse
    else:
        return redirect(to="/")
    
def profile(request):
    username_logged = None
    islogged = request.session.has_key('islogged')
    if islogged:
        username_logged = request.session['username']

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            image_name = instance.image.name 

            user = UsersDB.objects.get(username=username_logged)
            title = form.cleaned_data['title']
           # description = form.cleaned_data['description']  # Récupère l'objet de l'image
            image = image_name.replace("static/media/", "")
            PostsDB(id_username=user, title=title, description="description", pathImg=image).save()
            return redirect('/')  # Redirigez vers la page d'accueil après le téléchargement
    else:
        form = ImageForm()

    #
    user = UsersDB.objects.get(username=username_logged)
    posts =  []

    islogged = request.session.has_key('islogged')
    return render(request, 'myprofile.html', {'form': form, 'posts' : posts, "islogged": islogged})

def login(request): 
    islogged = request.session.has_key('islogged')
    if islogged:
        return redirect("/")

    if request.method == "POST": 
        hidden_value = request.POST.get('hidden_field', '')

        if hidden_value == 'login' :
            MyLoginForm = LoginForm(request.POST) 
            try:
                if MyLoginForm.is_valid_login(): 
                    username = MyLoginForm.cleaned_data['username']
                    request.session['username'] = username
                    request.session['islogged'] = True
                    return redirect('/profile')  
            except Exception as e:
                return render(request, 'login.html', {"username" : username, "notValidUser": True, "errorMessage": str(e).replace('[', ' ').replace(']', ' ') })
            
        if hidden_value == 'register':
            myRegisterForm = RegisterForm(request.POST) 
            try:
                if myRegisterForm.is_valid_register(): 
                    username = myRegisterForm.cleaned_data['username_register']
                    request.session['username'] = username
                    request.session['islogged'] = True

                    return redirect('/profile')  
            except NameError:
                return render(request, 'login.html', {"username" : username, "notValidUser": True, "errorMessage": str(e).replace('[', ' ').replace(']', ' ')})
            
        
    return render(request, 'login.html')

def logout(request):
    try: 
        del request.session['islogged'] 
        del request.session['username'] 
    except Exception as e:
        print(e)
    return redirect('/') 

    