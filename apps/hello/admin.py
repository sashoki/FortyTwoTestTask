# -*- coding: utf-8 -*-

from django.contrib import admin
from apps.hello.models import Home, MyContacts

# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    fields = ['home_title', 'home_image', 'home_text_min', 'home_text', 'home_data', 'home_video']
    list_display = ('home_title', 'home_image', 'bit_home')



class MyContactsAdmin(admin.ModelAdmin):
    fields = ['name', 'last_name', 'date_of_birth', 'photo', 'contacts', 'email', 'jaber', 'skype', 'other_contacts', 'bio']
    list_display = ('name', 'photo', 'contacts')


admin.site.register(Home, HomeAdmin)
admin.site.register(MyContacts, MyContactsAdmin)