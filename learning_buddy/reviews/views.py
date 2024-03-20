from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.views.generic import ListView, DeleteView, View
from .models import Room, Subject


def create_room(user):
    if user:
        Room.objects.create(user=user)
        return True 
    
    return False


class ReviewsSubjectsListView(ListView):
    template_name = "reviews/subjects/display_subjects.html"
    model = Subject
    context_object_name = "subjects"
    paginate_by = 10
    
    
    def get_queryset(self):
        return Subject.objects.filter(room=self.request.user.reviews_room).order_by("-date_time_modified")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_name"] = "Reviews" 
        context["user"] = self.request.user 
        return context

class ReviewsSubjectsDeleteView(View):
    def get(self, request, subject_id):
        subject = Subject.objects.get(id=subject_id)
        return render(request, "reviews/subjects/delete_subject.html", {"subject":subject})

    def post(self, request, subject_id):
        Subject.objects.filter(id=subject_id).delete()
        return HttpResponsePermanentRedirect(redirect_to=reverse("reviews:display_subjects"))
    
class ReviewsSubjectCreateView(View):
    def get(self, request):
        user = request.user
        return render(request, "reviews/subjects/create_subject.html", {"user":user})

    def post(self, request):
        name=request.POST["name"]
        room_id=request.POST["reviews_room_id"]
        room = Room.objects.get(id=room_id)
        Subject.objects.create(name=name, room=room)
        return HttpResponsePermanentRedirect(redirect_to=reverse("reviews:display_subjects"))


class ReviewsSubjectEditView(View):
    def get(self, request, subject_id):
        subject = Subject.objects.get(id=subject_id)
        return render(request, "reviews/subjects/edit_subject.html", {"subject":subject})

    def post(self, request, subject_id):
        subject = Subject.objects.get(id=subject_id)
        subject.name = request.POST["name"]
        subject.save()
        return HttpResponsePermanentRedirect(redirect_to=reverse("reviews:display_subjects"))