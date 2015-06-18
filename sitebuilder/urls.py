# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

__author__ = 'Denis Ivanets (denself@gmail.com)'


urlpatterns = patterns(
    'sitebuilder.views',
    url(r'^(?P<slug>[\w./-]+)/$', 'get_page', name='page'),
    url(r'^$', 'get_page', name='homepage'),
)