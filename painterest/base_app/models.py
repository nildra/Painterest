from django.db import models

# Create your models here.
class UsersDB(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    role = models.BooleanField(default=False)

class PostsDB(models.Model):
    id_post = models.AutoField(primary_key=True)
    id_username = models.ForeignKey(UsersDB, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    pathImg = models.CharField(max_length=255)