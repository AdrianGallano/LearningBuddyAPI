from django.urls import path
from . import views
from .views import ReviewsSubjectsListView, ReviewsSubjectsDeleteView, ReviewsSubjectCreateView
app_name = "reviews"

urlpatterns = [
    path("subjects/", ReviewsSubjectsListView.as_view(), name="display_subjects"),
    path("create_subject/", ReviewsSubjectCreateView.as_view(), name="create_subject"),
    path("delete_subject/<uuid:subject_id>", ReviewsSubjectsDeleteView.as_view(), name="delete_subject"),
]