from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('add_emp', views.add_emp,name="add_emp"),
    path('remove_emp', views.remove_emp,name="remove_emp"),
    path('remove_emp/<int:empid>', views.remove_emp,name="remove_emp"),
    path('view_emp', views.view_emp,name="view_emp"),               
    path('filter_emp', views.filter_emp,name="filter_emp"),               
]
