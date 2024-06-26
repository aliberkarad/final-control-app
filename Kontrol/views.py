from datetime import datetime
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponse
from .models import KontrolClass,AyazIsler,KaravanIs
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as user_login
from django.contrib import messages
from django.utils.text import slugify

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
        karavan_isleri = KaravanIs.objects.filter(karavan=ayaz,tamamlandi_mi="KALDI")
        #karavan_isleri = KaravanIs.objects.filter(karavan=ayaz)
        for karavan_is in karavan_isleri:
            is_bilgisi = karavan_is.is_bilgisi.is_bilgisi
            is_bolumu = karavan_is.is_bilgisi.bolum
            is_bilgisi = is_bolumu + " - " + is_bilgisi
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


        
        if model in ayaz_models:
            ayaz = KontrolClass.objects.create(date=my_datetime_aware,model=model,chassis=chassis)
            # Ayaz için geçerli işler alınır
            tum_isler = AyazIsler.objects.all()
            # İş bölümleri için liste oluşturulur
            for is_bilgisi in tum_isler:
                # Ayaz için geçerli işler karavana atanır
                KaravanIs.objects.create(karavan=ayaz,is_bilgisi=is_bilgisi)

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
        # Son oluşturulan karavan alınır
        ayaz = KontrolClass.objects.latest('id')         
        # Ayaz için geçerli işler alınır
        tum_isler = AyazIsler.objects.all()
        # İş bölümleri için liste oluşturulur
        tum_isler_bolum = []
        for is_bilgisi in tum_isler:
            # Ayaz için iş bölümleri tek olarak alınır
            if is_bilgisi.bolum not in tum_isler_bolum:
                tum_isler_bolum.append(is_bilgisi.bolum)

    if request.method == "POST":
        # ayaz şasi bilgisi çekilir
        chassis = request.POST.get('chassis')
        # ayaz iş bilgileri sayfadan liste olarak çekilir
        is_bilgileri_values = request.POST.getlist('isler')
        # şasi bilgisi alınan karavan çekilir
        karavan = KontrolClass.objects.get(chassis=chassis)
        # çekilen karavana ait işler alınır
        karavan_isleri = KaravanIs.objects.filter(karavan=karavan)
        # Her bir işin tamamlandı durumunu güncelle
        for karavan_is in karavan_isleri:
            karavan_is.tamamlandi_mi = request.POST.get(slugify(karavan_is.is_bilgisi.is_bilgisi))
            karavan_is.save()

        # kayıt sonrası ana sayfaya dönülür
        return redirect('home')

    return render(request,"blog/ayaz.html",{
        'ayaz_tum_isler':tum_isler,
        'ayaz_tum_isler_bolum':tum_isler_bolum,
        'ayaz': ayaz,
    })


def exit(request):
    logout(request)
    return redirect("login")