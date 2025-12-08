from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ana_sayfa'),
    path('bolumlerimiz/', views.bolumlerimiz, name='bolumlerimiz'),
    path('doktorlarimiz/', views.doktorlarimiz, name='doktorlarimiz'),
    path('iletisim/', views.iletisim, name='iletisim'),
    
    # Doktor Yönetimi
    path('doktor-yonetimi/', views.doktor_listesi, name='doktor_listesi'),
    path('doktor-ekle/', views.doktor_ekle, name='doktor_ekle'),
    path('doktor-duzenle/<int:id>/', views.doktor_duzenle, name='doktor_duzenle'),
    path('doktor-sil/<int:id>/', views.doktor_sil, name='doktor_sil'),
    path('doktor-foto-sil/<int:id>/', views.doktor_foto_sil, name='doktor_foto_sil'),
    
    # Doktor Detay (Ziyaretçiler için)
    path('doktor/<int:id>/', views.doktor_detay, name='doktor_detay'),
]