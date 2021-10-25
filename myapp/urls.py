
from django.contrib import admin
from django.urls import path
from .views import index, AddStudent, login_page, user_logout, assign, invoice

urlpatterns = [
    path('', index, name='index'),
    path('add/', AddStudent, name='AddStudent'),
    path('login/', login_page, name='login'),
    path('logout/', user_logout, name='logout'),
    path('assign/', assign, name='assign'),
    path('invoice/', invoice, name='invoice'),


]
