from django.contrib import admin
from .models import KontrolClass,AyazIsler,KaravanIs


class AyazIslerAdmin(admin.ModelAdmin):
    list_display = ('is_bilgisi', 'bolum')
    list_filter = ('bolum',)

class KaravanIsAdmin(admin.ModelAdmin):
    list_display = ('karavan', 'is_bilgisi','tamamlandi_mi')
    list_filter = ('karavan',)

class KontrolClassAdmin(admin.ModelAdmin):
    list_display = ('chassis', 'model','date')
    search_fields = ('chassis',)

admin.site.register(AyazIsler,AyazIslerAdmin)
admin.site.register(KontrolClass,KontrolClassAdmin)
admin.site.register(KaravanIs,KaravanIsAdmin)