# -*- coding: utf-8 -*-
import os

from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template import Template
from django.utils._os import safe_join

__author__ = 'Denis Ivanets (denself@gmail.com)'


def get_page_or_404(name):
    """Returns Page content as a Django template or raise 404 error."""
    try:
        file_path = safe_join(settings.SITE_PAGES_DIRECTORY, name)
    except ValueError:
        raise Http404
    else:
        if not os.path.exists(file_path):
            raise Http404

    with open(file_path, 'r') as f:
        page = Template(f.read())

    return page


def get_page(request, slug='index'):
    """Render the requested page if found."""
    file_name = '{}.html'.format(slug)
    page = get_page_or_404(file_name)
    context = {
        'slug': slug,
        'page': page,
    }
    return render(request, 'page.html', context)