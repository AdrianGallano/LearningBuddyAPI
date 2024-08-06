from django.shortcuts import render
from rest_framework import viewsets
from .models import Note, NoteCategory
from .serializers import NoteSerializer, NoteCategorySerializer

class NoteViewSet(viewsets.ModelViewSet):
    model = Note
    serializer_class = NoteSerializer 
    queryset = Note.objects.all()

class NoteCategoryViewSet(viewsets.ModelViewSet):
    model = NoteCategory
    serializer_class = NoteCategorySerializer 
    queryset = NoteCategory.objects.all()
