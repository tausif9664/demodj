# Generated by Django 2.1.15 on 2020-01-31 05:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_matplotlib.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ATR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='TEST NAME')),
                ('test_status', models.CharField(blank=True, max_length=100, null=True, verbose_name='STATUS')),
                ('run_date', models.CharField(blank=True, max_length=100, verbose_name='LAST RUN DATE')),
                ('run_time', models.CharField(blank=True, max_length=100, null=True, verbose_name='RUN TIME')),
                ('link', models.CharField(blank=True, max_length=100, null=True, verbose_name='TOTAL LINK PASSED')),
                ('creation_date', models.CharField(max_length=100, null=True, verbose_name='CREATED_DATE')),
                ('exe_test', models.CharField(blank=True, max_length=100, null=True, verbose_name='Exec Test')),
                ('result_history', models.TextField(blank=True, max_length=1000, null=True, verbose_name='History')),
                ('results', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='atr_loadTestDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LinkPath', models.CharField(blank=True, max_length=1000, null=True, verbose_name='PAGE LINKS')),
                ('status', models.CharField(blank=True, max_length=100, null=True, verbose_name='STATUS')),
                ('StartTime', models.CharField(blank=True, max_length=100, null=True, verbose_name='StartTime')),
                ('EndTime', models.CharField(blank=True, max_length=100, null=True, verbose_name='EndTime')),
                ('Baseline', models.CharField(blank=True, max_length=100, null=True, verbose_name='Baseline')),
                ('CurrentRunDateTime', models.CharField(blank=True, max_length=100, null=True, verbose_name='CurrentRunDateTime')),
                ('testId', models.CharField(blank=True, db_column='#testId', max_length=100, null=True)),
                ('result_history', models.TextField(blank=True, max_length=1000, null=True, verbose_name='History')),
            ],
        ),
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('development_fixes', models.IntegerField(blank=True)),
                ('qa_verfication', models.IntegerField(blank=True)),
                ('regection_rate', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=255)),
                ('notes', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='h_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history_date', models.CharField(blank=True, default='30/01/2020, 23:39:48', max_length=100, null=True)),
                ('assigned', models.CharField(blank=True, choices=[['automation', 'automation'], ['Admin', 'Admin'], ['asekhar', 'asekhar']], max_length=100, null=True)),
                ('status', models.CharField(blank=True, choices=[('Open', 'Open'), ('Close', 'Close'), ('Inprogress', 'Inprogress')], max_length=100, null=True)),
                ('date_assign', models.DateField(blank=True, null=True)),
                ('days', models.CharField(blank=True, max_length=100, null=True)),
                ('h_a', models.TextField(blank=True, max_length=1000, null=True)),
                ('ATR', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='ATR.name', to='users.ATR')),
                ('user_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='hATR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history_date', models.CharField(blank=True, default='30/01/2020, 23:39:48', max_length=100, null=True)),
                ('assigned', models.CharField(blank=True, choices=[['automation', 'automation'], ['Admin', 'Admin'], ['asekhar', 'asekhar']], max_length=100, null=True)),
                ('status', models.CharField(blank=True, choices=[('Open', 'Open'), ('Close', 'Close'), ('Inprogress', 'Inprogress')], max_length=100, null=True)),
                ('date_assign', models.DateField(blank=True, null=True)),
                ('days', models.CharField(blank=True, max_length=100, null=True)),
                ('h_a', models.TextField(blank=True, max_length=1000, null=True)),
                ('ATR', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='ATR.name', to='users.ATR')),
                ('user_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.TextField(max_length=1000)),
                ('ATR_log', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='ATR.name', to='users.ATR')),
            ],
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('figure', django_matplotlib.fields.MatplotlibFigureField()),
            ],
        ),
        migrations.CreateModel(
            name='Prod_Env',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('App', models.CharField(max_length=100, verbose_name='App')),
                ('Regrations_details', models.CharField(default='-', max_length=100, verbose_name='Regression Tests Details')),
                ('No_of_tests', models.IntegerField(verbose_name='# of Tests')),
                ('Passed', models.FloatField(blank=True, null=True, verbose_name='Passed %')),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('App', models.CharField(max_length=100, verbose_name='App')),
                ('Release_date', models.DateField(blank=True, null=True, verbose_name='Release date')),
                ('No_items', models.IntegerField(blank=True, null=True, verbose_name='#No Items')),
                ('Status', models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='StageNext_Env',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('App', models.CharField(max_length=100, verbose_name='App')),
                ('Regrations_details', models.CharField(default='-', max_length=100, verbose_name='Regression Tests Details')),
                ('No_of_tests', models.IntegerField(verbose_name='# of Tests')),
                ('Passed', models.FloatField(blank=True, null=True, verbose_name='Passed %')),
            ],
        ),
        migrations.CreateModel(
            name='Test_Env',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('App', models.CharField(max_length=100, verbose_name='App')),
                ('Regrations_details', models.CharField(default='-', max_length=100, verbose_name='Regression Tests Details')),
                ('No_of_tests', models.IntegerField(verbose_name='# of Tests')),
                ('Passed', models.FloatField(blank=True, null=True, verbose_name='Passed %')),
            ],
        ),
    ]