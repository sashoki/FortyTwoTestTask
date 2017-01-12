# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
#from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
from django.utils import timezone
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField

# Create your models here.


class Home(models.Model):
    class Meta():
        db_table = 'home'
        verbose_name_plural = "Центрально сторінка"
        verbose_name = 'Головна сторінка'
    home_title = models.CharField(max_length=200)
    home_text_min = models.TextField(null=True, blank=True)
    home_text = HTMLField()
    home_image = models.ImageField(null=True, blank=True, upload_to='image/', verbose_name=u'Зображення')
    home_video = EmbedVideoField(null=True, blank=True, verbose_name=u'Відео')
    home_data = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.home_title

    def __str__(self):
        return self.home_title

    def bit_home(self):
        if self.home_image:
            return u'<img src="%s" width="70"/>' % self.home_image.url
        else:
            return u'(none)'

    bit_home.short_descriptio = u'Зображення'
    bit_home.allow_tags = True


class MyContacts(models.Model):
    class Meta():
        db_table = 'mycontacts'
        verbose_name_plural = "Мої дані"
        verbose_name = 'Мої дані'

    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    photo = models.ImageField(null=True, blank=True, upload_to='image/', verbose_name=u'Зображення')
    contacts = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    jaber = models.CharField(max_length=100)
    skype = models.CharField(max_length=100)
    other_contacts = RichTextField(null=True, blank=True)
    bio = HTMLField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def bit_mycontacts(self):
        if self.photo:
            return u'<img src="%s" width="70"/>' % self.photo.url
        else:
            return u'(none)'

    bit_mycontacts.short_descriptio = u'Зображення'
    bit_mycontacts.allow_tags = True