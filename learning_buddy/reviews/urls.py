from django.urls import path
from . import views
from .views import ReviewsSubjectsListView
app_name = "reviews"

urlpatterns = [
    path("", ReviewsSubjectsListView.as_view(), name="display_subject"),
]