from django.db import models
from django.contrib.auth.models import User


class EmpData(models.Model):
    issue_choice = [
        ('cleared', 'cleared'),
        ('pending', 'pending'),
        ('flagged', 'flagged'),
    ]

    emp_nid = models.CharField(max_length=12, verbose_name='ID Number')
    emp_name = models.CharField(max_length=250, verbose_name='Name')
    issue = models.CharField(max_length=200, choices=issue_choice)
    remarks = models.TextField(max_length=500, verbose_name='Remark')
    date = models.DateField(auto_now_add=True)
    data_entry_person = models.ForeignKey(User, on_delete=models.CASCADE)


class Company(models.Model):
    comp_name = models.CharField(max_length=200, verbose_name="Name")

    def __str__(self):
        return f"{self.comp_name}"


class DataEntryOperator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
