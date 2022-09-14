from django.contrib import admin

# Register your models here.

from .models import Post, User, SubPost, Tag

admin.site.register(Post)
admin.site.register(User)
admin.site.register(SubPost)
admin.site.register(Tag)