from django import forms

class SingUpForm(forms.Form):
    username = forms.CharField( max_length=100)
    name = forms.CharField( max_length=200)
    email = forms.CharField( max_length=300, widget=forms.EmailInput())
    password = forms.CharField( max_length=100, widget=forms.PasswordInput())
    password2 = forms.CharField( max_length=100, widget=forms.PasswordInput())