from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("profile/", views.profile , name="profile"),
    path("register/", views.register , name="register"),
    path("create/", views.create , name="create"),
]