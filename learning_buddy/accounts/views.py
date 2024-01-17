from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from .forms import UserForm

g_user = None


def profile(request):
    if g_user == None:
        return HttpResponse(f"please <a href='{reverse('accounts:login')}'>log in</a>")

    context = {"user": g_user}

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