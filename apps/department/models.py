# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=False)
