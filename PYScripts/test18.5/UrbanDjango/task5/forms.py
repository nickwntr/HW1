from django import forms

class registration_form(forms.Form):
    name = forms.CharField(max_length=30,label="ваше имя")
    age = forms.CharField(max_length=3,label="Ваш возраст")
    psw = forms.CharField(min_length=8,widget=forms.PasswordInput)
    psw_rpt = forms.CharField(min_length=8,widget=forms.PasswordInput)