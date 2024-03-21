from django.urls import path
from . import views
from .views import SubjectListView, SubjectDeleteView, SubjectCreateView, SubjectEditView, CategoryListView, CategoryCreateView, CategoryDeleteView, CategoryEditView, TopicListView, TopicCreateView, TopicDeleteView, TopicEditView
app_name = "reviews"
urlpatterns = [
    path("subject/", SubjectListView.as_view(), name="display_subjects"),
    path("subject/create/", SubjectCreateView.as_view(), name="create_subject"),
    path("subject/edit/<uuid:subject_id>/", SubjectEditView.as_view(), name="edit_subject"),
    path("subject/delete/<uuid:subject_id>/", SubjectDeleteView.as_view(), name="delete_subject"),
    path("subject/<uuid:subject_id>/category/", CategoryListView.as_view(), name="display_categorys"),
    path("subject/<uuid:subject_id>/category/create/", CategoryCreateView.as_view(), name="create_category"),
    path("subject/<uuid:subject_id>/category/edit/<uuid:category_id>/", CategoryEditView.as_view(), name="edit_category"),
    path("subject/<uuid:subject_id>/category/delete/<uuid:category_id>/", CategoryDeleteView.as_view(), name="delete_category"),
    path("subject/<uuid:subject_id>/category/<uuid:category_id>/topic", TopicListView.as_view(), name="display_topics"),
    path("subject/<uuid:subject_id>/category/<uuid:category_id>/topic/create/", TopicCreateView.as_view(), name="create_topic"),
    path("subject/<uuid:subject_id>/category/<uuid:category_id>/topic/edit/<uuid:topic_id>/", TopicEditView.as_view(), name="edit_topic"),
    path("subject/<uuid:subject_id>/category/<uuid:category_id>/topic/delete/<uuid:topic_id>/", TopicDeleteView.as_view(), name="delete_topic"),
]
