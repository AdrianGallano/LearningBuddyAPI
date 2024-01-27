from django.urls import path
from . import views
from .views import RegisterView, LoginView
app_name = "accounts"

urlpatterns = [
    path("profile/", views.profile , name="profile"),
    path("register/", RegisterView.as_view() , name="register"),
    path("registration_successful/", views.registration_successful , name="registration_successful"),
    path("login/", LoginView.as_view() , name="login"),
    path("logout/", views.user_logout , name="logout"),
]