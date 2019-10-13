from django.db import models

# Create your models here.

class User(models.Model):#用户
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length=32, unique=True)
    def __str__(self):
        return self.username

class Category(models.Model):#类别
    caption = models.CharField(max_length=16,null=True)
    index = models.IntegerField(default=999, verbose_name="分类的排序")

    def __str__(self):
        return self.caption


class Article(models.Model):#文章
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=32, null=True)
    content = models.TextField()
    click_count = models.IntegerField(default=0)
    is_recommend = models.BooleanField(default=False)
    date_publish = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to='User', to_field='id', on_delete=models.CASCADE)
    category = models.ForeignKey(to='Category', to_field='id',null=True, blank=True, on_delete=models.SET_NULL)
    tag = models.ManyToManyField(to='Tag')
    def __str__(self):
        return self.title

class Tag(models.Model):#标签
    name = models.CharField(max_length=16)
    
    def __str__(self): 
        return self.name

class Indexlink(models.Model):#常用链接
    desc = models.CharField(max_length=32)
    link = models.CharField(max_length=128)
    def __str__(self):
        return self.link

class Comment(models.Model):#评论
    content = models.TextField()
    data_publish = models.DateTimeField(auto_now_add=True)
    pid = models.ForeignKey('self', null=True,  on_delete=models.CASCADE)#父级评论
