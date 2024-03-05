from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect,get_object_or_404
from bs4 import BeautifulSoup
from djqscsv import render_to_csv_response
import pyodbc, csv,datetime
import datetime as p
from datetime import timedelta,datetime
import pyodbc, csv
from django.db.models.query import QuerySet
import pandas as pd
from django.contrib.auth.models import User
from django.template import loader
import os
import py
from django.contrib import messages
from .forms import UserRegisterForm,AssignForm,ExportResource
from .models import  hATR, ATR,logs,h_form,Chart,Release,Test_Env,StageNext_Env,Prod_Env
from .tables import ATRTable
from .tables import atr_loadTestDetailsTable,ReleaseTable,TestEnvTable,StageNextTable,ProdEnvTable
from django_tables2 import RequestConfig
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import csv, io,time
from datetime import date
from django.db.models import Q
import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse
from django.http import HttpResponse
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
# from dynamic_models.models import AbstractModelSchema, AbstractFieldSchema
from django.db import models
import subprocess
# class FilteredPersonListView(SingleTableMixin, FilterView):
#     table_class = ATRTable
#     model = ATR
#     template_name = "users/loadTest.html"
#     filterset_class = ATRFilter

#### Path for files #####
test_path="C:\\FoodchainAutomation_old\\FoodchainAutomation_old\\Tests\\"

csv_path='C:\\FoodchainAutomation_old\\FoodchainAutomation_old\\Tests\\csv_files\\'
log_path='C:\\FoodchainAutomation_old\\FoodchainAutomation_old\\Tests\\\\log_files\\'
import matplotlib.pyplot as plt
from random import randint
from django.views.generic import TemplateView
# from chartjs.views.lines import BaseLineChartView


def connect(pk):
    pk = pk
    print(("PK",pk))
    name = ATR.objects.get(id=pk)
    p = name.name
    l = str(p)
    import pyodbc, csv, datetime
    import datetime as p
    from datetime import timedelta, datetime
    # print("DATE:", str(p.datetime.today()))
    Pre_Hour = datetime.strftime(datetime.now() - timedelta(hours=1), '%Y-%m-%d %H')
    Pre_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
    # print("Pre_date", Pre_date)
    # print("Pre_Hour", Pre_Hour)
    # print("Pre_date", type(Pre_date))
    # print("Pre_Hour", type(Pre_Hour))
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 13 for SQL server};server=192.168.8.20;database=FCID_Automation;uid=sa;PWD=!nd!a0ffice@2020;')
    # 'DRIVER={ODBC Driver 13 for SQL server};server=192.168.8.20;database=FCID_Automation;uid=GID\pip-rhiremath;')

    print(conn)
    cursor = conn.cursor()
    print("CSV",csv_path)
    print("OK")
    with open(csv_path + l + '.txt', 'r') as link_file:
        a = link_file.readline()  # insert header in tables
        b = link_file.readlines()  # insert data in tables
        c = len(b)
        y = list()
        w = y[1:]
        print("c:", c)
        for z in range(c):
            y.append(z)
        print("Y", y[1:])

    def get_sec(time_str):
        """Get Seconds from time."""
        h, m, s = time_str.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)

    c = len(b)
    time = []
    for e in range(c - 1):
        t1 = (b[e].split(',')[2])
        t2 = (b[e].split(',')[3])
        t4 = get_sec(t2)
        t3 = get_sec(t1)
        t = int(t4) - int(t3)
        print("StartTime:", t4)
        print("EndTime:", t3)
        print("Time:", t)
        q = str(p.timedelta(seconds=t))
        print("Q:", q)
        time.append(q)
    cursor.execute("""
                IF OBJECT_ID('""" + l + """', 'U') IS NULL
                    
                CREATE TABLE """ + l + """ (
                    id INT NOT NULL,
                    """ + str(a.split(',')[0][1:].rstrip()) + """ VARCHAR(100),
                    """ + str(a.split(',')[1].rstrip()) + """ VARCHAR(100),
                    """ + str(a.split(',')[2].rstrip()) + """ VARCHAR(100),
                    """ + str(a.split(',')[3].rstrip()) + """ VARCHAR(100),
                    """ + str(a.split(',')[4].rstrip()) + """ VARCHAR(100),
                    """ + str(a.split(',')[5].rstrip()) + """ VARCHAR(100),
                    """ + str(a.split(',')[6].rstrip()) + """ VARCHAR(100),
                    blank VARCHAR(100),
                    PerfTime VARCHAR(100),

                )
                """)
    a = 1
    for n in b[:-1]:
        # print("N", str(n))
        p = n.rstrip().split(',')
        d = list(p)
        d.insert(0, a)
        d.insert(9, time[a - 1])
        a = a + 1
        print("d:", d)

        cursor.executemany(
            "INSERT INTO " + l + " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [tuple(d)])
        conn.commit()

@login_required()
def welcome(request):
    #---------For Chart
    Development = []
    Regection = []
    QA = []
    Chart_list = Chart.objects.all()
    for i in Chart_list:
        Development.append(i.development_fixes)
        QA.append(i.qa_verfication)
        Regection.append(i.regection_rate)

    #------ReleaseTable
    Release_Table = ReleaseTable(Release.objects.all())
    RequestConfig(request).configure(Release_Table)
    RequestConfig(request, paginate={'per_page': 7}).configure(Release_Table)

    TestEnv_Table = TestEnvTable(Test_Env.objects.all())
    for i in Test_Env.objects.all():
        print("I:",i)
    RequestConfig(request).configure(TestEnv_Table)

    ProdEnv_Table = ProdEnvTable(Prod_Env.objects.all())
    RequestConfig(request).configure(ProdEnv_Table)

    StageNext_Table = StageNextTable(StageNext_Env.objects.all())
    RequestConfig(request).configure(StageNext_Table)

    simple_table = ReleaseTable(Release.objects.all())
    RequestConfig(request).configure(simple_table)
    # RequestConfig(request, paginate={'per_page': 7}).configure(simple_table)
    ajax=simple_table.as_html(request)
    # return HttpResponse(simple_table.as_html(request))
    data = {'Development':Development,'Regection':Regection,'QA':QA, 'Release_Table':Release_Table, 'ProdEnv_Table':ProdEnv_Table,
            'TestEnv_Table':TestEnv_Table,'ajax':ajax, 'StageNext_Table':StageNext_Table}

    return render(request, 'welcome.html',data)
###########------Release Table Functionality---------########
def simple_view(request):
    simple_table = ReleaseTable(Release.objects.all())
    RequestConfig(request).configure(simple_table)
    RequestConfig(request, paginate={'per_page': 7}).configure(simple_table)
    return HttpResponse(simple_table.as_html(request))
###########------TestEnv Table Functionality---------########
def TestEnv_view(request):
    TestEnv_Table = TestEnvTable(Test_Env.objects.all())
    RequestConfig(request).configure(TestEnv_Table)
    return HttpResponse(TestEnv_Table.as_html(request))

#### Create your user registration here. ####
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!. You are now able to login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
#### welcome page view #####


import datetime as n
#### loadTestDetails_id page view for loadTestDetails page ####

@login_required()
def loadTestDetails_id(request, pk):
    ####

    pk = pk
    name = ATR.objects.get(id=pk)
    p=name.name
    l=str(p)
    import pyodbc, csv, datetime
    import datetime as p
    from datetime import timedelta, datetime
    # print("DATE:", str(p.datetime.today()))
    Pre_Hour = datetime.strftime(datetime.now() - timedelta(hours=1), '%Y-%m-%d %H')
    Pre_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
    # print("Pre_date", Pre_date)
    # print("Pre_Hour", Pre_Hour)
    # print("Pre_date", type(Pre_date))
    # print("Pre_Hour", type(Pre_Hour))
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 13 for SQL server};server=192.168.8.20;database=FCID_Automation;uid=sa;PWD=!nd!a0ffice@2020;')
    # 'DRIVER={ODBC Driver 13 for SQL server};server=192.168.8.20;database=FCID_Automation;uid=GID\pip-rhiremath;')

    print(conn)
    cursor = conn.cursor()
    print("OK")
    # with open("C:\\Users\\tausif.tamboli\\Downloads\\" + l + '.txt', 'r') as link_file:
    #     a = link_file.readline()  # insert header in tables
    #     b = link_file.readlines()  # insert data in tables
    #     c = len(b)
    #     y = list()
    #     w = y[1:]
    #     print("c:", c)
    #     for z in range(c):
    #         y.append(z)
    #     print("Y", y[1:])
    #
    # def get_sec(time_str):
    #     """Get Seconds from time."""
    #     h, m, s = time_str.split(':')
    #     return int(h) * 3600 + int(m) * 60 + int(s)
    #
    # c = len(b)
    # time = []
    # for e in range(c - 1):
    #     t1 = (b[e].split(',')[2])
    #     t2 = (b[e].split(',')[3])
    #     t4 = get_sec(t2)
    #     t3 = get_sec(t1)
    #     t = int(t4) - int(t3)
    #     print("StartTime:", t4)
    #     print("EndTime:", t3)
    #     print("Time:", t)
    #     q=str(p.timedelta(seconds=t))
    #     print("Q:",q)
    #     time.append(q)
    # cursor.execute("""
    #         IF OBJECT_ID('""" + l + """', 'U') IS  NULL
    #         CREATE TABLE """ + l + """ (
    #             id INT NOT NULL,
    #             """ + str(a.split(',')[0].rstrip()) + """ VARCHAR(100),
    #             """ + str(a.split(',')[1].rstrip()) + """ VARCHAR(100),
    #             """ + str(a.split(',')[2].rstrip()) + """ VARCHAR(100),
    #             """ + str(a.split(',')[3].rstrip()) + """ VARCHAR(100),
    #             """ + str(a.split(',')[4].rstrip()) + """ VARCHAR(100),
    #             """ + str(a.split(',')[5].rstrip()) + """ VARCHAR(100),
    #             """ + str(a.split(',')[6].rstrip()) + """ VARCHAR(100),
    #             blank VARCHAR(100),
    #             PerfTime VARCHAR(100),
    #
    #         )
    #         """)
    # a = 1
    # for n in b[:-1]:
    #     print("N", str(n))
    #     p = n.rstrip().split(',')
    #     d = list(p)
    #     d.insert(0, a)
    #     d.insert(9, time[a - 1])
    #     a = a + 1
    #     print("d:", d)
    #
    #     cursor.executemany(
    #         "INSERT INTO " + l + " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    #         [tuple(d)])
    #     conn.commit()
    for x in range(365):

        Pre_date = datetime.strftime(datetime.now() - timedelta(x), '%Y-%m-%d')
        print("Pre_date:", Pre_date)
        cursor.execute('select * from ' + l + '  where CurrentRunDateTime LIKE \'%' + Pre_date + '%\'')
        # declearation of the global variable

        # All Data fetching in a variable data
        data = cursor.fetchall()
        if len(data)>0 :
            # print("DATA3:", data)
            break;


    # print("DATA1:", data)
    table = atr_loadTestDetailsTable(data)
    RequestConfig(request, paginate={'per_page': 500}).configure(table)
    return render(request, 'users/loadTestDetails.html',
                  {'table': table, 'name': name, 'pk': pk})
    return HttpResponse("<h1>No LinkTable Found </h1>")


global forms
global Assigned
global d

@login_required()
def history(request,pk):
    d=None
    try:
        try:
            p = h_form.objects.get(id=pk)
        except:
            p = h_form.objects.get(id=pk + 62) or h_form.objects.get(id=pk)
        form = AssignForm(instance=p)
    except:
        form=AssignForm()
    f_forms=form

    if request.method == "POST":
        try:
            try:
                instance = h_form.objects.get(id=pk)
            except:
                instance = h_form.objects.get(id=pk + 62) or h_form.objects.get(id=pk)
            form = AssignForm(request.POST, instance=instance)
        except:
            form = AssignForm(request.POST)
        if form.is_valid():
            try:
                assigned=form.cleaned_data.get('assigned')
                status=form.cleaned_data.get('status')
                date_assign=form.cleaned_data.get('date_assign')
                a = ATR.objects.get(id=pk)
                user = request.user
                a = ATR.objects.get(id=pk)
                # print('is valid ')
                users = h_form.objects.all()
                ##############################################################################
                dt = datetime.date.today()
                dc = dt.strftime("%m/%d/%Y")
                # print(dc, 'd')
                # print(dt, 'dt')
                datetime_object1 = datetime.datetime.strptime(dc, '%m/%d/%Y')
                datetime_object2 = datetime.datetime.strptime(str(date_assign), '%Y-%m-%d')
                # print()
                p = (datetime_object1 - datetime_object2).days
                # print(p)
                c = p
                # print("DAYS: ",p)
                Assign = h_form.objects.all()
                Assigned = h_form.objects.first()
                hist = hATR.objects.all()
                user = request.user
                users = User.objects.values_list('username', flat=True)
                try:
                    # print("data update")
                    # print(len(h_form.objects.filter(id=pk)),":length")
                    b=1

                    try:
                        if  len(h_form.objects.filter(id=pk)) != 0 :
                            form_history = h_form.objects.filter(id=pk) \
                                .update(assigned=assigned, status=status, date_assign=date_assign, ATR=a, days=p,user_name=user)
                            # print("data update successfully")
                        else:
                            # print("Add new data entry")
                            form_history = h_form.objects.filter(id=pk) \
                                .create(assigned=assigned, status=status, date_assign=date_assign, ATR=a, days=p,
                                        user_name=user)
                            # print("data added successfully")
                    except:
                        pass
                    # a.save()

                except:
                    pass
                hform_history = hATR(history_date=datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),assigned=assigned, status=status, date_assign=date_assign, ATR=a, days=p, user_name=user)
                hform_history.save()
                ATR_id = ATR.objects.all()
                j = 0
                try:
                    for a in ATR_id:
                        if pk == a.id:
                            for i in Assign:
                                if i.ATR.id == a.id:

                                    if j == 0:
                                        # print(i.days)
                                        d = i.days
                                        j = 1
                                        if i.status != "Open":
                                            d = "NA"
                                        if int(i.days) < 0:
                                            d = "NA"

                except:
                    pass
                return render(request, 'users/history.html',
                              {'user': user, 'users': users, 'hist': hist, 'Assign': Assign, 'form': form,
                               'ATR_id': ATR_id,
                               'pk': pk, 'p': p, 'Assigned': Assigned, 'd': d})

            except:
                try:
                    try:
                        p = h_form.objects.get(id=pk)
                    except:
                        p = h_form.objects.get(id=pk + 62) or h_form.objects.get(id=pk)
                    form = AssignForm(instance=p)
                except:
                    form = AssignForm()
                Assign = h_form.objects.all()
                Assigned = h_form.objects.first()
                ATR_id = ATR.objects.all()
                log_id = logs.objects.all()
                hist = hATR.objects.all()
                table = ATRTable(ATR.objects.all())
                RequestConfig(request).configure(table)
                try:
                    result_history = request.POST["history"]
                except:
                    result_history=" "
                a = ATR.objects.get(id=pk)
                hform_history = hATR(history_date=datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),h_a=result_history, ATR=a, user_name=user, date_assign=date.today(),
                                     assigned=status,
                                     status=status)
                hform_history.save()
                return render(request, 'users/history.html',
                              {'user': user, 'users': users, 'hist': hist, 'Assign': Assign, 'form': form, 'ATR_id': ATR_id,
                               'pk': pk, 'Assigned':Assigned,'d':d})

    Assign = h_form.objects.all()
    Assigned = h_form.objects.first()
    p=None
    try:
        p = h_form.objects.get(id=pk)
        form = AssignForm(instance=p)
    except:
        form=AssignForm()
    pk = pk
    global id_atrs
    id_atrs = pk
    request.session['pk'] = pk
    user = request.user
    users = User.objects.values_list('username', flat=True)
    user_range = range(1, )
    ATR_id = ATR.objects.all()
    log_id = logs.objects.all()
    hist = hATR.objects.all()
    table = ATRTable(ATR.objects.all())
    RequestConfig(request).configure(table)
    # print("History view")
    j=0
    try:
        for a in ATR_id:
            if pk == a.id:
                for i in Assign :
                    if i.ATR.id == a.id:

                        if j==0:
                            p=i.date_assign

                            dt = datetime.date.today()
                            d = dt.strftime("%m/%d/%Y")
                            # print(d, 'd')
                            # print(dt, 'dt')
                            datetime_object1 = datetime.datetime.strptime(d, '%m/%d/%Y')
                            datetime_object2 = datetime.datetime.strptime(str(p), '%Y-%m-%d')
                            # print()
                            d = (datetime_object1 - datetime_object2).days

                            # print(d)
                            # d=i.days
                            j=1
                            if i.status != "Open":
                                d="NA"
                            if int(i.days) < 0:
                                d="NA"

    except:
        pass

    return render(request, 'users/history.html',
                  {'p': p, 'form': form, 'table': table, 'user_range': user_range, 'user': user, 'users': users,
                   'hist': hist, 'ATR_id': ATR_id, 'log_id': log_id, 'pk': pk, 'Assign': Assign,'Assigned':Assigned,'d':d})


#### Log Function #####
def log(request,pk):
    pk=pk
    ATR_id = ATR.objects.all()
    log_id = logs.objects.all()
    hist = hATR.objects.all()
    table = ATRTable(ATR.objects.all())
    RequestConfig(request).configure(table)
    name = ATR.objects.get(id=pk)
    fileName = log_path + name.name + ".log"
    with open(fileName) as f:
        b = f.readlines()

    response_content = b
    t = loader.get_template('users/log.html')
    c = {'pk': pk,'b':b}
    return HttpResponse(t.render(c,request),content_type="text/plain")

@login_required()
def loadTest(request):
    ATR_id = ATR.objects.all()
    log_id = logs.objects.all()
    hist = hATR.objects.all()
    table = ATRTable(ATR.objects.all())

    # for filename in os.listdir(test_path):
    #     if filename.startswith('TEST'):
    #         for name in ATR_id:
    #             if filename != name.name:
    #                 add_test = ATR(name=filename, creation_date=date.today())
    #                 add_test.save()
    #

    RequestConfig(request).configure(table)
    # print("loadTest")
    # pks = ATR.objects.all()[:1].get()
    # pk_default = pks.id  ####initiai Id to remove 404 not found error
    return render(request, 'users/loadTest.html', {'table': table, 'hist': hist,  'ATR_id': ATR_id, 'log_id':log_id
        # , 'pk':pk_default
                                                   })


########LOG view for log file #########
# @csrf_exempt
def results(request,pk):
    pk=pk
    table = ATRTable(ATR.objects.all())
    RequestConfig(request).configure(table)
    name = ATR.objects.get(id=pk)

    if request.method == 'POST':
        request.session['pk'] = pk
        fileName = log_path+name.name+".log"
        # print(name.name)
        with open(fileName) as f:
            b=f.readlines()

        response_content = b
        responce= HttpResponse(response_content, content_type="text/plain")
        return responce
    return redirect('loadTest')


###################
##This function for database entry from server via socket and render to loadtest page
##################


# @csrf_exempt
def recup_wos(request,pk):
    #########template section query##after Run button click

    testname = ATR.objects.get(id=pk)
    testname='a'
    ATR_id = ATR.objects.all()
    hist = hATR.objects.all()
    table = ATRTable(ATR.objects.all())
    RequestConfig(request).configure(table)
    ########
    global id_atr
    id_atr=pk
    name = ATR.objects.get(id=pk)
    # testcaseFullPath=test_path+name.name+'.py'
    if request.method == 'POST':
        a=ATR.objects.get(id=pk)
        a.run_date=date.today()
        a.save()
        try:
            if (csv_path+name.name+".csv" is not None):
                os.remove(csv_path+name.name+".csv")
                print("file deleted")
        except:
            pass
        try:
            # args_str = "--html=report.html --self-contained-html --excelreport= D:\csv_files\TEST_F022_FCIDWEB_Get_Your_Certification_on_track.py"

            args_str = "--html=report.html --self-contained-html --excelreport="+csv_path+name.name+".xls "+test_path+name.name+".py"
            # args_str ="-v -s --csv "+csv_path+name.name+".csv "+test_path+name.name+".py"
            print(args_str)
            py.test.cmdline.main(args_str.split(" "))   #test run succeefull
            connect(pk)

            soup = BeautifulSoup(open('report.html', 'r'))
            for script in soup(["script", "style"]):  # remove all javascript and stylesheet code
                script.extract()
            text=soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            with open('people.txt', 'w') as f:
                f.write(text)
                f.close()

            errors = []  # The list where we will store results.
            count = 0
            end_count = 0
            linenum = 0

            with open('people.txt', 'rt') as myfile:
                for line in myfile:
                    linenum += 1
                    if line.startswith('def'):
                        end_count += 1
                    if end_count == 2:
                        count = 2
                    if count == 1:
                        errors.append(line.rstrip('\n'))

                    if (line.startswith('self') and count == 0):
                        errors.append(line.rstrip('\n'))
                        count = 1

            for err in errors:
                # print(err)
                with open(log_path+'logfile.log', 'a') as f:
                    f.write(err)
                    f.write("\n")
                    f.close()
            time.sleep(2)
            xls = pd.ExcelFile(csv_path+name.name+".xls")
            df = xls.parse(sheetname="Sheet1", index_col=None, na_values=['NA'])
            df.to_csv(csv_path+name.name+".csv")
            time.sleep(2)
            os.remove(csv_path + name.name + ".xls")
            csv_file=open(csv_path + name.name+'.csv','r')
            data_set = csv_file.read()
            # print(data_set)
            io_string = io.StringIO(data_set)
            next(io_string)

            try:
                for column in csv.reader(io_string, delimiter=','):

                    # created=ATR.objects.update_or_create
                    _, created=ATR.objects.filter(pk=id_atr).update(
                        ##id = column[0],
                        test_status = column[4],
                        run_time = column[5][0:8],

                    )

            except:

                return redirect('loadTest')
            csv_file.close()

        except:

            return redirect('loadTest')


        context = {}
        table = ATRTable(ATR.objects.all())
        RequestConfig(request).configure(table)
        a=zip(ATR_id,hist)
        time.sleep(3)

        return render(request, 'users/loadTest.html', {'table': table,'hist': hist, 'name': testname, 'ATR_id': ATR_id,'a':a })


    return redirect('loadTest')


#search field for load test details page
def search(request):
    # print("search view called")
    template = 'users/loadTest.html'
    pk=request.session['rk']
    query = request.GET.get('q')
    testname = ATR.objects.get(id=pk)
    name_details = atr_loadTestDetails.objects.all()
    table = atr_loadTestDetailsTable(atr_loadTestDetails.objects.all())
    RequestConfig(request).configure(table)
    table_list = atr_loadTestDetails.objects.all()
    if query=="":
        # print("blank")
        table = atr_loadTestDetailsTable(atr_loadTestDetails.objects.filter(id=pk))
        return render(request, 'users/loadTestDetails.html',
                      {'table': table, 'name': testname, 'name_details': name_details, 'pk': pk})
    else:
        # print("not blank")
        results = atr_loadTestDetailsTable(atr_loadTestDetails.objects.filter(
            Q(page_links__contains=query) | Q(status__contains=query) | Q(browser__contains=query) | Q(
                hw_info__contains=query) | Q(run_time__contains=query) | Q(last_run_date__contains=query) | Q(
                link__contains=query) | Q(result_history__contains=query)) \
                                           .filter(id=pk))
        return render(request, 'users/loadTestDetails.html',
                      {'table': results, 'name': testname, 'name_details': name_details, 'pk':pk})

global a



#this views is for clearfilter view
def sort(request):
    # print("search view called")
    template = 'users/loadTest.html'
    table = atr_loadTestDetailsTable(atr_loadTestDetails.objects.all())
    pk=request.session['rk']
    testname = ATR.objects.get(id=pk)
    name_details = atr_loadTestDetails.objects.all()
    table = atr_loadTestDetailsTable(atr_loadTestDetails.objects.all())
    RequestConfig(request).configure(table)
    table_list = atr_loadTestDetails.objects.all()

    return render(request, 'users/loadTestDetails.html',
                  {'table': table, 'name': testname, 'name_details': name_details, 'pk':pk})

def Export(request):
    pk=request.session['rk']
    name = ATR.objects.get(id=pk)
    queryset = atr_loadTestDetails.objects.get(id=pk)
    # print(queryset)
    qs = atr_loadTestDetails.objects.filter(id=pk).values('id', 'page_links','status','run_time','last_run_date')

    return render_to_csv_response(qs,filename=name.name)


