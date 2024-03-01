from django.http import HttpResponse
from .models import KontrolClass
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as user_login

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        kullanici = request.POST["username"]
        sifre = request.POST["password"]
        
        user = authenticate(request,username = kullanici,password = sifre)
        if user is not None:
            user_login(request,user)
            return redirect('home')
        else:
            return render(request,"blog/login.html",{
                "error": "İşlem Başarısız"
            })
    return render(request,"blog/login.html")

def home(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    
    if request.method == "POST":
        date = request.POST.get('date')
        model = request.POST.get('model')
        chassis = request.POST.get('chassis')

        ayaz_models = ['AYAZ SMART',
                       'AYAZ COMFORT',
                       'AYAZ PREMIUM',
                       'AYAZ OFFROAD SMART',
                       'AYAZ OFFROAD COMFORT',
                       'AYAZ OFFROAD PREMIUM',]
        
        arkut_models = ['ARKUT SMART',
                        'ARKUT COMFORT',
                        'ARKUT PREMIUM']
        
        alada_models = ['ALADA PREMIUM',]
        
        gredia_models = ['GREDIA PREMIUM',]

        if model in ayaz_models:
            pass

        if model in arkut_models:
            pass

        if model in alada_models:
            pass

        if model in gredia_models:
            pass

    return render(request,"blog/home.html")

def ayaz(request):
    if request.user.is_authenticated == False:
        return redirect('login')



    return render(request,"blog/ayaz.html")


def exit(request):
    logout(request)
    return redirect("login")