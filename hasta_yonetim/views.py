from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import IletisimFormu, DoktorForm
from .models import Doktor

def index(request):
    return render(request, 'hasta_yonetim/ana_sayfa.html')

def bolumlerimiz(request):
    return render(request, 'hasta_yonetim/bolumlerimiz.html')

def doktorlarimiz(request):
    doktorlar = Doktor.objects.all().order_by('sira', 'ad_soyad')
    context = {
        'doktorlar': doktorlar
    }
    return render(request, 'hasta_yonetim/doktorlarimiz.html', context)

def iletisim(request):
    if request.method == 'POST':
        form = IletisimFormu(request.POST)
        if form.is_valid():
            iletisim = form.save()
            messages.success(request, 'Mesajınız alındı. En kısa sürede size dönüş yapılacaktır.')

            try:
                subject = f"Yeni iletişim mesajı: {iletisim.konu or 'Konu yok'}"
                body_lines = [
                    f"Gönderen: {iletisim.ad_soyad}",
                    f"E‑posta: {iletisim.email}",
                    f"Telefon: {iletisim.telefon}",
                    "",
                    "Mesaj:",
                    iletisim.mesaj or "(boş)"
                ]
                message_body = "\n".join(body_lines)

                recipient_list = getattr(settings, 'CONTACT_RECIPIENTS', None) or []
                if isinstance(recipient_list, str):
                    recipient_list = recipient_list.split(',')

                if not recipient_list:
                    if hasattr(settings, 'ADMINS') and settings.ADMINS:
                        recipient_list = [email for _, email in settings.ADMINS]
                    else:
                        recipient_list = [getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@example.com')]

                send_mail(subject=subject,
                          message=message_body,
                          from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', None),
                          recipient_list=recipient_list,
                          fail_silently=False)
            except Exception:
                pass
            return redirect('iletisim')
        else:
            messages.error(request, 'Lütfen formu doğru şekilde doldurun.')
    else:
        form = IletisimFormu()
    
    context = {
        'form': form
    }
    return render(request, 'hasta_yonetim/iletisim.html', context)

def doktor_listesi(request):
    doktorlar = Doktor.objects.all().order_by('sira', 'ad_soyad')
    return render(request, 'hasta_yonetim/doktor_listesi.html', {'doktorlar': doktorlar})


def doktor_ekle(request):
    form = DoktorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Doktor başarıyla eklendi.')
        return redirect('doktor_listesi')
    return render(request, 'hasta_yonetim/doktor_form.html', {'form': form, 'islem': 'Ekle'})


def doktor_duzenle(request, id):
    doktor = get_object_or_404(Doktor, id=id)
    form = DoktorForm(request.POST or None, request.FILES or None, instance=doktor)
    if form.is_valid():
        form.save()
        messages.success(request, 'Doktor bilgileri başarıyla güncellendi.')
        return redirect('doktor_listesi')
    return render(request, 'hasta_yonetim/doktor_form.html', {'form': form, 'doktor': doktor, 'islem': 'Düzenle'})


def doktor_sil(request, id):
    doktor = get_object_or_404(Doktor, id=id)
    if request.method == "POST":
        doktor.delete()
        messages.success(request, 'Doktor başarıyla silindi.')
        return redirect('doktor_listesi')
    return render(request, 'hasta_yonetim/doktor_sil.html', {'doktor': doktor})


def doktor_detay(request, id):
    """Doktor detay sayfası (ziyaretçiler için)"""
    doktor = get_object_or_404(Doktor, id=id)
    
    ilgili_doktorlar = Doktor.objects.filter(
        bolum=doktor.bolum
    ).exclude(id=doktor.id)[:3] 
    
    context = {
        'doktor': doktor,
        'ilgili_doktorlar': ilgili_doktorlar
    }
    return render(request, 'hasta_yonetim/doktor_detay.html', context)
