from django.db import models

class Person(models.Model):
    RIN = models.CharField(max_length=100, blank=True)
    GSTN = models.CharField(max_length=100, blank=True)
    #birth_date = models.DateField()
    TOTALGST = models.CharField(max_length=100, blank=True)
    MonthofPayment = models.CharField(max_length=100, blank=True)