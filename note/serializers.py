from rest_framework import serializers
from .models import Note, NoteCategory


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"


class NoteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteCategory
        fields = "__all__"
