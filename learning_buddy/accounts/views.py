from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from .models import User
from .forms import UserForm

g_user = None

def profile(request):
    if g_user == None:
        return HttpResponse("please login")

    context = {"user": g_user}

    return render(request, "profile.html", context)


def register(request):
    template = "register.html"
    form = UserForm()
    context = {"form": form}
    return render(request, template, context)


def create(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )

            global g_user
            g_user = user
            context = {"user": user}
        else:
            return HttpResponseBadRequest("BAD REQUEST")
    else:
        raise Http404

    return render(request, "registration_successful.html", context)
