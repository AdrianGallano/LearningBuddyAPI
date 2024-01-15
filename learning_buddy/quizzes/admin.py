from django.contrib import admin
from .models import Room, Subject, Category, Topic, Item, FakeAnswer

admin.site.register(Room)
admin.site.register(Subject)
admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Item)
admin.site.register(FakeAnswer)