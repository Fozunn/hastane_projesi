from django import forms
from .models import IletisimMesaji, Doktor

class IletisimFormu(forms.ModelForm):
    class Meta:
        model = IletisimMesaji
        fields = ['ad_soyad', 'telefon', 'email', 'konu', 'mesaj']
        widgets = {
            'ad_soyad': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all',
                'placeholder': 'Adınız ve soyadınız'
            }),
            'telefon': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all',
                'placeholder': 'Telefon numaranız',
                'type': 'tel'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all',
                'placeholder': 'E-mail adresiniz'
            }),
            'konu': forms.Select(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all'
            }),
            'mesaj': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all',
                'placeholder': 'Mesajınızı buraya yazın...',
                'rows': 5
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Form alanlarını zorunlu yapalım
        for field in self.fields:
            self.fields[field].required = True


class DoktorForm(forms.ModelForm):
    class Meta:
        model = Doktor
        fields = ['ad_soyad', 'unvan', 'bolum', 'bio', 'foto', 'aktif']
        
        widgets = {
            'ad_soyad': forms.TextInput(attrs={
                'class': 'w-full px-3 py-3 border border-gray-300 rounded-lg text-base leading-6 focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:ring-opacity-10 transition-all duration-150',
                'placeholder': 'Doktor adı ve soyadı'
            }),
            'unvan': forms.TextInput(attrs={
                'class': 'w-full px-3 py-3 border border-gray-300 rounded-lg text-base leading-6 focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:ring-opacity-10 transition-all duration-150',
                'placeholder': 'Örn: Uzm. Dr., Prof. Dr.'
            }),
            'bolum': forms.Select(attrs={
                'class': 'w-full px-3 py-3 border border-gray-300 rounded-lg text-base leading-6 focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:ring-opacity-10 transition-all duration-150'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'w-full px-3 py-3 border border-gray-300 rounded-lg text-base leading-6 focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:ring-opacity-10 transition-all duration-150',
                'placeholder': 'Doktor hakkında bilgiler...',
                'rows': 4
            }),
            'foto': forms.FileInput(attrs={
                'class': 'w-full px-3 py-3 border border-gray-300 rounded-lg text-base leading-6 focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:ring-opacity-10 transition-all duration-150',
                'accept': 'image/*'
            }),
            'aktif': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 mt-1'
            }),
        }