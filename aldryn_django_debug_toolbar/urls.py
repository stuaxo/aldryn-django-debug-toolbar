# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include

import sys
import debug_toolbar

if settings.DEBUG and 'test' not in sys.argv:
    urlpatterns = [url(r'^__debug__/', include(debug_toolbar.urls))]
