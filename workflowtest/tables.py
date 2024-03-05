import django_tables2 as tables
from .models import ATR_WF,ATR_WfTestDetails
global  a,b,w,v
a = 1
b = 1
#create your table here

### loadtest Table ###
class ATR_WF_Table(tables.Table):
    # name = tables.TemplateColumn('<a href="/workflowTestDetails/{{record.id}}/">{{record.name}}</a>')
    exe_test=tables.TemplateColumn('<form  action ="/recup_wos_wf/{{record.id}}/" method="POST">{% csrf_token %}<button type="submit" id="btn" onclick="spinner(this)" class="btn btn-success btn-sm" style="padding: .1rem .25rem;font-size: 0.7rem;"> Run </form></button>')
    result_history = tables.TemplateColumn('<a href="/history_wf/{{record.id}}/" target="myFrame"><button data-toggle="modal" href="#modal-id" onclick="myFunction_workflow({{record.id}})" class="btn btn-primary btn-sm" style="padding: .1rem .25rem;font-size: 0.7rem;">History</button></a>')
    results = tables.TemplateColumn('<form  action ="/results_wf/{{record.id}}/" target="myFrame1" method="POST">{% csrf_token %}<button type="submit" onclick="myFunction_workflow_test({{record.id}})" data-toggle="modal" href="#modal-id1" target="myFrame" class="btn btn-primary btn-sm" style="padding: .1rem .25rem;font-size: 0.7rem;"> Log <span class="spinner-border id="spinner" spinner-border-sm" role="status" aria-hidden="true" style="display: none"></span></form></button>')
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
        model = ATR_WF
        row_attrs = {
            "data-id": lambda record: record.id
        }
        template_name = 'django_tables2/bootstrap.html'
        exclude = ('link',)
        attrs = {'class': 'table table-striped table-bordered table-hover table-sm'}


## loadtestDetails Table ###
class atr_wf_loadTestDetailsTable(tables.Table):
    result_history = tables.TemplateColumn(
        '<button type="submit" data-toggle="modal" href="#modal-id" class="btn btn-primary btn-sm" style="padding: .1rem .25rem;font-size: 0.7rem;">History</button>')
    id = tables.Column()

    def render_id(self, value):
        global b, w

        if b == 1:
            w = value
            value = w - (w - 1)
            b = b + 1
            return str(value)
        else:
            value = value - (w - 1)
            return str(value)
    class Meta:
        model = ATR_WfTestDetails
        template_name = 'django_tables2/bootstrap.html'
        attrs = {'class': 'table table-striped table-bordered table-hover table-sm'}


