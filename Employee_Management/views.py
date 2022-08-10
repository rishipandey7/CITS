from django.shortcuts import render, HttpResponse
from .models import Employee ,Department , Role
from datetime import datetime
from django.db.models import Q
# Create your views here.


def index(request):
    return render(request,'index.html')


def view_emp(request):
    
    emps = Employee.objects.all()

    params = {'emp':emps}

    return render(request,'view_emp.html',params)

def remove_emp(request, empid = 0):

    emps = Employee.objects.all()
    params = {'emp':emps}
    
    if empid :
        emps = Employee.objects.filter(id = empid)
        emps.delete()
        return HttpResponse("deleted sucessfully")

    return render(request,'remove_emp.html',params)

def add_emp(request):

    if request.method == "POST":
        Fname = request.POST['Fname']
        Lname = request.POST['Lname']
        dept = request.POST['dept']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        role = request.POST['role']
        phone = request.POST['phone']

        employee = Employee(Fname = Fname,Lname = Lname, dept_id = dept, salary = salary,bonus = bonus,role_id = role,phone= phone,hire_date = datetime.now())
        employee.save()

        return HttpResponse("Employee added succesfully")
    elif request.method == "GET":
        return render(request,'add_emp.html')    
    else:
        return HttpResponse("Error Occured try again")

    return render(request,'add_emp.html')    


def filter_emp(request):

    if request.method == "POST":
        name = request.POST['Fname']
        dept = request.POST['dept']
        role = request.POST['role']

        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(Fname__icontains = name) | Q(Lname__icontains = name))
        if dept:
            emps = emps.filter(Q(dept__name = dept))
        if role:
            emps = emps.filter(Q(role__name = role))

        params = {'emp':emps}
        return render(request,'view_emp.html',params)

    return render(request,'filter_emp.html')