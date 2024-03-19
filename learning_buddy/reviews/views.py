from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DeleteView
from .models import Room, Subject


def create_room(user):
    if user:
        Room.objects.create(user=user)
        return True 
    
    return False


class ReviewsSubjectsListView(ListView):
    template_name = "reviews/display_subjects.html"
    model = Subject
    context_object_name = "subjects"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_name"] = "Reviews" 
        context["user"] = self.request.user 
        return context

class ReviewSubjectsDeleteView(DeleteView):
    pass