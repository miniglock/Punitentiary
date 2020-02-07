from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("nsfw_jokes", views.nsfw_jokes, name="nsfw_jokes"),
    path("jokes_create", views.jokes_create, name="jokes_create"),
    path("signup", views.signup, name="signup"),
]

