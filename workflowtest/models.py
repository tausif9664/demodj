from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django import forms
import datetime
from datetime import date
# register model fields
#### loadTest fields ####
class ATR_WF(models.Model):

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
class ATR_WfTestDetails(models.Model):

    page_links = models.CharField(max_length=100, verbose_name='PAGE LINKS',null=True,blank=True)
    status = models.CharField(max_length=100, verbose_name='STATUS',null=True,blank=True)
    browser = models.CharField(max_length=100, verbose_name='BROWESR',null=True,blank=True)
    hw_info = models.CharField(max_length=100, verbose_name='HW INFO',null=True,blank=True)
    run_time = models.CharField(max_length=100, verbose_name='RUN TIME',null=True,blank=True)
    last_run_date = models.CharField(max_length=100, verbose_name='LAST RUN DATE',null=True,blank=True)
    link = models.CharField(max_length=100, verbose_name='QA REVIEW',null=True,blank=True)
    result_history = models.TextField(max_length=1000, verbose_name="History",null=True,blank=True)

#### history fields ####
class hATR_wf(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Close', 'Close'),
        ('Inprogress', 'Inprogress'),

    ]

    user_names_wf = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    history_date = models.CharField(max_length=100, default=datetime.datetime.today().strftime("%d/%m/%Y, %H:%M:%S"),
                                    blank=True, null=True)
    assigned = models.CharField(max_length=100, choices=[[g.username, g.username] for g in User.objects.all()],
                               blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, blank=True, null=True)
    date_assign = models.DateField(blank=True, null=True)

    days = models.CharField(max_length=100, blank=True, null=True)
    ATR_wf = models.ForeignKey(ATR_WF, on_delete=models.CASCADE, related_query_name='ATR_WF.name', null=True, blank=True)
    h_a = models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        ordering = ['-id']
#
#### log file fields ####
class logs(models.Model):
    log = models.TextField(max_length=1000)
    ATR_log = models.ForeignKey(ATR_WF, on_delete=models.CASCADE, related_query_name='ATR.name', null=True)

users = User.objects.all().values_list('username', flat=True)
class h_form_wf(models.Model):


    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Close', 'Close'),
        ('Inprogress', 'Inprogress'),

    ]

    user_names_wf = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    history_date = models.CharField(max_length=100, default=datetime.datetime.today().strftime("%d/%m/%Y, %H:%M:%S"),
                                    blank=True,null=True)
    assigned=models.CharField(max_length=100,choices= [ [g.username, g.username] for g in User.objects.all() ],blank=True,null=True)
    status=models.CharField(max_length=100,choices= STATUS_CHOICES,blank=True,null=True)
    date_assign=models.DateField(blank=True,null=True)

    days=models.CharField(max_length=100,blank=True,null=True)
    ATR_WF = models.ForeignKey(ATR_WF, on_delete=models.CASCADE, related_query_name='ATR_WF.name', null=True,blank=True)
    h_a = models.TextField(max_length=1000,blank=True,null=True)
    class Meta:
        ordering=['-id']
#
#### Assign fields ####

from django.db import models

#only for testing purpose no relation with any files
class Comment(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)

    def __str__(self):  # __unicode__ on Python 2
        return self.title

# class Post(models.Model)
