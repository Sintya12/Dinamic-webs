from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profil

class RegisterPengguna(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UpdatePengguna(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profil
        fields = [
            'nama_lengkap',
            'tentang',
            'alamat',
            'website',
            'hp',
            'gambar',
        ]
