# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Resource(models.Model):
    company_name = models.CharField(max_length=50)
    author_name  = models.CharField(max_length=50)


class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)

class ERG(models.Model):
    manual_id = models.IntegerField()
    contact_name = models.CharField(max_length=50)
    contact_email = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    city_name = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)
    #post_date = models.DateField()
    post_date = models.CharField(max_length=50)
    identification = models.CharField(max_length=50)

