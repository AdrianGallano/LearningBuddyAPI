from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import User

current_user = None

def profile(request):
    if current_user == None:
        return HttpResponse("please login")

    context = {
    "id":current_user.id,
    "first_name":current_user.first_name,
    "last_name":current_user.last_name,
    "email":current_user.email,
    "password":current_user.password}

    return render(request, "profile.html", context)


def register(request):
    return render(request, "register.html", {})


def create_user(request):
    context = {}
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        user.save()
        global current_user
        current_user = user
        context = {
            "id":id,
            "first_name":first_name,
            "last_name":last_name,
            "email":email,
            "password":password}
        
    else:
        raise Http404
    
    return render(request, "registration_successful.html", context)
