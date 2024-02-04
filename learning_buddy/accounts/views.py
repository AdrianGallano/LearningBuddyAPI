from django.shortcuts import render
from django.urls import reverse
from django.http import (
    HttpResponseRedirect,
    HttpResponsePermanentRedirect,
    HttpResponse,
)
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from .models import User

@login_required
def profile(request):
    context = {"user": request.user}
    
    return render(request, "accounts/profile.html", context)

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {"form": form}
        return render(request, "accounts/register.html", context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("accounts:registration_successful"))
        else:
            return render(request, "accounts/register.html", {"form":form})


class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponsePermanentRedirect(reverse("accounts:profile"))

        form = LoginForm()
        return render(request, "accounts/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user  = User.objects.get(username=request.POST["username"])
            login(request, user)
            return HttpResponseRedirect(reverse("accounts:profile"))

        return render(request, "accounts/login.html", {"form": form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponse("logout successful")

def registration_successful(request):
    return render(request, "accounts/registration_successful.html", {})
