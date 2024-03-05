
# from .models import atr_loadTestDetails, hATR, ATR,logs,h_form,Chart,Release,Test_Env,StageNext_Env,Prod_Env
def file():
    pk = 235
    name = "Sample Test"
    with open("C:\\Users\\tausif.tamboli\\Downloads\\"+name+ '.log', 'r') as link_file:
        a = link_file.readlines()
        # print("a",a)
        for line in a[1:]:
            # print(line)
            if line.startswith("PASSED") or line.startswith("REDIRECT") or line.startswith("NOT_FOUND") or line.startswith("DENIED") or line.startswith("ERROR") :
                if line.startswith("PASSED=") or line.startswith("REDIRECT(") or line.startswith("NOT_FOUND=") or line.startswith("DENIED=") or line.startswith("ERROR="):
                    continue
                # print(line.rstrip())
                p = line.rstrip().split()
                # print("p:",p)
                for links in p:
                    if links.startswith("/"):
                        link = links
                        print("link:",link) #link
                    try:
                        if links.startswith("Perf-time"):
                            time = links.split(":")
                            t = ":"
                            runtime = t.join(time[1:])
                            # print("time:", runtime)
                            print("Perf-time:", runtime)  # runtime

                            if runtime == "-1":
                                day = line.rstrip().split()[4]
                                times = line.rstrip().split()[5]
                                runtime = runtime[1:] + day +times
                                print("Perf-time new_runtime:", runtime) # runtime

                    except:
                        pass

                # print(line.rstrip().split())
                status = line.rstrip().split()[0]

                s = line.rstrip().split()[1:3]
                rundate = " "
                rundate = rundate.join(s)
                print("rundate:",rundate)  #Rundate
                print("status", status)  # status
                print("runtime:", runtime)
                print("link:", link)  # link
                print('\n')
                # print(line.rstrip().split()[3])
                # print(line.rstrip().split()[3].split(':')[1:])

file()
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
# import django
# django.setup()
# from django_project import settings
# from django.db.migrations.state import ModelState
# from django.db.migrations import operations
# from django.db.migrations.migration import Migration
# from django.db import connections
# from django.db.migrations.state import ProjectState

# from os import getenv
# import pymssql
import pyodbc, csv
def connect():
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 13 for SQL server};server=172.40.0.5;database=FCIDUI_30;uid=puneusers;PWD=pune@users!123;')
        print(conn)
        cursor = conn.cursor()
        print("OK")
        with open("C:\\Users\\tausif.tamboli\\Downloads\\db_STAGENEXT_CRM_PAGELOAD_TEST"+ '.txt', 'r') as link_file:
            a = link_file.readline()  #insert header in tables
            b = link_file.readlines()   #insert data in tables

            print("First:",a[0])
            print("First:", b[0].rstrip().split(',')[0])
            print("First:", b[0].rstrip().split(',')[1])
        cursor.execute("""
        IF OBJECT_ID('persons', 'U') IS NOT NULL
            DROP TABLE persons
        CREATE TABLE persons (
            id INT NOT NULL,
            """+ str(a.split(',')[0].rstrip())  +""" VARCHAR(100),
            """+ str(a.split(',')[1].rstrip())  +""" VARCHAR(100),
            """+ str(a.split(',')[2].rstrip())  +""" VARCHAR(100),
            """+ str(a.split(',')[3].rstrip())  +""" VARCHAR(100),
            """+ str(a.split(',')[4].rstrip())  +""" VARCHAR(100),
            """+ str(a.split(',')[5].rstrip())  +""" VARCHAR(100),
            """+ str(a.split(',')[6].rstrip())  +""" VARCHAR(100),

            PRIMARY KEY(id)
        )
        """)
        cursor.executemany(
            "INSERT INTO persons VALUES (?, ?, ?, ?, ?, ?, ?)",
            [(1, 'ME', 'OTHERME'),
             (2, 'ANOTHERGUY', 'GUY'),
             (3, 'NAME', 'SURNAME')])
        conn.commit()

connect()








# def get_create_sql_for_model(model):
#
#     model_state = ModelState.from_model(model)
#
#     # Create a fake migration with the CreateModel operation
#     cm = operations.CreateModel(name=model_state.name, fields=model_state.fields)
#     migration = Migration("fake_migration", "app")
#     migration.operations.append(cm)
#
#     # Let the migration framework think that the project is in an initial state
#     state = ProjectState()
#
#     # Get the SQL through the schema_editor bound to the connection
#     connection = connections['default']
#     with connection.schema_editor(collect_sql=True, atomic=migration.atomic) as schema_editor:
#         state = migration.apply(state, schema_editor, collect_sql=True)
#
#     # return the CREATE TABLE statement
#     return "\n".join(schema_editor.collected_sql)
#
# if __name__ == "__main__":
#
#     import importlib
#     import sys
#
#     if len(sys.argv) < 2:
#         print("Usage: {} <app.model>".format(sys.argv[0]))
#         sys.exit(100)
#
#     app, model_name = sys.argv[1].split('.')
#
#     models = importlib.import_module("{}.models".format(app))
#     model = getattr(models, model_name)
#     rv = get_create_sql_for_model(model)
#     print(rv)