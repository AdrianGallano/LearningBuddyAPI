from django.http import HttpResponsePermanentRedirect, HttpResponse
from django.urls import reverse

def index(request):
    if request.user.is_authenticated:
        return HttpResponsePermanentRedirect(redirect_to=reverse("dashboard_app:dashboard"))
    else:
        return HttpResponsePermanentRedirect(redirect_to=reverse("accounts:login"))
