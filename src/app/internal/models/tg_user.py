from django.contrib import admin
from django.db import models


class tgUser(models.Model):
    username = models.CharField(max_length=20, blank=True, verbose_name="Uname")
    phone_number = models.CharField(max_length=20, blank=True, verbose_name="Phonenumber")
