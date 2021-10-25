from django.shortcuts import render, redirect
from .models import *
from .form import StudentRegister, CoursesAssign, InvoiceForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def index(request):
    student = Candidate.objects.all()
    context = {
        'student':student,

    }
    return render(request,'index.html', context)


@login_required
def AddStudent(request):
    form = StudentRegister()
    data = CoursesAssign()
    if request.method == 'POST':
        form = StudentRegister(request.POST)
        data = CoursesAssign(request.POST)
        if form.is_valid() and data.is_valid():
            form.save() and data.save()
            return redirect('/')
    context = {
        'form': form,
        'data':data
    }
    return render(request, 'add.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('AddStudent')
        else:
            messages.info(request, 'Username Or Password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('index')


@login_required
def assign(request):
    data = CoursesAssign()
    if request.method == 'POST':
        data = CoursesAssign(request.POST)
        if data.is_valid():
            data.save()
            return redirect('index')

    context = {'data':data}

    return render(request, 'assign.html', context)


def invoice(request):
    student = Candidate.objects.all()
    form = InvoiceForm()
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form':form, 'student':student}
    return render(request,'invoice.html', context)
