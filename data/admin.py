from django.contrib import admin
from .models import DataCenter


class DataAdmin(admin.ModelAdmin):
    list_display = ['eid', 'stime', 'product', 'iver', 'mid', 'uid', 'ip']

admin.site.register(DataCenter, DataAdmin)