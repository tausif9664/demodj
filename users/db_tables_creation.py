import pyodbc, csv,datetime
import datetime as p
from datetime import timedelta,datetime
a=str(p.datetime.today())
print("DATE:", a)
Pre_Hour=datetime.strftime(datetime.now() - timedelta(hours=1), '%Y-%m-%d %H')
Pre_date=datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
print("Pre_date",Pre_date)
print("Pre_Hour",Pre_Hour)
print("Pre_date",type(Pre_date))
print("Pre_Hour",type(Pre_Hour))
# l="db_STAGENEXT_CRM_PAGELOAD_TEST"
l="Prod_SCC_MGR_PAGELOAD_TEST"
def connect():

        conn = pyodbc.connect(
            # 'DRIVER={ODBC Driver 13 for SQL server};server=192.168.8.20;database=FCIDUI;uid=sa;PWD=!nd!a0ffice@2020;')
        'DRIVER={ODBC Driver 13 for SQL server};server=192.168.8.20;database=FCID_Automation;uid=sa;PWD=!nd!a0ffice@2020')

        print(conn)
        cursor = conn.cursor()
        print("OK")
        # with open("C:\\Users\\tausif.tamboli\\Downloads\\"+l+ '.txt', 'r') as link_file:
        #     a = link_file.readline()  #insert header in tables
        #     b = link_file.readlines()   #insert data in tables
        #     print("A:", a)
        #     c= list()
        #
        #
        #     def get_sec(time_str):
        #             """Get Seconds from time."""
        #             h, m, s = time_str.split(':')
        #             return int(h) * 3600 + int(m) * 60 + int(s)
        #
        #     c = len(b)
        #     time = []
        #     for e in range(c-1):
        #         t1 = (b[e].split(',')[2])
        #         t2 = (b[e].split(',')[3])
        #         t4 = get_sec(t2)
        #         t3 = get_sec(t1)
        #         t = int(t4) - int(t3)
        #         print("StartTime:", t4)
        #         print("EndTime:", t3)
        #         print("Time:", t)
        #         time.append(t)
        #     print("time:",time)
        #     # a.append("PrefTime")
        #     # for g in range(len(b)):
        #     #     print("B:",list(b[g]).append(b[g].split(',')[0]))
        #     # print("b")
        #     c=len(b)
        #     y = list()
        #     w = y [1:]
        #     print("c:",c)
        #     for z in range (c):
        #         y.append(z)
        #     print("Y",y[1:])
        #
        # cursor.execute("""
        # IF OBJECT_ID('"""+l+"""', 'U') IS NOT NULL
        #     DROP TABLE """+l+"""
        # CREATE TABLE """+l+""" (
        #     id INT NOT NULL,
        #     """+ str(a.split(',')[0].rstrip())  +""" VARCHAR(100),
        #     """+ str(a.split(',')[1].rstrip())  +""" VARCHAR(100),
        #     """+ str(a.split(',')[2].rstrip())  +""" VARCHAR(100),
        #     """+ str(a.split(',')[3].rstrip())  +""" VARCHAR(100),
        #     """+ str(a.split(',')[4].rstrip())  +""" VARCHAR(100),
        #     """+ str(a.split(',')[5].rstrip())  +""" VARCHAR(100),
        #     """+ str(a.split(',')[6].rstrip())  +""" VARCHAR(100),
        #     blank VARCHAR(100),
        #     PerfTime VARCHAR(100),
        #
        # )
        # """)
        # a=1
        #
        # for n in b[:-1]:
        #
        #
        #     # print("N", str(n))
        #     p = n.rstrip().split(',')
        #     d = list(p)
        #     d.insert(0, a)
        #     d.insert(9, time[a-1])
        #     print("DD:", d)
        #     a = a + 1
        #     # print("d",d)
        #
        # # for n in b[:-1] :
        # #     print("TY",n)
        # #     # a=int(n.rstrip())
        # #     p = n.rstrip().split(',')
        # #     d = list(p)
        # #     d.insert(9, time[0])
        # #     print("DD:",d)
        #
        #
        #     cursor.executemany(
        #         "INSERT INTO "+l+" VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        #             [tuple(d)])
        #     conn.commit()
        # for x in range (24):
        #     print("X", x)
        #
        #
        #     Pre_date = datetime.strftime(datetime.now() - timedelta(x), '%Y-%m-%d')
        #     print("Pre_date1:", Pre_date)
        #     cursor.execute('select * from '+l+'  where CurrentRunDateTime LIKE \'%'+Pre_date+'%\'')
        #     data = cursor.fetchall()
        #
        #     if len(data)>1 :
        #         print("DATA3:", data)
        #         break;
        #
        #
        # print("DATA1:",data )
connect()
# print("P:",p)
#     # conn = pyodbc.connect(
#     #     'DRIVER={ODBC Driver 13 for SQL server};server=172.40.0.5;database=FCIDUI_30;uid=puneusers;PWD=pune@users!123;')
#     # print(conn)
#     # cursor = conn.cursor()
#     # print("OK")
#     # with open("C:\\Users\\tausif.tamboli\\Downloads\\db_STAGENEXT_CRM_PAGELOAD_TEST" + '.txt', 'r') as link_file:
#     #     a = link_file.readline()  # insert header in tables
#     #     b = link_file.readlines()  # insert data in tables
#     #     c = len(b)
#     #     y = list()
#     #     w = y[1:]
#     #     print("c:", c)
#     #     for z in range(c):
#     #         y.append(z)
#     #     print("Y", y[1:])
#
#         # for x in (b[0:-1]):
#         #         p = x.rstrip().split(',')
#         #         d = tuple(p)
#         #         a=1
#         #         if a==1:
#         #             for y in d:
#         #                 print(f"d[0]",y)
#         #                 a=2
#     ################################
#
#     #############################
#
#     # print("3:",type (d[0]) )
#     # for x in d, y:
#     # print("n:",n)
#     # b[0]=list(b[0].rstrip().split(',')[0])
#     # print("b[0]:",b[0])
#     #         #
#     # cursor.execute("""
#     #         IF OBJECT_ID('""" + l + """', 'U') IS  NULL
#     #
#     #         CREATE TABLE """ + l + """ (
#     #             id INT NOT NULL,
#     #             """ + str(a.split(',')[0].rstrip()) + """ VARCHAR(100),
#     #             """ + str(a.split(',')[1].rstrip()) + """ VARCHAR(100),
#     #             """ + str(a.split(',')[2].rstrip()) + """ VARCHAR(100),
#     #             """ + str(a.split(',')[3].rstrip()) + """ VARCHAR(100),
#     #             """ + str(a.split(',')[4].rstrip()) + """ VARCHAR(100),
#     #             """ + str(a.split(',')[5].rstrip()) + """ VARCHAR(100),
#     #             """ + str(a.split(',')[6].rstrip()) + """ VARCHAR(100),
#     #             blank VARCHAR(100),
#     #
#     #         )
#     #         """)
#     # a = 1
#     # for n in b[:-1]:
#     #     print("N", str(n))
#     #     p = n.rstrip().split(',')
#     #     d = list(p)
#     #     d.insert(0, a)
#     #     a = a + 1
#     #     print("d:", d)
#     #
#     #     cursor.executemany(
#     #         "INSERT INTO " + l + " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
#     #         [tuple(d)])
#     #     conn.commit()
#     # conn = pyodbc.connect(
#     #     'DRIVER={ODBC Driver 13 for SQL server};server=172.40.0.5;database=FCIDUI_30;uid=puneusers;PWD=pune@users!123;')
#     # print(conn)
#     # cursor = conn.cursor()
#     # print("OK")
#     # with open("C:\\Users\\tausif.tamboli\\Downloads\\db_STAGENEXT_CRM_PAGELOAD_TEST"+'.txt', 'r') as link_file:
#     #     a = link_file.readline()  #insert header in tables
#     #     b = link_file.readlines()   #insert data in tables
#     #     c=len(b)
#     #     y = list()
#     #     w = y [1:]
#     #     print("c:",c)
#     #     for z in range (c):
#     #         y.append(z)
#     #     print("Y",y[1:])
#     #
#     # cursor.execute("""
#     #         IF OBJECT_ID('db_STAGENEXT_CRM_PAGELOAD_TEST', 'U') IS NULL
#     #         CREATE TABLE """+ p +""" (
#     #             id INT NOT NULL,
#     #             """+ str(a.split(',')[0].rstrip())  +""" VARCHAR(100),
#     #             """+ str(a.split(',')[1].rstrip())  +""" VARCHAR(100),
#     #             """+ str(a.split(',')[2].rstrip())  +""" VARCHAR(100),
#     #             """+ str(a.split(',')[3].rstrip())  +""" VARCHAR(100),
#     #             """+ str(a.split(',')[4].rstrip())  +""" VARCHAR(100),
#     #             """+ str(a.split(',')[5].rstrip())  +""" VARCHAR(100),
#     #             """+ str(a.split(',')[6].rstrip())  +""" VARCHAR(100),
#     #             blank VARCHAR(100),
#     #
#     #         )
#     #         """)
#     # a=1
#     # for n in b[:-1]:
#     #     print("N", str(n))
#     #     p = n.rstrip().split(',')
#     #     d = list(p)
#     #     d.insert(0, a)
#     #     a = a + 1
#     #     print("d:", d)
#     #
#     #     cursor.executemany(
#     #         "INSERT INTO db_STAGENEXT_CRM_PAGELOAD_TEST VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
#     #         [tuple(d)])
#     #     conn.commit()
#     import datetime as p
#     from datetime import timedelta, datetime
#     print("DATE:", str(p.datetime.today()))
#     Pre_Hour = datetime.strftime(datetime.now() - timedelta(hours=1), '%Y-%m-%d %H')
#     Pre_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
#     print("Pre_date", Pre_date)
#     print("Pre_Hour", Pre_Hour)
#     print("Pre_date", type(Pre_date))
#     print("Pre_Hour", type(Pre_Hour))
#     l = "db_STAGENEXT_CRM_PAGELOAD_TEST"
#     # l = "Prod_SCC_MGR_PAGELOAD_TEST"
#     conn = pyodbc.connect(
#         'DRIVER={ODBC Driver 13 for SQL server};server=172.40.0.5;database=FCIDUI_30;uid=puneusers;PWD=pune@users!123;')
#     print(conn)
#     cursor = conn.cursor()
#     print("OK")
#     with open("C:\\Users\\tausif.tamboli\\Downloads\\" + l + '.txt', 'r') as link_file:
#         a = link_file.readline()  # insert header in tables
#         b = link_file.readlines()  # insert data in tables
#         c = len(b)
#         y = list()
#         w = y[1:]
#         print("c:", c)
#         for z in range(c):
#             y.append(z)
#         print("Y", y[1:])
#
#         # for x in (b[0:-1]):
#         #         p = x.rstrip().split(',')
#         #         d = tuple(p)
#         #         a=1
#         #         if a==1:
#         #             for y in d:
#         #                 print(f"d[0]",y)
#         #                 a=2
#     ################################
#
#     #############################
#
#     # print("3:",type (d[0]) )
#     # for x in d, y:
#     # print("n:",n)
#     # b[0]=list(b[0].rstrip().split(',')[0])
#     # print("b[0]:",b[0])
#     #         #
#     cursor.execute("""
#             IF OBJECT_ID('""" + l + """', 'U') IS NULL
#
#             CREATE TABLE """ + l + """ (
#                 id INT NOT NULL,
#                 """ + str(a.split(',')[0].rstrip()) + """ VARCHAR(100),
#                 """ + str(a.split(',')[1].rstrip()) + """ VARCHAR(100),
#                 """ + str(a.split(',')[2].rstrip()) + """ VARCHAR(100),
#                 """ + str(a.split(',')[3].rstrip()) + """ VARCHAR(100),
#                 """ + str(a.split(',')[4].rstrip()) + """ VARCHAR(100),
#                 """ + str(a.split(',')[5].rstrip()) + """ VARCHAR(100),
#                 """ + str(a.split(',')[6].rstrip()) + """ VARCHAR(100),
#                 blank VARCHAR(100),
#
#             )
#             """)
#     a = 1
#     for n in b[:-1]:
#         print("N", str(n))
#         p = n.rstrip().split(',')
#         d = list(p)
#         d.insert(0, a)
#         a = a + 1
#         print("d:", d)
#
#         cursor.executemany(
#             "INSERT INTO " + l + " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
#             [tuple(d)])
#         conn.commit()
#     for x in range(365):
#         try:
#             Pre_date = datetime.strftime(datetime.now() - timedelta(hours=x), '%Y-%m-%d')
#             cursor.execute('select * from ' + l + '  where CurrentRunDateTime LIKE \'%' + Pre_date + '%\'')
#             # declearation of the global variable
#
#             # All Data fetching in a variable data
#             data = cursor.fetchall()
#             print("DATA:", data)
#             for row in data:
#                 f1 = row[2]
#                 print("F1", f1)
#             break;
#         except:
#             Pre_date = datetime.strftime(datetime.now() - timedelta(x), '%Y-%m-%d')
#             cursor.execute(
#                 'select * from ' + l + '  where CurrentRunDateTime LIKE \'%' + Pre_date + '%\'')
#             # declearation of the global variable
#
#             # All Data fetching in a variable data
#             data = cursor.fetchall()
#             # x = list(data)
#             #
#             # # print("DATA:",x )
#             # print("DATA:",x[0][0])
#             for row in data:
#                 f1 = row[2]
#                 # print(f1)
#             # print("DATA:",x(0))
#             # print("DATA:", x[0][0])
#             break;
#
#         for x in range(365):
#             try:
#                 from datetime import datetime
#                 Pre_date = datetime.strftime(datetime.now() - timedelta(hours=x), '%Y-%m-%d')
#                 cursor.execute(
#                     'select * from db_STAGENEXT_CRM_PAGELOAD_TEST  where CurrentRunDateTime LIKE \'%' + Pre_date + '%\'')
#                 data = cursor.fetchall()
#                 break;
#             except:
#                 from datetime import datetime
#                 Pre_date = datetime.strftime(datetime.now() - timedelta(x), '%Y-%m-%d')
#                 cursor.execute(
#                     'select * from db_STAGENEXT_CRM_PAGELOAD_TEST where CurrentRunDateTime LIKE \'%' + Pre_date + '%\'')
#
#                 data = cursor.fetchall()
#                 break;
#         # inner_qs = Prod_SCC_MGR_PAGELOAD_TEST.objects.all()
#             table = atr_loadTestDetailsTable(data)
#             RequestConfig(request, paginate={'per_page': 500}).configure(table)
#             return render(request, 'users/loadTestDetails.html',
#                           {'table': table, 'name': name, 'pk':pk})
#
#
#         table = atr_loadTestDetailsTable(data)
#         RequestConfig(request, paginate={'per_page': 500}).configure(table)
#         return render(request, 'users/loadTestDetails.html',
#                       {'table': table, 'name': name, 'pk':pk})