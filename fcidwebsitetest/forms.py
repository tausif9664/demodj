#file for userRegister fields
from django import forms
from import_export import resources
from datetime import date
import time
import django_filters
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
# from bootstrap_datepicker.widgets import DatePicker
from .models import ATR_FT,atr_FTloadTestDetails
from datetime import datetime,timedelta


STATUS_CHOICES= [
    ('Open', 'Open'),
    ('Close', 'Close'),
    ('Inprogress', 'Inprogress'),

    ]
global d
d=datetime.today()







