from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("profile/", views.profile , name="profile"),
    path("register/", views.register , name="register"),
    path("registration_successful/", views.registration_successful , name="registration_successful"),
    path("login/", views.login , name="login"),
]