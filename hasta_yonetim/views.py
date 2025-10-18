from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import IletisimFormu
from .models import Doktor

def index(request):
    return render(request, 'hasta_yonetim/ana_sayfa.html')

def bolumlerimiz(request):
    return render(request, 'hasta_yonetim/bolumlerimiz.html')

def doktorlarimiz(request):
    doktorlar = Doktor.objects.filter(aktif=True).order_by('sira', 'ad_soyad')
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

            # Gönderilen iletiyi development ortamında test amaçlı e-posta olarak gönder (console backend).
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

                # Öncelikle settings.CONTACT_RECIPIENTS kontrol et (tekil veya virgülle ayrılmış bir string olarak settings'te tanımlı olabilir)
                recipient_list = getattr(settings, 'CONTACT_RECIPIENTS', None) or []
                # Eğer tekil string olarak gelmişse (ör. 'a@b.com') listeye çevir
                if isinstance(recipient_list, str):
                    recipient_list = recipient_list.split(',')

                # Eğer hala boşsa ADMINS'e, sonra DEFAULT_FROM_EMAIL'e düş
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
                # E-posta gönderimi başarısız olursa bile kullanıcı akışı etkilenmesin; admin panelinden mesaj mevcut.
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
