from django import forms
from django.contrib.auth import authenticate
#from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı:")
    password = forms.CharField(label="Parola:", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Kullanıcı adı veya parola hatalı.")
        
        return cleaned_data

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı Adı")
    password = forms.CharField(max_length=30, label="Parola", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=30, label="Tekrar girin", widget=forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor...")
        
        values = {
            "username": username,
            "password": password  
        }
        return values
