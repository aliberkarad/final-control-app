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

    ayazlar = KontrolClass.objects.filter(model__contains="AYAZ")
    arkutlar = KontrolClass.objects.filter(model__contains="ARKUT")
    aladalar = KontrolClass.objects.filter(model__contains="ALADA")
    gredialar = KontrolClass.objects.filter(model__contains="GREDIA")

    if request.method == "POST":
        date = request.POST.get('date')
        model = request.POST.get('model')
        chassis = request.POST.get('chassis')

        caravan = KontrolClass.objects.create(date=date,model=model,chassis=chassis)

        if model in ayaz_models:
            return redirect('ayaz')

        if model in arkut_models:
            pass

        if model in alada_models:
            pass

        if model in gredia_models:
            pass

    return render(request,"blog/home.html",{ 
        'ayazlar' : ayazlar,
        'arkutlar' : arkutlar,
        'aladalar' : aladalar,
        'gredialar' : gredialar,
    })

def ayaz(request):
    if request.user.is_authenticated == False:
        return redirect('login')



    return render(request,"blog/ayaz.html")


def exit(request):
    logout(request)
    return redirect("login")