from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    contact = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
    owner = models.CharField(max_length=30)

class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
