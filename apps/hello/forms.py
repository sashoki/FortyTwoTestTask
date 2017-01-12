# -*- coding: utf-8 -*-

from django.forms import ModelForm, TextInput
from django import forms
from django.conf import settings

from models import Home, MyContacts
from django.contrib.admin.widgets import AdminDateWidget


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



class MyContactsForm(ModelForm):
    class Meta:
        model = MyContacts
        fields = '__all__'
        fields = [
            'name',
            'last_name',
            'date_of_birth',
            'photo',
            'contacts',
            'email',
            'jaber',
            'skype',
            'other_contacts',
            'bio',
        ]

    class Media:
        js = ('/admin/jsi18n',
            settings.ADMIN_MEDIA_PREFIX + 'js/core.js',
            settings.ADMIN_MEDIA_PREFIX + "js/calendar.js",
            settings.ADMIN_MEDIA_PREFIX + "js/admin/DateTimeShortcuts.js")

        css = {
            'all': (
                settings.ADMIN_MEDIA_PREFIX + 'css/forms.css',
                settings.ADMIN_MEDIA_PREFIX + 'css/base.css',
                settings.ADMIN_MEDIA_PREFIX + 'css/widgets.css',)
        }

    widgets = {
        'date_of_birth': AdminDateWidget()
    }


"""class CalendarWidget(TextInput):
    class Media:
        js = ( '/admin/jsi18n',
              settings.ADMIN_MEDIA_PREFIX + 'js/core.js',
              settings.ADMIN_MEDIA_PREFIX + "js/calendar.js",
              settings.ADMIN_MEDIA_PREFIX + "js/admin/DateTimeShortcuts.js")
        css = {
            'all': (
                settings.ADMIN_MEDIA_PREFIX + 'css/forms.css',
                settings.ADMIN_MEDIA_PREFIX + 'css/base.css',
                settings.ADMIN_MEDIA_PREFIX + 'css/widgets.css',)
        }

    def __init__(self, attrs={}):
        super(CalendarWidget, self).__init__(attrs={'class': 'vDateField', 'size': '10'})"""