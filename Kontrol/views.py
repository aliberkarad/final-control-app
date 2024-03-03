from datetime import datetime
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponse
from .models import KontrolClass,AyazIsler,KaravanIs
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as user_login
from django.contrib import messages

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
        #karavan_isleri = KaravanIs.objects.filter(karavan=ayaz,tamamlandi_mi="KALDI")  !!!
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
        date_str = request.POST.get('date')  # Formdan gelen tarih ve zaman bilgisi
        my_datetime = datetime.strptime(date_str, '%Y-%m-%dT%H:%M')  # Tarih ve zaman nesnesine dönüştürme
        my_datetime_aware = timezone.make_aware(my_datetime, timezone=timezone.get_current_timezone())  # Zaman dilimini belirleme
        model = request.POST.get('model')
        chassis = request.POST.get('chassis').upper()

        ayaz = KontrolClass.objects.create(date=my_datetime_aware,model=model,chassis=chassis)

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
        'ayaz_ve_isleri' : ayaz_ve_isleri,
        'arkutlar' : arkutlar,
        'aladalar' : aladalar,
        'gredialar' : gredialar,
    })

def ayaz(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    
    if request.method == "GET":
        ayaz = KontrolClass.objects.latest('id')
        tum_isler = AyazIsler.objects.all()
        tum_isler_bolum = set()
        for is_bilgisi in tum_isler:
            tum_isler_bolum.add(is_bilgisi.bolum)
            KaravanIs.objects.create(karavan=ayaz,is_bilgisi=is_bilgisi)

    if request.method == "POST":
        chassis = request.POST.get('chassis')
        is_bilgileri_values = request.POST.getlist('isler')

        karavan = KontrolClass.objects.get(chassis=chassis)
        karavan_isleri = KaravanIs.objects.filter(karavan=karavan)

        # Her bir işin tamamlandı durumunu güncelle
        for karavan_is, is_bilgi_value in zip(karavan_isleri, is_bilgileri_values):
            karavan_is.tamamlandi_mi = is_bilgi_value
            karavan_is.save()
        return redirect('home')

    return render(request,"blog/ayaz.html",{
        'ayaz_tum_isler':tum_isler,
        'ayaz_tum_isler_bolum':tum_isler_bolum,
        'ayaz': ayaz,
    })


def exit(request):
    logout(request)
    return redirect("login")