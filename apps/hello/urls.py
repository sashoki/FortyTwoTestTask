from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', 'apps.hello.views.contacts', name='contacts'),
    url(r'^$', 'apps.hello.views.homes', name='homes'),
    url(r'^homes/get/(?P<pk>\d+)/$', 'apps.hello.views.home', name='home'),
    url(r'^homes/create/$', 'apps.hello.views.create', name='create'),
    url(r'^homes/(?P<pk>\d+)/edit/$', 'apps.hello.views.post_edit', name='post_edit'),
    url(r'^add/callback/$', 'apps.hello.views.callback', name='callback'),
    url(r'^/(?P<pk>\d+)/edit/$', 'apps.hello.views.my_edit', name='my_edit'),
    #url(r'^thanks/$', 'apps.hello.views.thanks', name='thanks'),
    #url(r'^user/create/$', 'apps.hello.views.create_user', name='create_user'),

)
