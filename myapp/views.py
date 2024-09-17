from django.shortcuts import render, redirect
from . forms import EmployeeForm, CustomUserCreationForm, CustomAuthenticationForm
from django.http import HttpResponse
from .models import Employee
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.



################### Index for home
@login_required
def index(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})


################### Add Employee
@login_required
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
@login_required
def details(request, pk):
    employee = Employee.objects.get(pk=pk)
    return render(request, 'details.html', {'employee': employee})


################### management
@login_required
def management(request):
    employees = Employee.objects.all()
    return render(request, 'management.html', {'employees': employees})


################### update
@login_required
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



################## delete
@login_required
def delete(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('management')
    

################## Register
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid data! Please check the form.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


################## Login
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=user_name, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


################## login 
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



################## Profile 
@login_required
def profile(request):
    return render(request, 'profile.html')






