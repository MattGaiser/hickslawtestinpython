"""
Definition of models.
"""

from django.db import models
from django.contrib import admin

# Create your models here.
class DataPoint(models.Model):
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    numOfElements = models.IntegerField(default=2)
    seconds = models.IntegerField(default=0)
    timetaken = models.IntegerField(default=0)


admin.site.register(DataPoint)