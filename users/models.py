from django.db import models
from django.contrib.auth.models import User
from django import forms
import datetime
from datetime import date
from django.db import models
from django_matplotlib import MatplotlibFigureField


class MyModel(models.Model):
    figure = MatplotlibFigureField(figure='my_figure')
# register model fields
#### loadTest fields ####
class ATR(models.Model):

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
class atr_loadTestDetails(models.Model):
    # ATR_T = models.ForeignKey(ATR, on_delete=models.CASCADE, null=True, blank=True)
    LinkPath = models.CharField(max_length=1000, verbose_name='PAGE LINKS',null=True,blank=True)
    status = models.CharField(max_length=100, verbose_name='STATUS',null=True,blank=True)
    StartTime = models.CharField(max_length=100, verbose_name='StartTime',null=True,blank=True)
    EndTime = models.CharField(max_length=100, verbose_name='EndTime',null=True,blank=True)
    # PerfTime = models.CharField(max_length=100, verbose_name='PerfTime', null=True, blank=True)
    Baseline = models.CharField(max_length=100, verbose_name='Baseline',null=True,blank=True)
    CurrentRunDateTime = models.CharField(max_length=100, verbose_name='CurrentRunDateTime',null=True,blank=True)
    testId = models.CharField(db_column='#testId',max_length=100, null=True,blank=True)
    result_history = models.TextField(max_length=1000, verbose_name="History",null=True,blank=True)



#### history fields ####
class hATR(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Close', 'Close'),
        ('Inprogress', 'Inprogress'),

    ]

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    history_date = models.CharField(max_length=100, default=datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
                                    blank=True, null=True)
    assigned = models.CharField(max_length=100, choices=[[g.username, g.username] for g in User.objects.all()],
                               blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, blank=True, null=True)
    date_assign = models.DateField(blank=True, null=True)

    days = models.CharField(max_length=100, blank=True, null=True)
    ATR = models.ForeignKey(ATR, on_delete=models.CASCADE, related_query_name='ATR.name', null=True, blank=True)
    h_a = models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        ordering = ['-id']

    # ordering = ['-id', 'user_name']

#### log file fields ####
class logs(models.Model):
    log = models.TextField(max_length=1000)
    ATR_log = models.ForeignKey(ATR, on_delete=models.CASCADE, related_query_name='ATR.name', null=True)

users = User.objects.all().values_list('username', flat=True)
class h_form(models.Model):


    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Close', 'Close'),
        ('Inprogress', 'Inprogress'),

    ]

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    history_date = models.CharField(max_length=100, default=datetime.datetime.today().strftime("%d/%m/%Y, %H:%M:%S"),
                                    blank=True,null=True)
    assigned=models.CharField(max_length=100,choices= [ [g.username, g.username] for g in User.objects.all() ],blank=True,null=True)
    status=models.CharField(max_length=100,choices= STATUS_CHOICES,blank=True,null=True)
    date_assign=models.DateField(blank=True,null=True)

    days=models.CharField(max_length=100,blank=True,null=True)
    ATR = models.ForeignKey(ATR, on_delete=models.CASCADE, related_query_name='ATR.name', null=True,blank=True)
    h_a = models.TextField(max_length=1000,blank=True,null=True)
    class Meta:
        ordering=['-id']

    # ordering = ['-id', 'user_name']

#### Assign fields ####

from django.db import models

#only for testing purpose no relation with any files
class Comment(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)

    def __str__(self):  # __unicode__ on Python 2
        return self.title

# Database creation for welcome page
class Chart(models.Model):
    development_fixes = models.IntegerField(blank=True)
    qa_verfication = models.IntegerField(blank=True)
    regection_rate = models.IntegerField(blank=True)

class Release(models.Model):
    App = models.CharField(max_length=100, verbose_name='App')
    Release_date = models.DateField(verbose_name='Release date',blank=True, null=True,)
    # Release_date = models.CharField(max_length=100, verbose_name='Release date')
    No_items = models.IntegerField(verbose_name='#No Items',blank=True, null=True,)
    Status =  models.CharField(max_length=100,default='-', verbose_name='Status',blank=True, null=True,)

class Test_Env(models.Model):
    App = models.CharField(max_length=100, verbose_name='App')
    Regrations_details = models.CharField(max_length=100,default='-', verbose_name='Regression Tests Details')
    No_of_tests = models.IntegerField( verbose_name='# of Tests')
    Passed = models.FloatField(blank=True,null=True, verbose_name='Passed %')

class StageNext_Env(models.Model):
    App = models.CharField(max_length=100, verbose_name='App')
    Regrations_details = models.CharField(max_length=100, default='-', verbose_name='Regression Tests Details')
    No_of_tests = models.IntegerField(verbose_name='# of Tests')
    Passed = models.FloatField(blank=True, null=True, verbose_name='Passed %')

class Prod_Env(models.Model):
    App = models.CharField(max_length=100, verbose_name='App')
    Regrations_details = models.CharField(max_length=100, default='-', verbose_name='Regression Tests Details')
    No_of_tests = models.IntegerField(verbose_name='# of Tests')
    Passed = models.FloatField(blank=True, null=True, verbose_name='Passed %')