from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from .models import Message
from django.forms.models import model_to_dict

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.method == "POST":
        g_message=request.POST["message"]
        g_user= request.user.username
        d_message=Message.objects.create(message_text=g_message,sender=g_user)

    return render(request,"Homeapp/index.html")

def login_view(request):
    if request.method=="POST":
        username=request.POST["username"]
        password= request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request , user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"Homeapp/login.html",{
                "message":"Invalid credentials"
            })    
    return render(request, "Homeapp/login.html")

def logout_view(request):
    logout(request)
    return render(request,"Homeapp/login.html",{
        "message":"Logged out"
    })

def get_Message(request):
    if not request.user.is_authenticated:
        return HttpResponse("Can't send data")
    messages=[]; 
    users=[];   
    for i_message in Message.objects.all():
        messages.append(i_message.message_text)
        users.append(i_message.sender)
        
    return JsonResponse({
        "message":messages,
        "user":users
    })    

