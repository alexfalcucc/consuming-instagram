# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/graph-of-pets/$',
                           'consuming_instagram.core.views.consuming', name='graph'),
                       url(r'^admin/', include(admin.site.urls)),
                       )