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

    durum_bilgisi =(
        ('KALDI','KALDI'),
        ('GEÇTİ','GEÇTİ'),
    )










    class Meta:
        verbose_name = 'Kontrol'
        verbose_name_plural = 'Kontroller'

    def __str__(self):
        return f"{self.date} - {self.model} - {self.chassis}"