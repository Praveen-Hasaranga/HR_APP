# Generated by Django 3.1.2 on 2020-10-08 03:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_nid', models.CharField(max_length=12, verbose_name='ID Number')),
                ('emp_name', models.CharField(max_length=250, verbose_name='Name')),
                ('issue', models.CharField(choices=[('cleared', 'cleared'), ('pending', 'pending'), ('flagged', 'flagged')], max_length=200)),
                ('remarks', models.TextField(max_length=500, verbose_name='Remark')),
                ('date', models.DateField(auto_now_add=True)),
                ('data_entry_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]