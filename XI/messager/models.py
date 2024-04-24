from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Post(models.Model):

    owner = models.CharField(max_length=250, default="")
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=550)
    posted_time = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    about = models.CharField(max_length=550)
    age = models.DateField
    country = models.CharField(max_length=250)
