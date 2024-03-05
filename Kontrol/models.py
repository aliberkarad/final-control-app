from django.db import models

# Create your models here.
class KontrolClass(models.Model):

    date = models.DateTimeField(verbose_name="Tarih")

    chassis = models.CharField(max_length=17,unique=True,blank=False,verbose_name="Şasi No")
    
    #Model bilgisi
    caravan_models = (
        ('---','Boş'),
        ('AYAZ SMART','Ayaz Smart'),
        ('AYAZ COMFORT','Ayaz Comfort'),
        ('AYAZ PREMIUM','Ayaz Premium'),
        ('AYAZ OFFROAD SMART','Ayaz OffRoad Smart'),
        ('AYAZ OFFROAD COMFORT','Ayaz OffRoad Comfort'),
        ('AYAZ OFFROAD PREMIUM','Ayaz OffRoad Premium'),
        ('ARKUT SMART','Arkut Smart'),
        ('ARKUT COMFORT','Arkut Comfort'),
        ('ARKUT PREMIUM','Arkut Premium'),
        ('ALADA PREMIUM','Alada Premium'),
        ('GREDIA PREMIUM','Gredia Premium'),
    )
    model = models.CharField(max_length=100,default="---",choices=caravan_models,verbose_name="Model")

    class Meta:
        verbose_name = 'Kontrol'
        verbose_name_plural = '1-Kontroller'

    def __str__(self):
        return f"{self.chassis} - {self.model}"
    

class AyazIsler(models.Model):
    is_bilgisi = models.CharField(max_length=400,verbose_name='İş Bilgisi')
    karavanlar = models.ManyToManyField(KontrolClass,through='KaravanIs')

    bolumler = (
        ('ELEKTRİK - SOL ÖN DOLAP','ELEKTRİK - SOL ÖN DOLAP'),
        ('MOBİLYA - SOL ÖN DOLAP','MOBİLYA - SOL ÖN DOLAP'),
        ('MONTAJ - SOL ÖN DOLAP','MONTAJ - SOL ÖN DOLAP'),
        ('ELEKTRİK - SAĞ ÖN DOLAP','ELEKTRİK - SAĞ ÖN DOLAP'),
        ('MOBİLYA - SAĞ ÖN DOLAP','MOBİLYA - SAĞ ÖN DOLAP'),
        ('MONTAJ - SAĞ ÖN DOLAP','MONTAJ - SAĞ ÖN DOLAP'),
        ('MONTAJ - SAĞ KAPI','MONTAJ - SAĞ KAPI'),
        ('MOBİLYA - MUTFAK','MOBİLYA - MUTFAK'),
        ('OFFROAD İÇİN EK DOLAP','OFFROAD İÇİN EK DOLAP'),
        ('OFFROAD İÇİN SU DEPO KAPAĞI','OFFROAD İÇİN SU DEPO KAPAĞI'),
        ('AYAZ İÇİN SU DEPO KAPAKLARI','AYAZ İÇİN SU DEPO KAPAKLARI'),
        ('ELEKTRİK - MUTFAK','ELEKTRİK - MUTFAK'),
        ('MONTAJ - BAGAJ','MONTAJ - BAGAJ'),
        ('MONTAJ - SOL KAPI','MONTAJ - SOL KAPI'),
        ('MOBİLYA - YAŞAM ALANI','MOBİLYA - YAŞAM ALANI'),
        ('MONTAJ - YAŞAM ALANI','MONTAJ - YAŞAM ALANI'),
        ('ELEKTRİK - YAŞAM ALANI','ELEKTRİK - YAŞAM ALANI'),
        ('DÖŞEME','DÖŞEME'),
        ('ELEKTRİK - DIŞ AKSAM','ELEKTRİK - DIŞ AKSAM'),
        ('MONTAJ - DIŞ  AKSAM','MONTAJ - DIŞ  AKSAM'),
        ('DIŞ BOYA','DIŞ BOYA'),
    )

    bolum = models.CharField(max_length=50,choices=bolumler,blank=False,verbose_name="Kısım")

    class Meta:
        verbose_name = 'Ayaz İş'
        verbose_name_plural = '2-Ayaz İşler'
        ordering = ['id']

    def __str__(self):
        return f"{self.is_bilgisi} - {self.bolum}"

class KaravanIs(models.Model):
    durum_bilgisi =(
        ('KALDI','KALDI'),
        ('GEÇTİ','GEÇTİ'),
    )
    karavan = models.ForeignKey(KontrolClass, on_delete=models.CASCADE,verbose_name="Karavan")
    is_bilgisi = models.ForeignKey(AyazIsler, on_delete=models.CASCADE,verbose_name="İş Bilgisi")
    tamamlandi_mi = models.CharField(max_length=20,default='KALDI',choices=durum_bilgisi,verbose_name='Durum')

    class Meta:
        unique_together = (('karavan', 'is_bilgisi'),)
        verbose_name = 'Şasi-İş'
        verbose_name_plural = '3-Şasi-İş'
    
    def __str__(self):
        return f"{self.karavan} - {self.is_bilgisi}"