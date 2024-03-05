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
from .models import h_form,ATR,atr_loadTestDetails
from datetime import datetime,timedelta
from django.contrib.auth.forms import PasswordResetForm
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


    class Meta:
        model=User
        fields=['username','email','password1','password2']

# class ResetPassword(PasswordResetForm):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["new_password1"].help_text = None
#
#     class Meta:
#         model = User
#         fields = ("new_password1", "new_password2")

STATUS_CHOICES= [
    ('Open', 'Open'),
    ('Close', 'Close'),
    ('Inprogress', 'Inprogress'),

    ]
global d
d=datetime.today()
class AssignForm(forms.ModelForm):

    class Meta:
        model = h_form
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


class ExportResource(resources.ModelResource):
    class Meta:
        model = atr_loadTestDetails




