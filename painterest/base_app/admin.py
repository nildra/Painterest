from django.contrib import admin
from .models import UsersDB, PostsDB, CommentsDB, LikesDB

# Register your models here.
admin.site.register(UsersDB)
admin.site.register(PostsDB)
admin.site.register(CommentsDB)
admin.site.register(LikesDB)