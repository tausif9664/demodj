# Generated by Django 3.2.10 on 2021-12-23 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='h_form',
            name='assigned',
            field=models.CharField(blank=True, choices=[['tausif', 'tausif'], ['NewUser', 'NewUser'], ['NewUser2', 'NewUser2'], ['tonystark', 'tonystark'], ['tausif1', 'tausif1'], ['tausif2', 'tausif2'], ['NewVision', 'NewVision'], ['admin', 'admin']], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='h_form',
            name='history_date',
            field=models.CharField(blank=True, default='23/12/2021, 20:26:50', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hatr',
            name='assigned',
            field=models.CharField(blank=True, choices=[['tausif', 'tausif'], ['NewUser', 'NewUser'], ['NewUser2', 'NewUser2'], ['tonystark', 'tonystark'], ['tausif1', 'tausif1'], ['tausif2', 'tausif2'], ['NewVision', 'NewVision'], ['admin', 'admin']], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hatr',
            name='history_date',
            field=models.CharField(blank=True, default='23/12/2021, 20:26:50', max_length=100, null=True),
        ),
    ]
