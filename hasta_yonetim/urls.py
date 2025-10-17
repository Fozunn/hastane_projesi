from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ana_sayfa'),
    path('bolumlerimiz/', views.bolumlerimiz, name='bolumlerimiz'),
    path('doktorlarimiz/', views.doktorlarimiz, name='doktorlarimiz'),
    path('iletisim/', views.iletisim, name='iletisim'),
]