# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from apps.department.models import Department

admin.site.register(Department)
