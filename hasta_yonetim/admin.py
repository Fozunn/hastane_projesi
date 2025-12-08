from django.contrib import admin
from .models import IletisimMesaji
from .models import Doktor

@admin.register(IletisimMesaji)
class IletisimMesajiAdmin(admin.ModelAdmin):
    list_display = ['ad_soyad', 'telefon', 'email', 'konu', 'durum', 'olusturma_tarihi']
    list_filter = ['durum', 'konu', 'olusturma_tarihi']
    search_fields = ['ad_soyad', 'email', 'telefon', 'mesaj']
    readonly_fields = ['olusturma_tarihi', 'guncelleme_tarihi']
    list_editable = ['durum']
    
    fieldsets = (
        ('Kişi Bilgileri', {
            'fields': ('ad_soyad', 'telefon', 'email')
        }),
        ('Mesaj Detayları', {
            'fields': ('konu', 'mesaj', 'durum')
        }),
        ('Admin İşlemleri', {
            'fields': ('admin_notu',)
        }),
        ('Zaman Bilgileri', {
            'fields': ('olusturma_tarihi', 'guncelleme_tarihi'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mesaj_okundu_isaretle', 'mesaj_yanitlandi_isaretle']
    
    def mesaj_okundu_isaretle(self, request, queryset):
        updated = queryset.update(durum='okundu')
        self.message_user(request, f'{updated} mesaj okundu olarak işaretlendi.')
    mesaj_okundu_isaretle.short_description = "Seçili mesajları okundu olarak işaretle"
    
    def mesaj_yanitlandi_isaretle(self, request, queryset):
        updated = queryset.update(durum='yanıtlandı')
        self.message_user(request, f'{updated} mesaj yanıtlandı olarak işaretlendi.')
    mesaj_yanitlandi_isaretle.short_description = "Seçili mesajları yanıtlandı olarak işaretle"


@admin.register(Doktor)
class DoktorAdmin(admin.ModelAdmin):
    list_display = ['ad_soyad', 'unvan', 'bolum', 'aktif', 'sira']
    list_filter = ['bolum', 'aktif']
    search_fields = ['ad_soyad', 'unvan']
    ordering = ['sira', 'ad_soyad']
    list_editable = ['aktif', 'sira']
    fieldsets = (
        (None, {
            'fields': ('ad_soyad', 'unvan', 'bolum', 'bio')
        }),
        ('Medya ve Sıra', {
            'fields': ('foto', 'sira', 'aktif')
        }),
        ('Zaman Bilgileri', {
            'fields': ('olusturma_tarihi', 'guncelleme_tarihi'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('olusturma_tarihi', 'guncelleme_tarihi')
