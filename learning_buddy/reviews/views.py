from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.views.generic import ListView, View
from .models import Room, Subject, Category, Topic
from .forms import EditorForm
from docx import Document


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
        subject_filter = self.request.GET.get("filter", False)
        if subject_filter:
            subject = Subject.objects.filter(
                room=self.request.user.reviews_room, name__icontains=subject_filter
            ).order_by("-date_time_modified")
        else:
            subject = Subject.objects.filter(
                room=self.request.user.reviews_room
            ).order_by("-date_time_modified")
        return subject

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_name"] = "Reviews"
        context["user"] = self.request.user
        return context


class SubjectDeleteView(View):
    def get(self, request, subjectId):
        subject = Subject.objects.get(id=subjectId)
        return render(
            request, "reviews/subjects/delete_subject.html", {"subject": subject}
        )

    def post(self, request, subjectId):
        Subject.objects.filter(id=subjectId).delete()
        return HttpResponsePermanentRedirect(
            redirect_to=reverse("reviews:display_subjects")
        )


class SubjectCreateView(View):
    def get(self, request):
        user = request.user
        return render(request, "reviews/subjects/create_subject.html", {"user": user})

    def post(self, request):
        name = request.POST["name"]
        room_id = request.POST["reviews_room_id"]
        room = Room.objects.get(id=room_id)
        Subject.objects.create(name=name, room=room)
        return HttpResponsePermanentRedirect(
            redirect_to=reverse("reviews:display_subjects")
        )


class SubjectEditView(View):
    def get(self, request, subjectId):
        subject = Subject.objects.get(id=subjectId)
        return render(
            request, "reviews/subjects/edit_subject.html", {"subject": subject}
        )

    def put(self, request, subjectId):
        subject = Subject.objects.get(id=subjectId)
        subject.name = request.PUT["name"]
        subject.save()
        return HttpResponsePermanentRedirect(
            redirect_to=reverse("reviews:display_subjects")
        )


class CategoryListView(ListView):
    template_name = "reviews/categorys/display_categorys.html"
    model = Category
    context_object_name = "categorys"
    paginate_by = 10

    def get_queryset(self):
        subject_id = self.kwargs["subjectId"]
        subject = Subject.objects.get(id=subject_id)
        category_filter = self.request.GET.get("filter", False)
        if category_filter:
            category = Category.objects.filter(
                subject=subject, name__icontains=category_filter
            ).order_by("-date_time_modified")
        else:
            category = Category.objects.filter(subject=subject).order_by(
                "-date_time_modified"
            )

        return category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject_id = self.kwargs["subjectId"]
        subject = Subject.objects.get(id=subject_id)

        context["app_name"] = "Categories"
        context["subject"] = subject
        context["user"] = self.request.user
        return context


class CategoryCreateView(View):
    def get(self, request, subjectId):
        subject = Subject.objects.get(id=subjectId)
        return render(
            request, "reviews/categorys/create_category.html", {"subject": subject}
        )

    def post(self, request, subjectId):
        name = request.POST["name"]

        subject = Subject.objects.get(id=subjectId)
        Category.objects.create(name=name, subject=subject)
        return HttpResponsePermanentRedirect(
            redirect_to=reverse(
                "reviews:display_categorys", kwargs={"subjectId": subjectId}
            )
        )


class CategoryDeleteView(View):
    def get(self, request, subjectId, categoryId):
        category = Category.objects.get(id=categoryId)
        subject = Subject.objects.get(id=subjectId)

        return render(
            request,
            "reviews/categorys/delete_category.html",
            {"category": category, "subject": subject},
        )

    def post(self, request, subjectId, categoryId):
        Category.objects.filter(id=categoryId).delete()

        return HttpResponsePermanentRedirect(
            redirect_to=reverse(
                "reviews:display_categorys", kwargs={"subjectId": subjectId}
            )
        )


class CategoryEditView(View):
    def get(self, request, subjectId, categoryId):
        category = Category.objects.get(id=categoryId)
        subject = Subject.objects.get(id=subjectId)

        return render(
            request,
            "reviews/categorys/edit_category.html",
            {"category": category, "subject": subject},
        )

    def post(self, request, subjectId, categoryId):
        category = Category.objects.get(id=categoryId)
        category.name = request.POST["name"]
        category.save()
        return HttpResponsePermanentRedirect(
            redirect_to=reverse(
                "reviews:display_categorys", kwargs={"subjectId": subjectId}
            )
        )


class TopicListView(ListView):
    template_name = "reviews/topics/display_topics.html"
    model = Topic
    context_object_name = "topics"
    paginate_by = 10

    def get_queryset(self):
        category_id = self.kwargs["categoryId"]
        category = Category.objects.get(id=category_id)

        topic_filter = self.request.GET.get("filter", False)
        if topic_filter:
            topic = Topic.objects.filter(
                category=category, name__icontains=topic_filter
            ).order_by("-date_time_modified")
        else:
            topic = Topic.objects.filter(category=category).order_by(
                "-date_time_modified"
            )
        return topic

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject_id = self.kwargs["subjectId"]
        subject = Subject.objects.get(id=subject_id)
        category_id = self.kwargs["categoryId"]
        category = Category.objects.get(id=category_id)

        context["app_name"] = "Topics"
        context["subject"] = subject
        context["category"] = category
        context["user"] = self.request.user
        return context


class TopicCreateView(View):
    def get(self, request, subjectId, categoryId):
        subject = Subject.objects.get(id=subjectId)
        category = Category.objects.get(id=categoryId)
        return render(
            request,
            "reviews/topics/create_topic.html",
            {"subject": subject, "category": category},
        )

    def post(self, request, subjectId, categoryId):
        name = request.POST["name"]

        category = Category.objects.get(id=categoryId)
        Topic.objects.create(name=name, category=category)
        return HttpResponsePermanentRedirect(
            redirect_to=reverse(
                "reviews:display_topics",
                kwargs={"subjectId": subjectId, "categoryId": categoryId},
            )
        )


class TopicDeleteView(View):
    def get(self, request, subjectId, categoryId, topicId):
        category = Category.objects.get(id=categoryId)
        subject = Subject.objects.get(id=subjectId)
        topic = Topic.objects.get(id=topicId)
        return render(
            request,
            "reviews/topics/delete_topic.html",
            {"category": category, "subject": subject, "topic": topic},
        )

    def post(self, request, subjectId, categoryId, topicId):
        Topic.objects.filter(id=topicId).delete()

        return HttpResponsePermanentRedirect(
            redirect_to=reverse(
                "reviews:display_topics",
                kwargs={"subjectId": subjectId, "categoryId": categoryId},
            )
        )


class TopicEditView(View):
    def get(self, request, subjectId, categoryId, topicId):
        category = Category.objects.get(id=categoryId)
        subject = Subject.objects.get(id=subjectId)
        topic = Topic.objects.get(id=topicId)

        return render(
            request,
            "reviews/topics/edit_topic.html",
            {"category": category, "subject": subject, "topic": topic},
        )

    def post(self, request, subjectId, categoryId, topicId):
        topic = Topic.objects.get(id=topicId)
        topic.name = request.POST["name"]
        topic.save()
        return HttpResponsePermanentRedirect(
            redirect_to=reverse(
                "reviews:display_topics",
                kwargs={"subjectId": subjectId, "categoryId": categoryId},
            )
        )


class TopicView(View):
    def get(self, request, subjectId, categoryId, topicId):
        topic = Topic.objects.get(id=topicId)
        
        form_context = {"content":topic.content}
        editor = EditorForm(form_context)
        category = Category.objects.get(id=categoryId)
        subject = Subject.objects.get(id=subjectId)
        topic = Topic.objects.get(id=topicId)

        # document = Document()
        print(editor)
        context = {
            "category": category,
            "subject": subject,
            "topic": topic,
            "editor": editor,
        }
        return render(request, "reviews/topics/topic.html", context=context)
    
    def post(self, request, subjectId, categoryId, topicId):
        topic = Topic.objects.get(id=topicId)
        data = request.POST["content"]
        topic.content = data
        


