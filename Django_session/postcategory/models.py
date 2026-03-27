from django.db import models
from posts.models import Post
from category.models import Category
# Create your models here.

class PostCategory(models.Model): 

    id = models.AutoField(primary_key=True)
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='postcategory')
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
