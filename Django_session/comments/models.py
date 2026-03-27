from django.db import models
from posts.models import Post

class BaseModel(models.Model): 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        abstract = True

class Comment(BaseModel): 

    id = models.AutoField(primary_key=True)
    nickname=models.CharField(max_length=10)
    content = models.TextField()
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comment')

    def __str__(self):
        return self.nickname