from django.contrib import admin
from .models import Post, PostCategory, Comment, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Category)
admin.site.register(Comment)