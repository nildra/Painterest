from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone
from .models import UsersDB, PostsDB, CommentsDB
from .forms import ImageForm
import os
from django.conf import settings

def test(request):
    return render(request, "test.html")

def error_404_view(request, exception):
    return render(request, "404.html", status=404)


def home(request):
    items = PostsDB.objects.all()
    return render(request, "home.html", {"posts": items})

def post(request):
    if request.method == 'POST':
        if request.POST.get('hidde_home_idpost', None):
            id_post_var = request.POST.get('hidde_home_idpost', None)
            post = PostsDB.objects.get(id_post=id_post_var)
        elif request.POST.get('idpost_post', None):
            id_post_var = request.POST.get('idpost_post', None)
            user = UsersDB.objects.get(username='Alice')
            post = PostsDB.objects.get(id_post=id_post_var)
            comment_description = request.POST.get('comment', None)
            comment = CommentsDB(id_username= user, id_post=post, comment_description=comment_description)#, date=timezone.now())
            comment.save()
        comment = CommentsDB.objects.filter(id_post=id_post_var)
        reponse= render(request, "post.html", {"comments": comment, "idpost_post": id_post_var, "post_pathImg": post.pathImg, "post_title": post.title, "post_description": post.description, "post_date": post.date, "post_like": post.like})
        return reponse
    else:
        return redirect(to="/")
    
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            image_name = instance.image.name 

            user = UsersDB.objects.get(username='Alice')
            title = form.cleaned_data['title']
           # description = form.cleaned_data['description']  # Récupère l'objet de l'image
            image = image_name.replace("static/media/", "")
            PostsDB(id_username=user, title=title, description="description", pathImg=image).save()
            return redirect('/')  # Redirigez vers la page d'accueil après le téléchargement
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})




"""
    user = UsersDB.objects.get(username='Alice')
    PostsDB(id_username=user, title="Je suis un chat", description="Voici une adorable photo d'un chat.", pathImg="chat.jpg").save()
    PostsDB(id_username=user, title="J'aime les fleurs", description="Une belle photo de fleurs dans un jardin.", pathImg="flower.jpg").save()
    PostsDB(id_username=user, title="Tea Time !!", description="Une tasse de thé fumant, parfait pour une pause détente.", pathImg="the.jpg").save()
    PostsDB(id_username=user, title="Trop de style", description="Un look incroyablement élégant pour impressionner.", pathImg="style.jpg").save()
    PostsDB(id_username=user, title="Miam", description="Un délicieux gâteau qui met l'eau à la bouche.", pathImg="gateau.jpg").save()
    PostsDB(id_username=user, title="Je suis un chat", description="Voici une adorable photo d'un chat.", pathImg="chat.jpg").save()
    PostsDB(id_username=user, title="J'aime les fleurs", description="Une belle photo de fleurs dans un jardin.", pathImg="flower.jpg").save()
    PostsDB(id_username=user, title="Tea Time !!", description="Une tasse de thé fumant, parfait pour une pause détente.", pathImg="the.jpg").save()
    PostsDB(id_username=user, title="Trop de style", description="Un look incroyablement élégant pour impressionner.", pathImg="style.jpg").save()
    PostsDB(id_username=user, title="Miam", description="Un délicieux gâteau qui met l'eau à la bouche.", pathImg="gateau.jpg").save()
    PostsDB(id_username=user, title="Je suis un chat", description="Voici une adorable photo d'un chat.", pathImg="chat.jpg").save()
    PostsDB(id_username=user, title="J'aime les fleurs", description="Une belle photo de fleurs dans un jardin.", pathImg="flower.jpg").save()
    PostsDB(id_username=user, title="Tea Time !!", description="Une tasse de thé fumant, parfait pour une pause détente.", pathImg="the.jpg").save()
    PostsDB(id_username=user, title="Trop de style", description="Un look incroyablement élégant pour impressionner.", pathImg="style.jpg").save()
    PostsDB(id_username=user, title="Miam", description="Un délicieux gâteau qui met l'eau à la bouche.", pathImg="gateau.jpg").save()
"""