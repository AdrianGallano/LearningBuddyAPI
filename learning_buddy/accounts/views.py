from django.shortcuts import render
from django.urls import reverse
from django.http import (
    HttpResponseRedirect,
    HttpResponseBadRequest,
    HttpResponseNotAllowed,
    HttpResponse,
)
from .forms import UserForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from .models import User


def profile(request):
    if request.user.is_anonymous:
        raise HttpResponseNotAllowed

    context = {"user": request.user}

    return render(request, "profile.html", context)


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            password = request.POST["password"]

            User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )

            return HttpResponseRedirect(reverse("accounts:login"))
        else:
            return HttpResponseBadRequest("Bad Request")

    form = UserForm()
    return render(request, "register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("accounts:registration_successful"))

    form = LoginForm()
    return render(request, "login.html", {"form": form})

def user_logout(request):
    logout(request)
    return HttpResponse("logout successful")


def registration_successful(request):
    return render(request, "registration_successful.html", {})
