from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', 'apps.hello.views.homes', name='homes'),
    url(r'^homes/get/(?P<pk>\d+)/$', 'apps.hello.views.home', name='home'),
    url(r'^homes/create/$', 'apps.hello.views.create', name='create'),
    url(r'^homes/(?P<pk>\d+)/edit/$', 'apps.hello.views.post_edit', name='post_edit'),
    url(r'^add/callback/$', 'apps.hello.views.callback', name='callback'),

)
