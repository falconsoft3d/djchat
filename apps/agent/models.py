# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
