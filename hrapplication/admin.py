from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *


# inline admin descriptor for employee model
class DataEntryOperatorInline(admin.StackedInline):
    model = DataEntryOperator
    can_delete = False
    verbose_name_plural = 'Data Entry Person'


# define new UserAdmin
class UserAdmin(BaseUserAdmin):
    inlines = (DataEntryOperatorInline,)


# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(EmpData)
admin.site.register(Company)
