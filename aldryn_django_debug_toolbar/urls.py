# -*- coding: utf-8 -*-
from django.conf.urls import url, include

import debug_toolbar

urlpatterns = [url(r'^__debug__/', include(debug_toolbar.urls))]
