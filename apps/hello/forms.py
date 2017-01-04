# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms
from models import Home


class HomeForm(ModelForm):
    class Meta:
        model = Home
        fields = '__all__'
        fields = [
            'home_title',
            'home_text',
        ]

# Модель формы обратной связи
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
    phon = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size': '40', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    copy = forms.BooleanField(required=False)