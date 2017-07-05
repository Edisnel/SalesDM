# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', required=True)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', required=True)

#class MyAuthenticationForm(AuthenticationForm):
    # add your form widget here
#    username = forms.CharField(label='Usuario', required=True)
#    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña', required=True)

#class PassChangeForm(PasswordChangeForm):
    # add your form widget here
#    old_password  = forms.CharField(widget=forms.PasswordInput, label='Contraseña antigua:', required=True)
#    new_password1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña nueva:', required=True)
#    new_password2 = forms.CharField(widget=forms.PasswordInput, label='Contraseña nueva (confirmación):', required=True)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden   .')
        return cd['password2']




