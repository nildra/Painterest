from django.shortcuts import render, HttpResponse, redirect
from .models import UsersDB, PostsDB, CommentsDB
from .forms import ImageForm
import os
from django.conf import settings
from base_app.forms import LoginForm, RegisterForm
import time
import random
from django.http import JsonResponse
import json

def test(request):
    return render(request, "test.html")

def error_404_view(request, exception):
    return render(request, "404.html", status=404)

def home(request):
    items = PostsDB.objects.all().order_by("-id_post")
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
        reponse= render(request, "post.html", {"comments": comment, "idpost_post": id_post_var, "post_pathImg": post.pathImg, "post_title": post.title, "post_description": post.description, "post_date": post.date, "post_like": post.like, "post_user": post.id_username.username,"islogged": islogged, "username": username_logged })
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

            user = UsersDB.objects.get(username=username_logged)
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            upload_image = form.cleaned_data['upload_image']

            file_path, image = generate_unique_filename(upload_image.name)

            with open(file_path, 'wb') as f:
                for chunk in upload_image.chunks():
                    f.write(chunk)
            

            #image = image_name.replace("static/media/", "")
            PostsDB(id_username=user, title=title, description=description, pathImg=image).save()
            return redirect('/profile')
    else:
        form = ImageForm()

    islogged = request.session.has_key('islogged')
    posts = None
    if islogged :
        user = UsersDB.objects.get(username=username_logged)
        posts = PostsDB.objects.all().filter(id_username=user).order_by("-id_post")

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
                return render(request, 'login.html', {"notValidUser": True, "errorMessage": str(e).replace('[', ' ').replace(']', ' ') })
            
        if hidden_value == 'register':
            myRegisterForm = RegisterForm(request.POST) 
            try:
                if myRegisterForm.is_valid_register(): 
                    username = myRegisterForm.cleaned_data['username_register']
                    request.session['username'] = username
                    request.session['islogged'] = True

                    return redirect('/profile')  
            except NameError:
                return render(request, 'login.html', {"notValidUser": True, "errorMessage": str(e).replace('[', ' ').replace(']', ' ')})
                  
    return render(request, 'login.html')

def logout(request):
    try: 
        del request.session['islogged'] 
        del request.session['username'] 
    except Exception as e:
        print(e)
    return redirect('/') 

def edit(request):
    username_logged = None
    islogged = request.session.has_key('islogged')
    if islogged:
        username_logged = request.session['username']
    else:
        print("####################### not connected")
        return redirect("/")

    print("#######################  OK", request.method)

    if request.method == 'POST':
        id_post_var = request.POST.get('hidde_home_idpost', None)
        post = PostsDB.objects.get(id_post=id_post_var)

        if username_logged == post.id_username.username:
            return render(request, "edit.html", {"idpost_post": id_post_var, "post_pathImg": post.pathImg, "post_title": post.title, "post_description": post.description, "post_date": post.date, "post_like": post.like, "post_user": post.id_username.username,"islogged": islogged, "username": username_logged })
    elif request.method == 'DELETE':
            try:
                data = json.loads(request.body)
                id_post_var = data.get('hidden_home_idpost')

                print(id_post_var)
                post = PostsDB.objects.get(id_post=id_post_var)
                post.delete()
                return JsonResponse("Post deleted successfully.")
            except PostsDB.DoesNotExist:
                return JsonResponse("Post does not exist.")
    elif request.method == 'PUT':
            id_post_var = request.POST.get('hidde_home_idpost', None)
            title = request.POST.get('title', None)
            description = request.POST.get('description', None)

            PostsDB.objects.filter(pk=id_post_var).update(description=description)
            PostsDB.objects.filter(pk=id_post_var).update(title=title)
            PostsDB.save()
            return render(request, "edit.html", {"idpost_post": id_post_var, "post_pathImg": post.pathImg, "post_title": post.title, "post_description": post.description, "post_date": post.date, "post_like": post.like, "post_user": post.id_username.username,"islogged": islogged, "username": username_logged, "edit": "Success update" })
    else:
        return redirect("/")



def generate_unique_filename(filename):
    timestamp = str(int(time.time()))
    filename, extension = os.path.splitext(filename)
    id_random = random.randint(0, 99999)
    unique_filename = f"{filename}_{timestamp}_{id_random}{extension}"
    return os.path.join('static/media/', unique_filename), unique_filename
