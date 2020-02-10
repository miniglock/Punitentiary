from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("jokes/nsfw_jokes/", views.nsfw_jokes, name="nsfw_jokes"),
    path("jokes/create/", views.JokeCreate.as_view(), name="jokes_create"),
    path("jokes/<int:joke_id>/", views.jokes_detail, name="jokes_detail"),
    path("jokes/<int:pk>/update/", views.JokeUpdate.as_view(), name="jokes_update"),
    path("jokes/<int:pk>/delete/", views.JokeDelete.as_view(), name="jokes_delete"),
    path("jokes/<int:joke_id>/comments_add/", views.comments_add, name="comments_add"),
    path(
        "comment/<int:pk>/update/",
        views.CommentUpdate.as_view(),
        name="comments_update",
    ),
    path(
        "comment/<int:pk>/delete/",
        views.CommentDelete.as_view(),
        name="comments_delete",
    ),
    path("accounts/profile/", views.profile, name="profile"),
    path("accounts/signup/", views.signup, name="signup"),
]

