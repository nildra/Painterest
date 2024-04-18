from django.shortcuts import render, HttpResponse, redirect
from .models import UsersDB, PostsDB, CommentsDB, FollowsDB
from .forms import ImageForm
import os
from django.conf import settings
from base_app.forms import LoginForm, RegisterForm
import time
import random
from django.http import JsonResponse
import json
from django.contrib import messages

def test(request):
    return render(request, "test.html")

def error_404_view(request, exception):
    return render(request, "404.html", status=404)

def home(request):
    items = PostsDB.objects.all().order_by("-id_post")

    
    islogged = request.session.has_key('islogged')
    username_navbar = None
    if islogged : 
        username_navbar = request.session['username']

    return render(request, "home.html", {"posts": items, "islogged": islogged, "username_navbar": username_navbar})

def post(request):
    username_logged = None
    username_navbar = None
    islogged = request.session.has_key('islogged')
    if islogged:
        username_logged = request.session['username']
        username_navbar = request.session['username']

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
        reponse= render(request, "post.html", {"username_navbar": username_navbar, "comments": comment, "idpost_post": id_post_var, "post_pathImg": post.pathImg, "post_title": post.title, "post_description": post.description, "post_date": post.date, "post_like": post.like, "post_user": post.id_username.username,"islogged": islogged, "username": username_logged })
        return reponse
    else:
        return redirect(to="/")
    
def profile(request):
    username_logged = None
    username_navbar = None
    islogged = request.session.has_key('islogged')
    if islogged:
        username_logged = request.session['username']
        username_navbar = request.session['username']
    else:
        return render(request, 'myprofile.html', {"islogged": islogged})


    if request.method == 'POST':

        if request.POST.get('type_form', None) == None:
            return redirect('/')
        elif request.POST.get('type_form', None) == "upload":
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
                PostsDB(id_username=user, title=title, description=description, pathImg=image).save()
                path = "/profile?profile=" + str(username_logged)
                return redirect(path)
        elif request.POST.get('type_form', None) == "follow":
            username_get = request.GET.get('profile', None)
            user_get = UsersDB.objects.get(username=username_get)

            form = ImageForm()
            islogged = request.session.has_key('islogged')
            posts = PostsDB.objects.all().filter(id_username=user_get).order_by("-id_post")
            user_to_follow = request.POST.get('user_to_follow', None)
            user_to_follow = UsersDB.objects.get(username=user_to_follow)
            user = UsersDB.objects.get(username=username_logged)
            FollowsDB(id_follower=user, id_following=user_to_follow).save()

            followers_ids = FollowsDB.objects.filter(id_following=user_to_follow).values_list('id_follower', flat=True)
            followers = UsersDB.objects.filter(id_user__in=followers_ids)

            following_ids = FollowsDB.objects.filter(id_follower=user_to_follow).values_list('id_following', flat=True)
            following = UsersDB.objects.filter(id_user__in=following_ids)

            return render(request, 'myprofile.html', {"username_navbar": username_navbar,'followers': followers, 'following': following, 'form': form, 'posts' : posts, "islogged": islogged, "userpage": username_get})

    else:

        if request.GET.get('profile', None) != None:
            username_get = request.GET.get('profile', None)
            user_get = UsersDB.objects.get(username=username_get)

            form = ImageForm()
            islogged = request.session.has_key('islogged')
            posts = PostsDB.objects.all().filter(id_username=user_get).order_by("-id_post")
            if islogged :
                user = UsersDB.objects.get(username=username_logged)

            followers_ids = FollowsDB.objects.filter(id_following=user_get).values_list('id_follower', flat=True)
            followers = UsersDB.objects.filter(id_user__in=followers_ids)

            following_ids = FollowsDB.objects.filter(id_follower=user_get).values_list('id_following', flat=True)
            following = UsersDB.objects.filter(id_user__in=following_ids)

            return render(request, 'myprofile.html', {"username_navbar": username_navbar,'followers': followers, 'following': following,'form': form, 'posts' : posts, "islogged": islogged, "mypage": (user.username == username_get), "userpage": username_get})
        else:
            return redirect("/")
        
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
                    path = "/profile?profile=" + str(username)
                    return redirect(path)  
            except Exception as e:
                return render(request, 'login.html', {"notValidUser": True, "errorMessage": str(e).replace('[', ' ').replace(']', ' ') })
            
        if hidden_value == 'register':
            myRegisterForm = RegisterForm(request.POST) 
            try:
                if myRegisterForm.is_valid_register(): 
                    username = myRegisterForm.cleaned_data['username_register']
                    request.session['username'] = username
                    request.session['islogged'] = True
                    path = "/profile?profile=" + str(username)
                    return redirect(path)  
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
    username_navbar = None
    islogged = request.session.has_key('islogged')
    if islogged:
        username_logged = request.session['username']
        username_navbar = request.session['username']
    else:
        return redirect("/")

    if request.method == 'POST':

        if request.POST.get('type_form', None) == None:
            id_post_var = request.POST.get('hidde_home_idpost', None)
            post = PostsDB.objects.get(id_post=id_post_var)

            if username_logged == post.id_username.username:
                return render(request, "edit.html", {"username_navbar": username_navbar,"idpost_post": id_post_var, "post_pathImg": post.pathImg, "post_title": post.title, "post_description": post.description, "post_date": post.date, "post_like": post.like, "post_user": post.id_username.username,"islogged": islogged, "username": username_logged })
        elif request.POST.get('type_form', None) == "save":
            id_post_var = request.POST.get('hidde_edit_idpost', None)
            post = PostsDB.objects.get(id_post=id_post_var)
            title = request.POST.get('title', None)
            description = request.POST.get('description', None)
            PostsDB.objects.filter(pk=id_post_var).update(description=description)
            PostsDB.objects.filter(pk=id_post_var).update(title=title)
            return render(request, "edit.html", {"username_navbar": username_navbar,"idpost_post": id_post_var, "post_pathImg": post.pathImg, "post_title": title, "post_description": description, "post_date": post.date, "post_like": post.like, "post_user": post.id_username.username,"islogged": islogged, "username": username_logged, "edit": "Success update" })
        elif request.POST.get('type_form', None) == "delete":
            id_post_var = request.POST.get('hidde_edit_idpost', None)
            post = PostsDB.objects.get(id_post=id_post_var)
            post.delete()
            path = "/profile?profile=" + str(username_logged)
            return redirect(path) 
    else:
        return redirect("/")

def generate_unique_filename(filename):
    timestamp = str(int(time.time()))
    filename, extension = os.path.splitext(filename)
    id_random = random.randint(0, 99999)
    unique_filename = f"{filename}_{timestamp}_{id_random}{extension}"
    return os.path.join('static/media/', unique_filename), unique_filename

def following(request):
    username_logged = None
    username_navbar = None
    islogged = request.session.has_key('islogged')
    if islogged:
        username_logged = request.session['username']
        username_navbar = request.session['username']
        
        user = UsersDB.objects.get(username=username_logged)

        following_ids = FollowsDB.objects.filter(id_follower=user).values_list('id_following', flat=True)
        posts_following = PostsDB.objects.filter(id_username__in=following_ids)

        return render(request, "following.html", {'posts_following': posts_following, "username_navbar": username_navbar, "islogged": islogged})
    return render(request, "following.html", {"islogged": islogged})
