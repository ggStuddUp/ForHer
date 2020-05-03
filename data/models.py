from django.db import models
from django.utils import timezone


class DataCenter(models.Model):
    eid = models.CharField(max_length=40, blank=True)
    stime = models.CharField(max_length=30)
    product = models.CharField(max_length=40, blank=True)
    iver = models.CharField(max_length=20, blank=True)
    mid = models.CharField(max_length=100, blank=True)
    uid = models.CharField(max_length=500, blank=True)
    ip = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = '数据'
        verbose_name_plural = verbose_name

