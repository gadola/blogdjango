from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=150,default='')
    text = models.TextField()
    image = models.ImageField((""), upload_to='image/', height_field=None, width_field=None, max_length=None, null=True)
    author = models.ForeignKey('auth.User', related_name='posts',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    objects = models.Manager()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    time = models.DateField(auto_now=False, auto_now_add=True)

