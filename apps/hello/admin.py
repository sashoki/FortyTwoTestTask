# -*- coding: utf-8 -*-

from django.contrib import admin
from apps.hello.models import Home

# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    fields = ['home_title', 'home_image', 'home_text_min', 'home_text', 'home_data', 'home_video']
    list_display = ('home_title', 'home_image', 'bit_home')


admin.site.register(Home, HomeAdmin)