from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    photo = CloudinaryField('photo')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date = models.DateTimeField()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
