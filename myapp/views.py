from django.shortcuts import render, redirect
from .models import *
from .form import StudentRegister, CoursesAssign, InvoiceForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone



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
    # student = Candidate.objects.all()
    enrol = Enrollment.objects.all()
    form = InvoiceForm()
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            inv = form.save()
            subject = 'Assignment-Submission'
            message = f'Hi {inv.candidate}I hope you’re well.' \
                      f' We have yet to receive payment of {inv.amount} for invoice number' \
                      f' 001 for enrollment_id- {inv.enrollment_id}, which was due on ' \
                      f'{timezone.now()}. Please let us know when we can expect to receive payment, ' \
                      'and don’t hesitate to reach out if you have any questions or concerns.'
            email_from = settings.EMAIL_HOST_USER
            student = Candidate.email
            recipent_list = [student, ]
            # send_mail(subject, message, email_from, recipent_list)
            return redirect('index')

    context = {'form':form, 'enrol':enrol}
    return render(request,'invoice.html', context)











