#!/usr/bin/python
#
# Copyright 2018-2020 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import List

from django.contrib import admin
from django.urls import re_path
from django.views.decorators.csrf import ensure_csrf_cookie

from polycommon import conf
from polycommon.options.registry.core import ADMIN_VIEW_ENABLED

from polycommon.apis.index.errors import (
    Handler50xView,
    Handler403View,
    Handler404View,
)  # noqa
from polycommon.apis.index.health import HealthView
from polycommon.apis.index.views import IndexView


def _handler500(request):
    return Handler50xView.as_view()(request)


handler404 = Handler404View.as_view()
handler403 = Handler403View.as_view()
handler500 = _handler500


def get_urlpatterns(app_patterns: List):
    if conf.get(ADMIN_VIEW_ENABLED):
        app_patterns += [re_path(r"^_admin/", admin.site.urls)]

    urlpatterns = app_patterns + [
        re_path(r"^healthz/?$", HealthView.as_view(), name="health_check"),
        re_path(r"^50x.html$", Handler50xView.as_view(), name="50x"),
        re_path(r"^permission.html$", Handler403View.as_view(), name="permission"),
        re_path(r"^404.html$", Handler404View.as_view(), name="404"),
        re_path(r"^.*?", ensure_csrf_cookie(IndexView.as_view()), name="index",),
    ]

    return urlpatterns