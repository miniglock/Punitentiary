from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Joke, Comment, JokeFavorite, CommentFavorite
from .forms import CommentForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class JokeUpdate(UpdateView):
    model = Joke
    fields = ["body", "punchline", "tag"]


def profile(request):
    pass


def joke_favorites_add(request, joke_id):
    j_f = JokeFavorite(user=request.user, joke=Joke.objects.get(id=joke_id))
    j_f.save()
    return redirect("jokes_detail", joke_id=joke_id)


def home(request):
    jokes = Joke.objects.filter(tag="SFW")
    return render(request, "home.html", {"jokes": jokes})


class JokeCreate(LoginRequiredMixin, CreateView):
    model = Joke
    fields = ["body", "punchline", "tag"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class JokeDelete(LoginRequiredMixin, DeleteView):
    model = Joke
    success_url = "/"


def jokes_detail(request, joke_id):
    joke = Joke.objects.get(id=joke_id)
    favorite_count = len(JokeFavorite.objects.filter(joke=joke_id))
    try:
        joke_fav = JokeFavorite.objects.get(user=request.user, joke=joke_id)
    except JokeFavorite.DoesNotExist:
        joke_fav = None

    comments = Comment.objects.filter(joke=joke_id)
    comment_form = CommentForm()
    return render(
        request,
        "jokes/detail.html",
        {
            "joke": joke,
            "comment_form": comment_form,
            "comments": comments,
            "favorite_count": favorite_count,
            "joke_fav": joke_fav,
        },
    )


def profile(request):
    pass


@login_required
def nsfw_jokes(request):
    jokes = Joke.objects.filter(tag="NSFW")
    return render(request, "home.html", {"jokes": jokes})


@login_required
def comments_add(request, joke_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.joke_id = joke_id
        new_comment.user_id = request.user.id
        new_comment.save()
    return redirect("jokes_detail", joke_id=joke_id)


class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    success_url = "/jokes/{joke_id}/"
    fields = ["text"]


class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = "/jokes/{joke_id}/"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            error_message = "Invalid Sign Up - Try Again!"

    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)

