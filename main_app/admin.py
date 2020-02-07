from django.contrib import admin
from .models import Joke, Comment, JokeFavorite, CommentFavorite

# Register your models here.
admin.site.register(Joke)
admin.site.register(Comment)
admin.site.register(JokeFavorite)
admin.site.register(CommentFavorite)
