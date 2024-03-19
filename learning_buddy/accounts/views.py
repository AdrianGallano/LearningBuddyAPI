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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import User
from flashcards.views import create_room as create_flashcards_room
from reviews.views import create_room as create_reviews_room
from quizzes.views import create_room as create_quizzes_room
from django.core.exceptions import BadRequest

class ProfileView(LoginRequiredMixin ,View):
    def get(self, request):
        context = {"user": request.user}
        
        return render(request, "accounts/profile.html", context)

class RoomView(View):

    @staticmethod
    def create_user_rooms(user):
        is_flashcard_room_created = create_flashcards_room(user)
        is_reviews_room_created = create_reviews_room(user)
        is_quizzes_room_created = create_quizzes_room(user)
        
        if not (is_flashcard_room_created and is_reviews_room_created and is_quizzes_room_created):
            return False
        return True


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponsePermanentRedirect(reverse("dashboard_app:dashboard"))
        
        form = RegisterForm()
        context = {"form": form}
        return render(request, "accounts/register.html", context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            is_room_created = RoomView.create_user_rooms(user)

            if not is_room_created:
                raise BadRequest

            return HttpResponseRedirect(reverse("accounts:registration_successful"))
        else:
            return render(request, "accounts/register.html", {"form":form})
        
    @staticmethod
    def success(request):
        if request.user.is_authenticated:
            return HttpResponsePermanentRedirect(reverse("dashboard_app:dashboard"))
        
        return render(request, "accounts/registration_successful.html", {})

class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponsePermanentRedirect(reverse("dashboard_app:dashboard"))

        form = LoginForm()
        return render(request, "accounts/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user  = User.objects.get(username=request.POST["username"])
            login(request, user)
            return HttpResponseRedirect(reverse("dashboard_app:dashboard"))

        return render(request, "accounts/login.html", {"form": form})
    
    @staticmethod
    def user_logout(request):
        logout(request)
        return HttpResponsePermanentRedirect(reverse("accounts:login"))



