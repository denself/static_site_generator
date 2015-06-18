# -*- coding: utf-8 -*-
import os
import sys
from django.conf import settings

__author__ = 'Denis Ivanets (denself@gmail.com)'

DEBUG_SECRET_KEY = '+2!(!zt7rr$yjc*200kppydt4ao!97j)jn38j0jmgksn5@_qe@'
settings.configure(
    DEBUG=os.environ.get('DEBUG', 'on') == 'on',
    SECRET_KEY=os.environ.get('SECRET_KEY', DEBUG_SECRET_KEY),
    ROOT_URLCONF='sitebuilder.urls',
    ALLOWED_HOSTS=os.environ.get('ALLOWED_HOSTS', 'localhost').split(','),
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
    ),
    STATIC_URL='/static/'
)

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)