from django.urls import path
from . import views
from .views import RegisterView, LoginView, ProfileView
app_name = "accounts"

urlpatterns = [
    path("profile/", ProfileView.as_view() , name="profile"),
    path("register/", RegisterView.as_view() , name="register"),
    path("registration_successful/",  RegisterView.success , name="registration_successful"),
    path("login/", LoginView.as_view() , name="login"),
    path("logout/", LoginView.user_logout, name="logout"),
]