from django.urls import path
from . import views

app_name = "dashboard_app"

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
]