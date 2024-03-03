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
        verbose_name_plural = 'Kontroller'

    def __str__(self):
        return f"{self.chassis} - {self.model} - {self.date}"
    

class AyazIsler(models.Model):
    is_bilgisi = models.CharField(max_length=400,verbose_name='İş Bilgisi')
    karavanlar = models.ManyToManyField(KontrolClass,through='KaravanIs')
    bolum = models.CharField(max_length=20,blank=False,verbose_name="Kısım")

    class Meta:
        verbose_name = 'Ayaz İş'
        verbose_name_plural = 'Ayaz İşler'

    def __str__(self):
        return f"{self.is_bilgisi}"

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
        verbose_name = 'Karavan-İş'
        verbose_name_plural = 'Karavan-İş Tümü'
    
    def __str__(self):
        return f"{self.karavan} - {self.is_bilgisi}"