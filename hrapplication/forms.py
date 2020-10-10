from django.contrib import admin
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django import forms

from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'email': None,
            'password2': None,
        }


class AssignCompanyForm(ModelForm):
    class Meta:
        model = DataEntryOperator
        fields = ['user', 'company']


class AddCompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['comp_name']
