from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from .forms import UserForm

g_user = None


def profile(request):
    if g_user == None:
        return HttpResponse("please login")

    context = {"user": g_user}

    return render(request, "profile.html", context)


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()

            return render(request, "registration_successful.html", {})
        else:
            return HttpResponseBadRequest("Bad Request")

    form = UserForm()
    return render(request, "register.html", {"form": form})


def login(request):
    return render(request, "login.html", {})
