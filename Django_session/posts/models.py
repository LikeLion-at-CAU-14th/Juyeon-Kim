from django.db import models
from accounts.models import User
# Create your models here.
# 추상 클래스 정의
class BaseModel(models.Model): # models.Model을 상속받음
    created_at = models.DateTimeField(auto_now_add=True) # 객체를 생성할 때 날짜와 시간 저장
    updated_at = models.DateTimeField(auto_now=True) # 객체를 저장할 때 날짜와 시간 갱신

    class Meta:
        abstract = True


class Post(BaseModel): # BaseModel을 상속받음

    CHOICES = (
        ('STORED', '보관'),
        ('PUBLISHED', '발행')
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=CHOICES, default='STORED')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
    
class Category(models.Model): 

    id = models.AutoField(primary_key=True)
    category_name= models.CharField(max_length=10)
    
    def __str__(self):
        return self.category_name
    
class PostCategory(models.Model): 

    id = models.AutoField(primary_key=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='postcategories')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories')



class Comment(BaseModel): 

    id = models.AutoField(primary_key=True)
    nickname=models.CharField(max_length=10)
    content = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return self.nickname