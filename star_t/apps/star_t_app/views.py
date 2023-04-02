from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Joke
from .forms import JokeForm

# Create your views here.
def index(request):
    context = {
        "favorite_animal": "llama"
    }
    return render(request, "index.html", context=context)

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["fname"]
        password = request.POST["password"]
        conf_password = request.POST["conf_password"]

        if password == conf_password:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                password=password
            )

            login(request, user)

            return redirect("/dashboard")
        else:
            messages.add_message(
                request,
                messages.ERROR,
                f"You effed up, {first_name}! The passwords don't match!"
            )
            return redirect("/")

    else:
        return redirect("/")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.add_message(
                request,
                messages.ERROR,
                "Aye! Couldn't find that user/password combination"
            )
            return redirect("/")
        else:
            login( request, user)
            return redirect("/dashboard")

    else:
        return redirect("/")

@login_required(login_url="/")
def dashboard(request):
    jokes = Joke.objects.filter(age_appropriate__lte=10)
    context = {"jokes": jokes}
    return render(request, "dashboard.html", context=context)

@login_required(login_url="/")
def joke_form(request):
    if request.method == "POST":
        joke_text=request.POST["joke_text"]
        punchline=request.POST["punchline"]
        age=request.POST["age_appropriate"]
        Joke.objects.create(
            joke_text=joke_text,
            punchline=punchline,
            age_appropriate=age,
            user=request.user
        )
        return redirect("/dashboard")
    context = {"form": JokeForm}
    return render(request, "form.html", context=context)

def logout_view(request):
    logout(request)
    return redirect("/")