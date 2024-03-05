from django.contrib import admin
from .models import ATR,atr_loadTestDetails,hATR,logs,h_form,Comment,MyModel,Chart,Test_Env,StageNext_Env,Prod_Env,Release

# Register your models here.
admin.site.register(ATR),
admin.site.register(atr_loadTestDetails),
admin.site.register(MyModel),
admin.site.register(hATR),
admin.site.register(logs),
admin.site.register(h_form),
admin.site.register(Comment),
admin.site.register(Chart),
admin.site.register(Test_Env),
admin.site.register(StageNext_Env),
admin.site.register(Prod_Env),
admin.site.register(Release),
