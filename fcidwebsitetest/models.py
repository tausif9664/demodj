from django.db import models
from django.contrib.auth.models import User
from django import forms
import datetime
from datetime import date
# register model fields
#### loadTest fields ####
class ATR_FT(models.Model):

    name = models.CharField(max_length=100, verbose_name='TEST NAME',null=True)
    test_status = models.CharField(max_length=100, verbose_name='STATUS',null=True,blank=True)
    run_date = models.CharField(max_length=100, verbose_name='LAST RUN DATE',blank=True)
    run_time = models.CharField(max_length=100, verbose_name='RUN TIME',null=True,blank=True)
    link = models.CharField(max_length=100, verbose_name='TOTAL LINK PASSED',null=True,blank=True)
    creation_date = models.CharField(max_length=100, verbose_name='CREATED_DATE',null=True)
    exe_test = models.CharField(max_length=100, verbose_name='Exec Test',null=True,blank=True)
    result_history = models.TextField(max_length=1000, verbose_name="History" ,null=True,blank=True)
    # results=models.TextField(max_length=1000, verbose_name="Results" ,null=True)
    results=models.FileField(blank=True)###file for log button


#### loadTestDetails fields ####
class atr_FTloadTestDetails(models.Model):

    page_links = models.CharField(max_length=100, verbose_name='PAGE LINKS',null=True,blank=True)
    status = models.CharField(max_length=100, verbose_name='STATUS',null=True,blank=True)
    browser = models.CharField(max_length=100, verbose_name='BROWESR',null=True,blank=True)
    hw_info = models.CharField(max_length=100, verbose_name='HW INFO',null=True,blank=True)
    run_time = models.CharField(max_length=100, verbose_name='RUN TIME',null=True,blank=True)
    last_run_date = models.CharField(max_length=100, verbose_name='LAST RUN DATE',null=True,blank=True)
    link = models.CharField(max_length=100, verbose_name='QA REVIEW',null=True,blank=True)
    result_history = models.TextField(max_length=1000, verbose_name="History",null=True,blank=True)

