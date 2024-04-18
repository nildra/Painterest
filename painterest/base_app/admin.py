from django.contrib import admin
from .models import UsersDB, PostsDB, CommentsDB, FollowsDB

# Register your models here.
admin.site.register(UsersDB)
admin.site.register(PostsDB)
admin.site.register(CommentsDB)
admin.site.register(FollowsDB)