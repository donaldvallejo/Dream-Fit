# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Testuser(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' | ' + self.email + " | " + self.password