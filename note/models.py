from django.db import models
from django.contrib.auth.models import User


class NoteCategory(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=255, blank=False, null=True)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    note_category_id = models.ForeignKey(NoteCategory, on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
