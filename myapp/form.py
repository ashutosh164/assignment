from django import forms
from .models import *


class StudentRegister(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['name', 'email', 'phone']


class CoursesAssign(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['candidate_name', 'course_name', 'total_fees', 'date_of_joining']


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'