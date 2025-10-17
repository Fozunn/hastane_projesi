from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import IletisimFormu

def index(request):
    return render(request, 'hasta_yonetim/ana_sayfa.html')

def bolumlerimiz(request):
    return render(request, 'hasta_yonetim/bolumlerimiz.html')

def doktorlarimiz(request):
    return render(request, 'hasta_yonetim/doktorlarimiz.html')

def iletisim(request):
    if request.method == 'POST':
        form = IletisimFormu(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız başarıyla gönderildi! En kısa sürede size dönüş yapacağız.')
            return redirect('iletisim')
        else:
            messages.error(request, 'Lütfen formu doğru şekilde doldurun.')
    else:
        form = IletisimFormu()
    
    context = {
        'form': form
    }
    return render(request, 'hasta_yonetim/iletisim.html', context)
