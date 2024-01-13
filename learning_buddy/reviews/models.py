from django.db import models
from accounts.models import User


class ReviewRoom(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class ReviewSubject(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    room = models.ForeignKey(ReviewRoom, on_delete=models.CASCADE)


class ReviewCategory(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=50)
    subject = models.ForeignKey(ReviewSubject, on_delete=models.CASCADE)


class ReviewTopic(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(ReviewCategory, on_delete=models.CASCADE)


class ReviewItem(models.Model):
    id = models.UUIDField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()
    topic = models.ForeignKey(ReviewTopic, on_delete=models.CASCADE)
