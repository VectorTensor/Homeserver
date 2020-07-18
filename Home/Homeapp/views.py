from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request,"Homeapp/index.html")

def login(request):
    return HttpResponse("Login")

def logout(request):
    return HttpResponse("logout")
