from datetime import date

from django.db import models
from django.contrib.postgres.fields import ArrayField


class Company(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=255, blank=False, default="")
    registered_name = models.CharField(max_length=255, blank=True, default="")
    email = models.CharField(max_length=255, blank=True, default="")
    company_reference = models.CharField(max_length=255, blank=False, default="")

    class Meta:
        ordering = ["date_created"]
