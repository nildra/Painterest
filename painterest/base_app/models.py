from django.db import models
from django.conf import settings
import time
import os
import random
from django.utils import timezone
# Create your models here.
class UsersDB(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    role = models.BooleanField(default=False)

class PostsDB(models.Model):
    id_post = models.AutoField(primary_key=True)
    id_username = models.ForeignKey(UsersDB, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    pathImg = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    like = models.IntegerField(default=0)

class CommentsDB(models.Model):
    id_comment = models.AutoField(primary_key=True)
    id_username = models.ForeignKey(UsersDB, on_delete=models.CASCADE)
    id_post = models.ForeignKey(PostsDB, on_delete=models.CASCADE)
    comment_description = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)


def generate_unique_filename(filename):
    timestamp = str(int(time.time()))
    filename, extension = os.path.splitext(filename)
    id_random = random.randint(0, 99999)
    unique_filename = f"{filename}_{timestamp}_{id_random}{extension}"
    return os.path.join('static/media/', unique_filename)

# class Image(models.Model):
#     title = models.CharField(max_length=100)
#     #description = models.CharField(max_length=255)
#     image = models.ImageField(upload_to=generate_unique_filename)