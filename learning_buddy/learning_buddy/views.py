from django.http import HttpResponsePermanentRedirect
from django.urls import reverse

def index(request):
    return HttpResponsePermanentRedirect(redirect_to=reverse("accounts:login"))