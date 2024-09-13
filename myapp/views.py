from django.shortcuts import render
from . forms import EmployeeForm
# Create your views here.


def index(request):
    return render(request, 'home.html')


def add_employee(request):
    form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})