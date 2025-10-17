from django.db import models
from django.utils import timezone

# İletişim Mesajları Modeli
class IletisimMesaji(models.Model):
    KONU_SECENEKLERI = [
        ('randevu', 'Randevu Talebi'),
        ('bilgi', 'Genel Bilgi'),
        ('sikayet', 'Şikayet'),
        ('oneri', 'Öneri'),
        ('diger', 'Diğer'),
    ]
    
    DURUM_SECENEKLERI = [
        ('yeni', 'Yeni'),
        ('okundu', 'Okundu'),
        ('yanıtlandı', 'Yanıtlandı'),
        ('kapandı', 'Kapandı'),
    ]
    
    ad_soyad = models.CharField(max_length=100, verbose_name="Ad Soyad")
    telefon = models.CharField(max_length=15, verbose_name="Telefon")
    email = models.EmailField(verbose_name="E-Mail")
    konu = models.CharField(max_length=20, choices=KONU_SECENEKLERI, verbose_name="Konu")
    mesaj = models.TextField(verbose_name="Mesaj")
    durum = models.CharField(max_length=20, choices=DURUM_SECENEKLERI, default='yeni', verbose_name="Durum")
    olusturma_tarihi = models.DateTimeField(default=timezone.now, verbose_name="Oluşturma Tarihi")
    guncelleme_tarihi = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")
    admin_notu = models.TextField(blank=True, null=True, verbose_name="Admin Notu")
    
    class Meta:
        verbose_name = "İletişim Mesajı"
        verbose_name_plural = "İletişim Mesajları"
        ordering = ['-olusturma_tarihi']
    
    def __str__(self):
        return f"{self.ad_soyad} - {self.get_konu_display()}"
    
    @property
    def kisa_mesaj(self):
        return self.mesaj[:50] + "..." if len(self.mesaj) > 50 else self.mesaj
