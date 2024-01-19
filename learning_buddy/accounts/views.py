from django.shortcuts import render
from django.urls import reverse
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    HttpResponseBadRequest,
    HttpResponseNotAllowed,
)
from .forms import UserForm
from django.contrib.auth.models import AnonymousUser
from flashcards.models import Room as fRoom
from reviews.models import Room as rRoom
from quizzes.models import Room as qRoom

def profile(request):
    if request.user is AnonymousUser:
        raise HttpResponseNotAllowed

    context = {"user": request.user}

    return render(request, "profile.html", context)


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse("accounts:registration_successful"))
        else:
            return HttpResponseBadRequest("Bad Request")

    form = UserForm()
    return render(request, "register.html", {"form": form})


def login(request):
    return render(request, "login.html", {})


def registration_successful(request):
    return render(request, "registration_successful.html", {})
