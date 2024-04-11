from django.shortcuts import render, HttpResponse
from .models import UsersDB, PostsDB

# Create your views here.
def test(request):
    return render(request, "main.html")

def home(request):
    items = PostsDB.objects.all()
    return render(request, "home.html", {"posts": items})

def post(request):
    return render(request, "post.html")

"""
   user = UsersDB.objects.get(username='Alice')
    nouveau_post = PostsDB(id_username=user, title='Je suis un chat', description='Description du post', pathImg='img/chat.jpg')
    nouveau_post.save()
    nouveau_post = PostsDB(id_username=user, title='Je suis un chat', description='Description du post', pathImg='img/flower.jpg')
    nouveau_post.save()
    nouveau_post = PostsDB(id_username=user, title='Je suis un chat', description='Description du post', pathImg='img/gateau.jpg')
    nouveau_post.save()
    nouveau_post = PostsDB(id_username=user, title='Je suis un chat', description='Description du post', pathImg='img/chat.jpg')
    nouveau_post.save()
    nouveau_post = PostsDB(id_username=user, title='Je suis un chat', description='Description du post', pathImg='img/style.jpg')
    nouveau_post.save()
    nouveau_post = PostsDB(id_username=user, title='Je suis un chat', description='Description du post', pathImg='img/the.jpg')
    nouveau_post.save()
    nouveau_post = PostsDB(id_username=user, title='Je suis un chat', description='Description du post', pathImg='img/chat.jpg')
    nouveau_post.save()
    nouveau_post = PostsDB(id_username=user, title='Je suis un chat', description='Description du post', pathImg='img/gateau.jpg')
    nouveau_post.save()
    nouveau_post = PostsDB(id_username=user, title='Je suis un chat', description='Description du post', pathImg='img/style.jpg')
    nouveau_post.save()
    nouveau_post = PostsDB(id_username=user, title='Je suis un chat', description='Description du post', pathImg='img/flower.jpg')
    nouveau_post.save()
    nouveau_post = PostsDB(id_username=user, title='Je suis un chat', description='Description du post', pathImg='img/the.jpg')
    nouveau_post.save()
    nouveau_post = PostsDB(id_username=user, title='Je suis un chat', description='Description du post', pathImg='img/style.jpg')
    nouveau_post.save()
    nouveau_post = PostsDB(id_username=user, title='Je suis un chat', description='Description du post', pathImg='img/gateau.jpg')
    nouveau_post.save()
    nouveau_post = PostsDB(id_username=user, title='Je suis un chat', description='Description du post', pathImg='img/chat.jpg')
    nouveau_post.save()
    nouveau_post = PostsDB(id_username=user, title='Je suis un chat', description='Description du post', pathImg='img/style.jpg')
    nouveau_post.save()
    nouveau_post = PostsDB(id_username=user, title='Je suis un chat', description='Description du post', pathImg='img/flower.jpg')
    nouveau_post.save()
    nouveau_post = PostsDB(id_username=user, title='Je suis un chat', description='Description du post', pathImg='img/style.jpg')
    nouveau_post.save()
"""