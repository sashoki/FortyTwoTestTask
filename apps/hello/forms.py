# -*- coding: utf-8 -*-

from django.forms import ModelForm
from models import Home


class HomeForm(ModelForm):
    class Meta:
        model = Home
        fields = '__all__'
        fields = [
            'home_title',
            'home_text',
        ]