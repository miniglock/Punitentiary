from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

TAGS = (("NSFW", "NSFW"), ("SFW", "SFW"))


class Joke(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    text = models.CharField(max_length=500)
    tag = models.CharField(max_length=4, choices=TAGS, default=TAGS[0][0])
    date = models.DateField()


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    joke = models.ForeignKey(Joke, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date = models.DateField()


class JokeFavorite(models.Model):
    joke = models.ForeignKey(Joke, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date = models.DateField()


class CommentFavorite(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date = models.DateField()

