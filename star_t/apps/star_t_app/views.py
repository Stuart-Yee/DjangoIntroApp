from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
            # define an error message
            return redirect("/")

    else:
        return redirect("/")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            return redirect("/")
        else:
            login( request, user)
            return redirect("/dashboard")

    else:
        return redirect("/")

@login_required(login_url="/")
def dashboard(request):
    return render(request, "dashboard.html")

def logout_view(request):
    logout(request)
    return redirect("/")