from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

TAGS = (("NSFW", "NSFW"), ("SFW", "SFW"))


class Joke(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    body = models.CharField(max_length=500)
    punchline = models.CharField(max_length=300, null=True, blank=True)
    tag = models.CharField(max_length=4, choices=TAGS, default=TAGS[0][0])
    date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("jokes_detail", kwargs={"joke_id": self.id})


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    joke = models.ForeignKey(Joke, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)


class JokeFavorite(models.Model):
    joke = models.ForeignKey(Joke, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["joke", "user"], name="unique_jokes_favorite"
            )
        ]


class CommentFavorite(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True)

