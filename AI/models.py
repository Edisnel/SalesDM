# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class AImodels(models.Model):
    name = models.CharField(max_length=20, default='DEFAULT VALUE')
    method = models.CharField(max_length=20, default='DEFAULT VALUE')
    accuracy = models.DecimalField(decimal_places=3, max_digits=3)
    applyto = models.Model
    predictors = models.CharField(max_length=20, default='DEFAULT VALUE')
    target = models.CharField(max_length=20, default='DEFAULT VALUE')
    dategen = models.DateTimeField(default=timezone.now)
    problemtoapply = models.CharField(max_length=20, default='DEFAULT VALUE')

# This is to describe the bussiness problems to solve with AI models
class Problems(models.Model):
    name = models.CharField(max_length=20, default='DEFAULT VALUE')
    area = models.CharField(max_length=20, default='DEFAULT VALUE') # the bussiness area or department the problem belongs to






