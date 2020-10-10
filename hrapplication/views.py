from django.contrib import messages
from django.contrib.auth.models import *
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *


# Create your views here.

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("system_admin")
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'login_page.html')


def logoutUser(request):
    logout(request)
    return redirect("login")


def logoutUser(request):
    logout(request)
    return redirect("login")


def AdminPage(request):
    form = CreateUserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    form = CreateUserForm(None)

    form2 = AddCompanyForm(request.POST or None)
    if request.method == 'POST':
        if form2.is_valid():
            form2.save()
    form2 = AddCompanyForm(None)

    userlist = User.objects.all()

    context = {'form': form, 'form2': form2, 'userlist': userlist}
    return render(request, 'admin_interface.html', context)


def DataEntryPage(request):
    return render(request, 'data_entry_interface.html')


def TestLayout(request):
    return render(request, 'test_layout.html')
