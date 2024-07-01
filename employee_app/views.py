from django.shortcuts import render, HttpResponse
from .models import Department, Role, Employee
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
  return render(request,'index.html')

def all_emp(request):
  emps=Employee.objects.all()
  context = {
    'emps':emps
  }
  return render(request,'View_emp.html', context)

def add_emp(request):
  if request.method =='POST':
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    dept=int(request.POST['dept'])
    salary=int(request.POST['salary'])
    bonus=int(request.POST['bonus'])
    role=int(request.POST['role'])
    phone=int(request.POST['phone'])
    new_emp=Employee(first_name=first_name, last_name=last_name, dept_id=dept, salary=salary, bonus=bonus, role_id=role,phone=phone, hire_date=datetime.now()) 
    new_emp.save()
    return HttpResponse("New Employee Added Successfully")
  elif request.method=='GET':  
    return render(request,'add_emp.html')
  else:
    return HttpResponse("Error")  

def filter(request):
  if request.method =='POST':
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    dept=int(request.POST['dept'])
    role=int(request.POST['role'])
    emps=Employee.objects.all()
    if name:
      emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
    if dept:
      emps=emps.filter(dept__name__icontains=dept) 
    if role:
      emps=emps.filter(dept__name__icontains=role) 
    context = {
    'emps':emps
  }  
    return render(request,'view_emp.html', context)
  elif request.method=='GET':   
    return render(request,'filter_emp.html')
  else:
    return HttpResponse("Error")   

def delete_emp(request, emp_id=0):
  if emp_id:
    try:
      emp_to_be_removed=Employee.objects.get(id=emp_id)
      emp_to_be_removed.delete()
      return HttpResponse("Employee removed succeswsfully")
    except:
      return HttpResponse("Error")    
  emps=Employee.objects.all()
  context = {
    'emps':emps
  }
  return render(request,'delete_emp.html',context)      