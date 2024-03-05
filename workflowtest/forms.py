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
from .models import h_form_wf,ATR_WF
from datetime import datetime,timedelta

# class UserRegisterForm(UserCreationForm):
#     email= forms.EmailField()
#
#     class Meta:
#         model=User
#         fields=['username','email','password1','password2']



STATUS_CHOICES= [
    ('Open', 'Open'),
    ('Close', 'Close'),
    ('Inprogress', 'Inprogress'),

    ]
global d
d=datetime.today()
class AssignForm(forms.ModelForm):

    class Meta:
        model = h_form_wf
        fields = ['assigned', 'status', 'date_assign']
        widgets = {
            'date_assign': DateTimePickerInput(
                options={
                    # 'minDate': (datetime.today() + timedelta(days=1)).strftime('%m/%d/%Y'),
                    "format": "MM/DD/YYYY",  # moment date-time format
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(AssignForm, self).__init__(*args, **kwargs)
        self.fields['assigned'].widget.attrs={

                'class': "form-control",
                }
        self.fields['status'].widget.attrs = {

            'class': "form-control",
        }


# class ExportResource(resources.ModelResource):
#     class Meta:
#         model = atr_loadTestDetails




