# Generated by Django 5.0.2 on 2024-03-03 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kontrol', '0005_alter_ayazisler_options_alter_karavanis_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ayazisler',
            name='bolum',
            field=models.CharField(choices=[('ELEKTRİK - SOL ÖN DOLAP', 'ELEKTRİK - SOL ÖN DOLAP'), ('MOBİLYA - SOL ÖN DOLAP', 'MOBİLYA - SOL ÖN DOLAP'), ('MONTAJ - SOL ÖN DOLAP', 'MONTAJ - SOL ÖN DOLAP'), ('ELEKTRİK - SAĞ ÖN DOLAP', 'ELEKTRİK - SAĞ ÖN DOLAP'), ('MOBİLYA - SAĞ ÖN DOLAP', 'MOBİLYA - SAĞ ÖN DOLAP'), ('MONTAJ - SAĞ ÖN DOLAP', 'MONTAJ - SAĞ ÖN DOLAP'), ('MONTAJ - SAĞ KAPI', 'MONTAJ - SAĞ KAPI'), ('MOBİLYA - MUTFAK', 'MOBİLYA - MUTFAK'), ('OFFROAD İÇİN EK DOLAP', 'OFFROAD İÇİN EK DOLAP'), ('OFFROAD İÇİN SU DEPO KAPAĞI', 'OFFROAD İÇİN SU DEPO KAPAĞI'), ('AYAZ İÇİN SU DEPO KAPAKLARI', 'AYAZ İÇİN SU DEPO KAPAKLARI'), ('ELEKTRİK - MUTFAK', 'ELEKTRİK - MUTFAK'), ('MONTAJ - BAGAJ', 'MONTAJ - BAGAJ'), ('MONTAJ - SOL KAPI', 'MONTAJ - SOL KAPI'), ('MOBİLYA - YAŞAM ALANI', 'MOBİLYA - YAŞAM ALANI'), ('MONTAJ - YAŞAM ALANI', 'MONTAJ - YAŞAM ALANI'), ('ELEKTRİK - YAŞAM ALANI', 'ELEKTRİK - YAŞAM ALANI'), ('DÖŞEME', 'DÖŞEME'), ('ELEKTRİK - DIŞ AKSAM', 'ELEKTRİK - DIŞ AKSAM'), ('MONTAJ - DIŞ  AKSAM', 'MONTAJ - DIŞ  AKSAM'), ('DIŞ BOYA', 'DIŞ BOYA')], max_length=50, verbose_name='Kısım'),
        ),
    ]
