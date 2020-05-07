from rest_framework import viewsets
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('RIN', 'GSTN', 'TOTALGST','MonthofPayment')