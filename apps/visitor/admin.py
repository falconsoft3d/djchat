# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from apps.visitor.models import Visitor

admin.site.register(Visitor)
