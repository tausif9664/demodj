import django_tables2 as tables
from .models import ATR,atr_loadTestDetails,Release,Test_Env,StageNext_Env,Prod_Env
from django.utils.safestring import mark_safe
#create your table here
global  a,b,v,w
a = 1
b = 1

### loadtest Table ###
class ATRTable(tables.Table):
    name = tables.TemplateColumn('<a href="/pagelinks/{{record.id}}/">{{record.name}}</a>')
    exe_test=tables.TemplateColumn('<form  action ="/recup_wos/{{record.id}}/" method="POST">{% csrf_token %}<button type="submit" id="btn" onclick="spinner(this)" class="btn btn-success btn-sm" style="padding: .1rem .25rem;font-size: 0.7rem;"> Run </form></button>')
    result_history = tables.TemplateColumn('<a href="/history/{{record.id}}/" target="myFrame"><button data-toggle="modal" href="#modal-id" onclick="myFunction({{record.id}})" class="btn btn-primary btn-sm" style="padding: .1rem .25rem;font-size: 0.7rem;">History</button></a>')
    results = tables.TemplateColumn('<form  action ="/results/{{record.id}}/" target="myFrame1" method="POST">{% csrf_token %}<button type="submit" onclick="myFunction1({{record.id}})" data-toggle="modal" href="#modal-id1" target="myFrame" class="btn btn-primary btn-sm" style="padding: .1rem .25rem;font-size: 0.7rem;"> Log <span class="spinner-border id="spinner" spinner-border-sm" role="status" aria-hidden="true" style="display: none"></span></form></button>')
    id = tables.Column()
    def render_id(self, value):
        global a, v

        if a == 1:
            v = value
            value = v - (v - 1)
            a = a + 1
            return str(value)
        else:
            value = value - (v - 1)
            return str(value)
    class Meta:
        model = ATR
        row_attrs = {
            "data-id": lambda record: record.id
        }
        template_name = 'django_tables2/bootstrap.html'

        attrs = {'class': 'table table-striped table-bordered table-hover table-sm whitebg','id':'AtrTable'}



### loadtestDetails Table ###
# class atr_loadTestDetailsTable(ATRTable,tables.Table):
class atr_loadTestDetailsTable(tables.Table):
    result_history = tables.TemplateColumn(
        '<button type="submit" data-toggle="modal" href="#modal-id" class="btn btn-primary btn-sm" style="padding: .1rem .25rem;font-size: 0.7rem;">History</button>')
    testId = tables.Column(verbose_name="#testId")
    StartTime = tables.Column()
    EndTime = tables.Column()
    PerfTime = tables.Column()
    id = tables.Column()

    LinkPath = tables.Column()
    # def render_PerfTime(self,  value):
    #     value = "record"
    #     return str(value)

    def render_LinkPath(self, value):
        if len(value) > 53:
            return value[0:50] + '...'
        return str(value)
    # def render_id(self, value):
    #     global b, w
    #
    #     if b == 1:
    #         w = value
    #         value = w - (w - 1)
    #         b = b + 1
    #         return str(value)
    #     else:
    #         value = value - (w - 1)
    #         return str(value)
    class Meta:
        model = atr_loadTestDetails
        template_name = 'django_tables2/bootstrap.html'
        sequence  = 'id','testId','LinkPath','status','StartTime','EndTime','Baseline','PerfTime'
        exclude = ('ATR_T',)
        attrs = {'class': 'table table-striped table-bordered table-hover table-sm'}
# attrs={'td': {'bgcolor': 'red','color': 'red'}}
class ReleaseTable(tables.Table):
    Release_date = tables.DateColumn(format='Y-m-d')
    Status = tables.Column()

    def render_Status(self, value):
        if str(value) == "Released":
            return mark_safe("<div class='greentext'>%s</div>" % (value))
        if str(value) == "Cancelled":
            return mark_safe("<div class='redtext'>%s</div>" % (value))
        if str(value) == "TBD":
            return value
        else:
            return mark_safe("<div class='yellowtext'>%s</div>" % (value))

    class Meta:
        model = Release
        exclude = ('id',)
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {'class': 'table table-striped table-bordered table-hover table-sm whitebg','thead' : {
            'class': '',
            'bgcolor': 'lightgreen'
        },'id':'Release'}
# ------------------------------------------------------------------------------------
class TestEnvTable(tables.Table):
    Passed = tables.Column()
    def render_Passed(self, value):
        if float(value) >=95:
            return mark_safe("<div class='greenbg'>%s</div>" % (value))
        if float(value) >=88 and float(value) <=94 :
            return mark_safe("<div class='yellowbg'>%s</div>" % (value))
        else:
            return mark_safe("<div class='redbg'>%s</div>" % (value))
    class Meta:
        model = Test_Env
        exclude = ('id',)
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {'class': 'table table-striped table-bordered table-hover table-sm whitebg'}
#-----------------------------------------------------------------------------------------------------------------
class StageNextTable(tables.Table):
    Passed = tables.Column()
    def render_Passed(self, value):
        if float(value) >= 95:
            return mark_safe("<div class='greenbg'>%s</div>" % (value))
        if float(value) >= 88 and float(value) <= 94:
            return mark_safe("<div class='yellowbg'>%s</div>" % (value))
        else:
            return mark_safe("<div class='redbg'>%s</div>" % (value))
    class Meta:
        model = StageNext_Env
        exclude = ('id',)
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {'class': 'table table-striped table-bordered table-hover table-sm whitebg'}

class ProdEnvTable(tables.Table):
    Passed = tables.Column()
    def render_Passed(self, value):
        if float(value) >= 95:
            return mark_safe("<div class='greenbg'>%s</div>" % (value))
        if float(value) >= 88 and float(value) <= 94:
            return mark_safe("<div class='yellowbg'>%s</div>" % (value))
        else:
            return mark_safe("<div class='redbg'>%s</div>" % (value))
    class Meta:
        model = Prod_Env
        exclude = ('id',)
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {'class': 'table table-striped table-bordered table-hover table-sm whitebg'}

# all_values=Test_Env.objects.all()
    # try:
    #     for i in all_values:
    #         value=i.Passed
    #         print((value),"VALUE")
    #         if float(value) <= 190 :
    #             Passed = tables.Column(attrs={'td': {'class': 'redbg'}})
    #         else:
    #             Passed = tables.Column(attrs={'td': {'class': 'greenbg'}})
    #
    # except:
    #     pass

    # if int(Passed.value.) >= 90:
    #     Passed = tables.Column(attrs={'td': {'bgcolor': 'red'}})
    # else:
    #     Passed = tables.Column(attrs={'td': {'bgcolor': 'green'}})