from django.urls import path
from . import views

urlpatterns = [
    path("notes", views.NoteViewSet.as_view({"get": "list", "post": "create"})),
    path("notes/<int:id>", views.NoteViewSet.as_view({
        "get":"retrieve",
        "put":"update",
        "patch":"partial_update",
        "delete":"destroy",
    })),
    path("note-categories", views.NoteCategoryViewSet.as_view({"get": "list", "post": "create"})),
    path("note-categories/<int:id>", views.NoteCategoryViewSet.as_view({
        "get":"retrieve",
        "put":"update",
        "patch":"partial_update",
        "delete":"destroy",
    })),
]
