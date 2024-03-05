from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect,get_object_or_404
from bs4 import BeautifulSoup
from djqscsv import render_to_csv_response
from django.db.models.query import QuerySet
import pandas as pd
from django.contrib.auth.models import User
from django.template import loader
import os
import py
from .models import ATR_FT, atr_FTloadTestDetails
from .tables import ATR_FT_Table
from django.contrib import messages
# from .forms import UserRegisterForm,AssignForm,ExportResource
# from .models import atr_loadTestDetails, hATR, ATR,logs,h_form
# from .tables import ATRTable
# from .tables import atr_loadTestDetailsTable
from django_tables2 import RequestConfig
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import csv, io,time
from datetime import date
from django.db.models import Q
import datetime
from .tables import ATR_FT_Table
from .models import ATR_FT
from.tables import atr_FTloadTestDetailsTable


#### Path for files #####
# test_path='D:\\Zip files\\FoodchainAutomation\\Tests\\'
# D:\Zip files\FoodchainAutomation\Tests\TEST_A020_SCC_CertificateInsertEdit.py
# D:\FCIDWebFormsAutomation\Tests\TEST_F002_FCIDWEB_Pt_Br_Contact.py
test_path="D:\\FCIDWebFormsAutomation\\Tests\\"
# test_path="D:\\FoodchainAutomation\\Tests\\"

test_path="C:\\AutomationUITests\\Tests\\"

csv_path='C:\\AutomationUITests\\Tests\\csv_files\\'
log_path='C:\\AutomationUITests\\Tests\\log_files\\'

# Create your views here.


#### Create your user registration here. ####
#
# #### loadTestDetails_id page view for loadTestDetails page ####
#@login_required()
def fcidwebsitetestDetails_id(request, pk):
    ####
    pk = pk
    global id_atr
    id_atr = pk
    fcidwebsitetestDetails_id.ids_atr=pk
    request.session['rk'] = pk
    name = ATR_FT.objects.get(id=pk)
    atr_details = atr_FTloadTestDetails(id=pk,run_time=name.run_time, last_run_date=name.run_date, status=name.test_status,
                                      page_links=name.name)
    atr_details.save()
    name_details = atr_FTloadTestDetails.objects.get(id=pk)
    name_details.run_time = name.run_time
    name_details.last_run_date = name.run_date
    name_details.status = name.test_status
    name_details.page_links = name.name
    name_details.id = name.id

    name_details.save()
    table = atr_FTloadTestDetailsTable(atr_FTloadTestDetails.objects.all())
    RequestConfig(request).configure(table)

    table = atr_FTloadTestDetailsTable(atr_FTloadTestDetails.objects.filter(id=pk))
    RequestConfig(request, paginate={'per_page': 2}).configure(table)
    return render(request, 'fcidwebsitetest/FTtestDetails.html',
                  {'table': table, 'name': name, 'name_details': name_details, 'pk':pk})

# global forms
# global Assigned
# global d
#
#@login_required()
def history_FT(request,pk):
    d=None
    try:
        try:
            p = h_form_FT.objects.get(id=pk)
        except:
            p = h_form_FT.objects.get(id=pk + 62) or h_form_FT.objects.get(id=pk)
        form = AssignForm(instance=p)
    except:
        form=AssignForm()
    f_forms=form

    if request.method == "POST":
        try:
            try:
                instance = h_form_FT.objects.get(id=pk)
            except:
                instance = h_form_FT.objects.get(id=pk + 62) or h_form_FT.objects.get(id=pk)
            form = AssignForm(request.POST, instance=instance)
        except:
            form = AssignForm(request.POST)
        if form.is_valid():
            try:
                assigned=form.cleaned_data.get('assigned')
                status=form.cleaned_data.get('status')
                date_assign=form.cleaned_data.get('date_assign')
                a = ATR_FT.objects.get(id=pk)
                user = request.user
                a = ATR_FT.objects.get(id=pk)
                print('is valid ')
                users = h_form_FT.objects.all()
    ##############################################################################
                dt = datetime.date.today()
                dc = dt.strftime("%m/%d/%Y")
                print(dc, 'd')
                print(dt, 'dt')
                datetime_object1 = datetime.datetime.strptime(dc, '%m/%d/%Y')
                datetime_object2 = datetime.datetime.strptime(str(date_assign), '%Y-%m-%d')
                print()
                p = (datetime_object1 - datetime_object2).days
                print(p)
                c = p
                print("DAYS: ",p)
                Assign = h_form_FT.objects.all()
                Assigned = h_form_FT.objects.first()
                hist = hATR_FT.objects.all()
                user = request.user
                users = User.objects.values_list('username', flat=True)
                try:
                    print("data update")
                    print(len(h_form_FT.objects.filter(id=pk)),":length")
                    b=1

                    try:
                        if  len(h_form_FT.objects.filter(id=pk)) != 0 :
                            form_history = h_form_FT.objects.filter(id=pk)\
                                .update(assigned=assigned, status=status, date_assign=date_assign, ATR_FT=a, days=p,user_names_FT=user)
                            print("data update successfully")
                        else:
                            print("Add new data entry")
                            form_history = h_form_FT.objects.filter(id=pk) \
                                .create(assigned=assigned, status=status, date_assign=date_assign, ATR_FT=a, days=p,
                                        user_names_FT=user)
                            print("data added successfully")
                    except:
                        pass
                    # a.save()

                except:
                    pass
                hform_history = hATR_FT(history_date=datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),assigned=assigned, status=status, date_assign=date_assign, ATR_FT=a, days=p, user_names_FT=user)
                hform_history.save()
                ATR_id = ATR_FT.objects.all()
                j = 0
                try:
                    for a in ATR_id:
                        if pk == a.id:
                            for i in Assign:
                                if i.ATR.id == a.id:

                                    if j == 0:
                                        print(i.days)
                                        d = i.days
                                        j = 1
                                        if i.status != "Open":
                                            d = "NA"
                                        if int(i.days) < 0:
                                            d = "NA"

                except:
                    pass
                return render(request, 'fcidwebsitetest/history_FT.html',
                              {'user': user, 'users': users, 'hist': hist, 'Assign': Assign, 'form': form,
                               'ATR_id': ATR_id, 'pk': pk, 'p': p, 'Assigned': Assigned, 'd': d})


            except:
                try:
                    try:
                        p = h_form_FT.objects.get(id=pk)
                    except:
                        p = h_form_FT.objects.get(id=pk + 62) or h_form_FT.objects.get(id=pk)
                    form = AssignForm(instance=p)
                except:
                    form = AssignForm()
                Assign = h_form_FT.objects.all()
                Assigned = h_form_FT.objects.first()
                ATR_id = ATR_FT.objects.all()
                # log_id = logs.objects.all()
                hist = hATR_FT.objects.all()
                table = ATR_FT_Table(ATR_FT.objects.all())
                RequestConfig(request).configure(table)
                try:
                    result_history = request.POST["history"]
                except:
                    result_history=" "
                a = ATR_FT.objects.get(id=pk)
                hform_history = hATR_FT(history_date=datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),h_a=result_history, ATR_FT=a, user_names_FT=user, date_assign=date.today(),
                                                    assigned=status,
                                                    status=status)
                hform_history.save()
                return render(request, 'fcidwebsitetest/history_FT.html',
                              {'user': user, 'users': users, 'hist': hist, 'Assign': Assign, 'form': form,
                               'ATR_id': ATR_id, 'pk': pk,  'Assigned': Assigned, 'd': d})

    Assign = h_form_FT.objects.all()
    Assigned = h_form_FT.objects.first()
    p=None
    try:
        p = h_form_FT.objects.get(id=pk)
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
    ATR_id = ATR_FT.objects.all()
    # log_id = logs.objects.all()
    hist = hATR_FT.objects.all()
    table = ATR_FT_Table(ATR_FT.objects.all())
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
                            print(d, 'd')
                            print(dt, 'dt')
                            datetime_object1 = datetime.datetime.strptime(d, '%m/%d/%Y')
                            datetime_object2 = datetime.datetime.strptime(str(p), '%Y-%m-%d')
                            print()
                            d = (datetime_object1 - datetime_object2).days

                            print(d)
                            # d=i.days
                            j=1
                            if i.status != "Open":
                                d="NA"
                            if int(i.days) < 0:
                                d="NA"

    except:
        pass

    return render(request, 'fcidwebsitetest/history_FT.html',{'user': user, 'users': users, 'hist': hist, 'Assign': Assign, 'form': form, 'ATR_id': ATR_id,'pk': pk, 'p': p, 'Assigned': Assigned, 'd': d})

#
# #### Log Function #####
# def log(request,pk):
#     pk=pk
#     ATR_id = ATR.objects.all()
#     log_id = logs.objects.all()
#     hist = hATR.objects.all()
#     table = ATRTable(ATR.objects.all())
#     RequestConfig(request).configure(table)
#     name = ATR.objects.get(id=pk)
#     fileName = log_path + name.name + ".log"
#     with open(fileName) as f:
#         b = f.readlines()
#
#     response_content = b
#     t = loader.get_template('users/log.html')
#     c = {'pk': pk,'b':b}
#     return HttpResponse(t.render(c,request),content_type="text/plain")
#
#@login_required()
def fcidwebsitetest(request):
    ATR_FT_id = ATR_FT.objects.all()
    # pks = ATR_FT.objects.all()[ :1].get()
    # pk = pks.id  ####initiai Id to remove 404 not found error
    # log_id = logs.objects.all()
    # hist = hATR_FT.objects.all()
    # table = ATR_FTTable(ATR_FT.objects.all())
    table = ATR_FT_Table(ATR_FT.objects.all())
    RequestConfig(request).configure(table)
    # print("fcidwebsitetest")

    return render(request,"fcidwebsitetest/FTtests.html", {'table': table, 'ATR_FT_id': ATR_FT_id

                                                           } )
#
#
# ########LOG view for log file #########
# #@csrf_exempt
def results_FT(request,pk):
    pk=pk
    table = ATR_FT_Table(ATR_FT.objects.all())
    RequestConfig(request).configure(table)
    name = ATR_FT.objects.get(id=pk)

    if request.method == 'POST':
        request.session['pk'] = pk
        fileName = log_path+name.name+".log"
        print(name.name)
        with open(fileName) as f:
            b=f.readlines()

        response_content = b
        responce= HttpResponse(response_content, content_type="text/plain")
    return responce


###################
##This function for database entry from server via socket and render to loadtest page
##################


#@csrf_exempt
def recup_wos_FT(request,pk):
#########template section query##after Run button click

    testname = ATR_FT.objects.get(id=pk)
    testname='a'
    ATR_id = ATR_FT.objects.all()
    hist = hATR_FT.objects.all()
    table = ATR_FT_Table(ATR_FT.objects.all())
    RequestConfig(request).configure(table)
########
    global id_atr
    id_atr=pk
    name = ATR_FT.objects.get(id=pk)
    # testcaseFullPath=test_path+name.name+'.py'
    if request.method == 'POST':
        a=ATR_FT.objects.get(id=pk)
        a.run_date=date.today()
        a.save()
        try:
            if (csv_path+name.name+".csv" is not None):
                os.remove(csv_path+name.name+".csv")
                print("file deleted")
        except:
            pass
        try:
            args_str = "--html=report.html --self-contained-html --excelreport="+csv_path+name.name+".xls "+test_path+name.name+".py"
            # args_str ="-v -s --csv "+csv_path+name.name+".csv "+test_path+name.name+".py"
            print(args_str)
            py.test.cmdline.main(args_str.split(" "))
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
                print(err)
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
            print(data_set)
            io_string = io.StringIO(data_set)
            next(io_string)

            try:
                for column in csv.reader(io_string, delimiter=','):

                        # created=ATR.objects.update_or_create
                        _, created=ATR_FT.objects.filter(pk=id_atr).update(
                            ##id = column[0],
                            test_status = column[4],
                            run_time = column[5][0:8],

                        )

            except:

                return redirect('fcidwebsitetest')

            csv_file.close()
        except:
            return redirect('fcidwebsitetest')
        context = {}
        table = ATR_FT_Table(ATR_FT.objects.all())
        RequestConfig(request).configure(table)
        a=zip(ATR_id,hist)
        time.sleep(3)

        return render(request, 'fcidwebsitetest/FTtests.html',
                      {'table': table, 'name': testname, 'ATR_id': ATR_id, 'a': a})

    return redirect('fcidwebsitetest')
#
#
# #search field for load test details page
# def search(request):
#     print("search view called")
#     template = 'users/loadTest.html'
#     pk=request.session['rk']
#     query = request.GET.get('q')
#     testname = ATR.objects.get(id=pk)
#     name_details = atr_loadTestDetails.objects.all()
#     table = atr_loadTestDetailsTable(atr_loadTestDetails.objects.all())
#     RequestConfig(request).configure(table)
#     table_list = atr_loadTestDetails.objects.all()
#     if query=="":
#         print("blank")
#         table = atr_loadTestDetailsTable(atr_loadTestDetails.objects.filter(id=pk))
#         return render(request, 'users/loadTestDetails.html',
#                       {'table': table, 'name': testname, 'name_details': name_details, 'pk': pk})
#     else:
#         print("not blank")
#         results = atr_loadTestDetailsTable(atr_loadTestDetails.objects.filter(
#             Q(page_links__contains=query) | Q(status__contains=query) | Q(browser__contains=query) | Q(
#                 hw_info__contains=query) | Q(run_time__contains=query) | Q(last_run_date__contains=query) | Q(
#                 link__contains=query) | Q(result_history__contains=query))\
#                                                    .filter(id=pk))
#         return render(request, 'users/loadTestDetails.html',
#                       {'table': results, 'name': testname, 'name_details': name_details, 'pk':pk})
#
# global a
#
# #@login_required()
# def welcome(request ,id=None):
#     return render(request, 'users/welcome.html')
#
# #this views is for clearfilter view
# def sort(request):
#     print("search view called")
#     template = 'users/loadTest.html'
#     table = atr_loadTestDetailsTable(atr_loadTestDetails.objects.all())
#     pk=request.session['rk']
#     testname = ATR.objects.get(id=pk)
#     name_details = atr_loadTestDetails.objects.all()
#     table = atr_loadTestDetailsTable(atr_loadTestDetails.objects.all())
#     RequestConfig(request).configure(table)
#     table_list = atr_loadTestDetails.objects.all()
#
#     return render(request, 'users/loadTestDetails.html',
#                   {'table': table, 'name': testname, 'name_details': name_details, 'pk':pk})
#



