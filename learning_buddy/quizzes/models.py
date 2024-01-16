from django.db import models
from accounts.models import User
import uuid


class Room(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="quizzes_room")

    def __str__(self):
        return f"{str(self.id)} - {self.user.first_name} {self.user.last_name}"


class Subject(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Topic(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_modified = models.DateTimeField(auto_now=True)
    score = models.IntegerField()
    number_of_items = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FakeAnswer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    answer = models.TextField()

    def __str__(self):
        return self.answer

class Item(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    question = models.TextField()
    answer = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    fake_answers = models.ManyToManyField(FakeAnswer)

    def __str__(self):
        return self.answer