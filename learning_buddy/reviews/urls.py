from django.urls import path
from . import views
from .views import SubjectListView, SubjectDeleteView, SubjectCreateView, SubjectEditView, CategoryListView, CategoryCreateView, CategoryDeleteView, CategoryEditView, TopicListView, TopicCreateView, TopicDeleteView, TopicEditView, TopicView
app_name = "reviews"
urlpatterns = [
    path("subjects", SubjectListView.as_view(), name="display_subjects"),
    path("subjects/create", SubjectCreateView.as_view(), name="create_subject"),
    path("subjects/<uuid:subjectId>/edit", SubjectEditView.as_view(), name="edit_subject"),
    path("subjects/<uuid:subjectId>/delete", SubjectDeleteView.as_view(), name="delete_subject"),
    path("subjects/<uuid:subjectId>/categories", CategoryListView.as_view(), name="display_categorys"),
    path("subjects/<uuid:subjectId>/categories/create", CategoryCreateView.as_view(), name="create_category"),
    path("subjects/<uuid:subjectId>/categories/<uuid:categoryId>/edit", CategoryEditView.as_view(), name="edit_category"),
    path("subjects/<uuid:subjectId>/categories/<uuid:categoryId>/delete", CategoryDeleteView.as_view(), name="delete_category"),
    path("subjects/<uuid:subjectId>/categories/<uuid:categoryId>/topics", TopicListView.as_view(), name="display_topics"),
    path("subjects/<uuid:subjectId>/categories/<uuid:categoryId>/topics/create", TopicCreateView.as_view(), name="create_topic"),
    path("subjects/<uuid:subjectId>/categories/<uuid:categoryId>/topics/<uuid:topicId>/edit", TopicEditView.as_view(), name="edit_topic"),
    path("subjects/<uuid:subjectId>/categories/<uuid:categoryId>/topics/<uuid:topicId>/delete", TopicDeleteView.as_view(), name="delete_topic"),
    path("subjects/<uuid:subjectId>/categories/<uuid:categoryId>/topics/<uuid:topicId>", TopicView.as_view(), name="topic"),
]
