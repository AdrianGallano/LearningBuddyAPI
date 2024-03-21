from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.views.generic import ListView, DeleteView, View
from .models import Room, Subject, Category, Topic, Item


def create_room(user):
    if user:
        Room.objects.create(user=user)
        return True 
    
    return False


class SubjectListView(ListView):
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

class SubjectDeleteView(View):
    def get(self, request, subject_id):
        subject = Subject.objects.get(id=subject_id)
        return render(request, "reviews/subjects/delete_subject.html", {"subject":subject})

    def post(self, request, subject_id):
        Subject.objects.filter(id=subject_id).delete()
        return HttpResponsePermanentRedirect(redirect_to=reverse("reviews:display_subjects"))
    
class SubjectCreateView(View):
    def get(self, request):
        user = request.user
        return render(request, "reviews/subjects/create_subject.html", {"user":user})

    def post(self, request):
        name=request.POST["name"]
        room_id=request.POST["reviews_room_id"]
        room = Room.objects.get(id=room_id)
        Subject.objects.create(name=name, room=room)
        return HttpResponsePermanentRedirect(redirect_to=reverse("reviews:display_subjects"))


class SubjectEditView(View):
    def get(self, request, subject_id):
        subject = Subject.objects.get(id=subject_id)
        return render(request, "reviews/subjects/edit_subject.html", {"subject":subject})

    def post(self, request, subject_id):
        subject = Subject.objects.get(id=subject_id)
        subject.name = request.POST["name"]
        subject.save()
        return HttpResponsePermanentRedirect(redirect_to=reverse("reviews:display_subjects"))


class CategoryListView(ListView):
    template_name = "reviews/categorys/display_categorys.html"
    model = Category
    context_object_name = "categorys"
    paginate_by = 10
    
    
    def get_queryset(self):
        subject_id= self.kwargs["subject_id"]
        subject = Subject.objects.get(id=subject_id)
        return Category.objects.filter(subject=subject).order_by("-date_time_modified")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject_id= self.kwargs["subject_id"]
        subject = Subject.objects.get(id=subject_id)

        context["app_name"] = "Categories" 
        context["subject"] = subject
        context["user"] = self.request.user 
        return context

class CategoryCreateView(View):
    def get(self, request, subject_id):
        subject = Subject.objects.get(id=subject_id)
        return render(request, "reviews/categorys/create_category.html", {"subject":subject})

    def post(self, request, subject_id):
        name=request.POST["name"]

        subject = Subject.objects.get(id=subject_id)
        Category.objects.create(name=name, subject=subject)
        return HttpResponsePermanentRedirect(redirect_to=reverse("reviews:display_categorys", kwargs={"subject_id": subject_id}))

class CategoryDeleteView(View):
    def get(self, request, subject_id, category_id):
        category = Category.objects.get(id=category_id)
        subject = Subject.objects.get(id=subject_id)

        return render(request, "reviews/categorys/delete_category.html", {"category":category, "subject": subject})

    def post(self, request, subject_id, category_id):
        Category.objects.filter(id=category_id).delete()

        return HttpResponsePermanentRedirect(redirect_to=reverse("reviews:display_categorys", kwargs={"subject_id":subject_id}))

class CategoryEditView(View):
    def get(self, request, subject_id, category_id):
        category = Category.objects.get(id=category_id)
        subject = Subject.objects.get(id=subject_id)

        return render(request, "reviews/categorys/edit_category.html", {"category":category, "subject": subject})

    def post(self, request, subject_id, category_id):
        category = Category.objects.get(id=category_id)
        category.name = request.POST["name"]
        category.save()
        return HttpResponsePermanentRedirect(redirect_to=reverse("reviews:display_categorys", kwargs={"subject_id":subject_id}))


class TopicListView(ListView):
    template_name = "reviews/topics/display_topics.html"
    model = Topic
    context_object_name = "topics"
    paginate_by = 10
    
    
    def get_queryset(self):
        category_id= self.kwargs["category_id"]
        category = Category.objects.get(id=category_id)
        return Topic.objects.filter(category=category).order_by("-date_time_modified")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject_id= self.kwargs["subject_id"]
        subject = Subject.objects.get(id=subject_id)
        category_id= self.kwargs["category_id"]
        category = Category.objects.get(id=category_id)

        context["app_name"] = "Topics" 
        context["subject"] = subject
        context["category"] = category
        context["user"] = self.request.user 
        return context

class TopicCreateView(View):
    def get(self, request, subject_id, category_id):
        subject = Subject.objects.get(id=subject_id)
        category = Category.objects.get(id=category_id)
        return render(request, "reviews/topics/create_topic.html", {"subject":subject, "category": category})

    def post(self, request, subject_id, category_id):
        name=request.POST["name"]

        category = Category.objects.get(id=category_id)
        Topic.objects.create(name=name, category=category)
        return HttpResponsePermanentRedirect(redirect_to=reverse("reviews:display_topics", kwargs={"subject_id": subject_id, "category_id": category_id}))

class TopicDeleteView(View):
    def get(self, request, subject_id, category_id, topic_id):
        category = Category.objects.get(id=category_id)
        subject = Subject.objects.get(id=subject_id)
        topic = Topic.objects.get(id=topic_id)
        return render(request, "reviews/topics/delete_topic.html", {"category":category, "subject": subject, "topic": topic})

    def post(self, request, subject_id, category_id, topic_id):
        Topic.objects.filter(id=topic_id).delete()

        return HttpResponsePermanentRedirect(redirect_to=reverse("reviews:display_topics", kwargs={"subject_id":subject_id, "category_id": category_id}))

class TopicEditView(View):
    def get(self, request, subject_id, category_id, topic_id):
        category = Category.objects.get(id=category_id)
        subject = Subject.objects.get(id=subject_id)
        topic = Topic.objects.get(id=topic_id)

        return render(request, "reviews/topics/edit_topic.html", {"category":category, "subject": subject, "topic":topic})

    def post(self, request, subject_id, category_id, topic_id):
        topic = Topic.objects.get(id=topic_id)
        topic.name = request.POST["name"]
        topic.save()
        return HttpResponsePermanentRedirect(redirect_to=reverse("reviews:display_topics", kwargs={"subject_id":subject_id, "category_id": category_id}))