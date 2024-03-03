# Generated by Django 5.0.2 on 2024-03-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kontrol', '0004_ayazisler_bolum'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ayazisler',
            options={'ordering': ['id'], 'verbose_name': 'Ayaz İş', 'verbose_name_plural': '2-Ayaz İşler'},
        ),
        migrations.AlterModelOptions(
            name='karavanis',
            options={'verbose_name': 'Şasi-İş', 'verbose_name_plural': '3-Şasi-İş'},
        ),
        migrations.AlterModelOptions(
            name='kontrolclass',
            options={'verbose_name': 'Kontrol', 'verbose_name_plural': '1-Kontroller'},
        ),
        migrations.AlterField(
            model_name='ayazisler',
            name='bolum',
            field=models.CharField(choices=[('1', 'ELEKTRİK - SOL ÖN DOLAP'), ('2', 'MOBİLYA - SOL ÖN DOLAP'), ('3', 'MONTAJ - SOL ÖN DOLAP'), ('4', 'ELEKTRİK - SAĞ ÖN DOLAP'), ('5', 'MOBİLYA - SAĞ ÖN DOLAP'), ('6', 'MONTAJ - SAĞ ÖN DOLAP'), ('7', 'MONTAJ - SAĞ KAPI'), ('8', 'MOBİLYA - MUTFAK'), ('9', 'OFFROAD İÇİN EK DOLAP'), ('10', 'MOBİLYA - MUTFAK'), ('11', 'OFFROAD İÇİN SU DEPO KAPAĞI'), ('12', 'AYAZ İÇİN SU DEPO KAPAKLARI'), ('13', 'ELEKTRİK - MUTFAK'), ('14', 'MONTAJ - BAGAJ'), ('15', 'MONTAJ - SOL KAPI'), ('16', 'MOBİLYA - YAŞAM ALANI'), ('17', 'MONTAJ - YAŞAM ALANI'), ('18', 'ELEKTRİK - YAŞAM ALANI'), ('19', 'DÖŞEME'), ('20', 'ELEKTRİK - DIŞ AKSAM'), ('21', 'MONTAJ - DIŞ  AKSAM'), ('22', 'DIŞ BOYA')], max_length=20, verbose_name='Kısım'),
        ),
    ]
