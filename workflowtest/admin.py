from django.contrib import admin

# Register your models here.
from .models import ATR_WF,ATR_WfTestDetails,h_form_wf,hATR_wf

# Register your models here.
admin.site.register(ATR_WF),
admin.site.register(ATR_WfTestDetails),
admin.site.register(h_form_wf),
admin.site.register(hATR_wf),