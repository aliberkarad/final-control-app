from django.http import HttpResponse
from .models import KontrolClass,AyazIsler,KaravanIs
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


    # "AYAZ" modeline sahip tüm karavanları al
    ayazlar = KontrolClass.objects.filter(model__contains="AYAZ")
    ayaz_ve_isleri = {}
    # Her bir "AYAZ" modeli için işleri al ve sözlüğe ekle
    for ayaz in ayazlar:
        #karavan_isleri = KaravanIs.objects.filter(karavan=ayaz,tamamlandi_mi="GEÇTİ")
        karavan_isleri = KaravanIs.objects.filter(karavan=ayaz)
        for karavan_is in karavan_isleri:
            is_bilgisi = karavan_is.is_bilgisi.is_bilgisi
            chassis = ayaz.chassis
            tamamlandi_mi = karavan_is.tamamlandi_mi  # tamamlandi_mi alanına erişim
            # Sözlüğe ekleme
            if chassis in ayaz_ve_isleri:
                ayaz_ve_isleri[chassis].append((is_bilgisi, tamamlandi_mi))
            else:
                ayaz_ve_isleri[chassis] = [(is_bilgisi, tamamlandi_mi)]

    # Modellere göre filtreleme yap
    arkutlar = KontrolClass.objects.filter(model__contains="ARKUT")
    aladalar = KontrolClass.objects.filter(model__contains="ALADA")
    gredialar = KontrolClass.objects.filter(model__contains="GREDIA")

    if request.method == "POST":
        date = request.POST.get('date')
        model = request.POST.get('model')
        chassis = request.POST.get('chassis')

        ayaz = KontrolClass.objects.create(date=date,model=model,chassis=chassis)

        if model in ayaz_models:
            tum_isler = AyazIsler.objects.all()
            for is_bilgisi in tum_isler:
                KaravanIs.objects.create(karavan=ayaz,is_bilgisi=is_bilgisi)
            return render(request,"blog/ayaz.html",{
                'ayaz' : ayaz,
                'ayaz_tum_isler' : tum_isler,
            })

        if model in arkut_models:
            pass

        if model in alada_models:
            pass

        if model in gredia_models:
            pass

    return render(request,"blog/home.html",{ 
        'ayazlar' : ayazlar,
        'ayaz_ve_isleri' : ayaz_ve_isleri,
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