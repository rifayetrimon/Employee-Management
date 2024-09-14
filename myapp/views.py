from django.shortcuts import render, redirect
from . forms import EmployeeForm
from django.http import HttpResponse
from .models import Employee
# Create your views here.



################### Index for home
def index(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})


################### Add Employee
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse(form.errors, status=400)
    else:
        form = EmployeeForm()
        return render(request, 'add_employee.html', {'form': form})
    

################### Details
def details(request, pk):
    employee = Employee.objects.get(pk=pk)
    return render(request, 'details.html', {'employee': employee})


################### management
def management(request):
    employees = Employee.objects.all()
    return render(request, 'management.html', {'employees': employees})


################### update
def update(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee, is_update=True)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse(form.errors, status=400)
    else:
        form = EmployeeForm(instance=employee, is_update=True)
        return render(request, 'update.html', {'form': form})




