from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

def index(request):
    return HttpResponse("Reviews")

def create_room(user):
    if user:
        Room.objects.create(user=user)
        return True 
    
    return False