# -*- coding: utf-8 -*-
from functools import partial

from aldryn_client import forms


class Form(forms.BaseForm):

    enable_debug_toolbar = forms.CheckboxField(
        'Enable Django Debug Toolbar',
        required=False,
        initial=True,
    )

    def _show_toolbar(self, request):
        return True

    def to_settings(self, data, settings):

        if settings["DEBUG"] and data['enable_debug_toolbar']:

            settings["INSTALLED_APPS"].extend(["debug_toolbar"])

            settings["DEBUG_TOOLBAR_CONFIG"] = {"SHOW_TOOLBAR_CALLBACK": self._show_toolbar}

            settings["MIDDLEWARE_CLASSES"].insert(
                settings["MIDDLEWARE_CLASSES"].index("django.middleware.gzip.GZipMiddleware") + 1,
                "debug_toolbar.middleware.DebugToolbarMiddleware"
            )

            settings['ADDON_URLS'].append('aldryn_django_debug_toolbar.urls')

        return settings
