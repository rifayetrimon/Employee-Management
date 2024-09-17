from django import forms
from .models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'address', 'phone_number', 'salary', 'designation', 'description']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full h-12 pl-4 pr-4 rounded-lg border border-gray-300',  
                'placeholder': 'Enter full name',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full h-12 pl-4 pr-4 rounded-lg border border-gray-300',  
                'placeholder': 'Enter address',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full h-12 pl-4 pr-4 rounded-lg border border-gray-300',  
                'placeholder': 'Enter phone number',
            }),
            'salary': forms.NumberInput(attrs={
                'class': 'form-input mt-1 block w-full h-12 pl-4 pr-4 rounded-lg border border-gray-300',
                'placeholder': '$ Enter salary',
            }),
            'designation': forms.Select(attrs={
                'class': 'border-gray-300 rounded-md p-2 w-full',
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-input mt-1 block w-full h-12 pl-4 pr-4 rounded-lg border border-gray-300',
                'placeholder': 'Enter a brief profile summary',
                'rows': 1,
            }),
        }

    def __init__(self, *args, **kwargs):
        is_update = kwargs.pop('is_update', False)
        super(EmployeeForm, self).__init__(*args, **kwargs)

        if is_update:
            self.fields['salary'].widget.attrs['readonly'] = True
            self.fields['designation'].disabled = True

    def clean_designation(self):
        return self.initial['designation']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-input mt-2 block w-full bg-white border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base py-2 px-3',
                'placeholder': 'Enter your username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input mt-2 block w-full bg-white border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base py-2 px-3',
                'placeholder': 'Enter your email'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-input mt-2 block w-full bg-white border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base py-2 px-3',
                'placeholder': 'Enter your password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-input mt-2 block w-full bg-white border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base py-2 px-3',
                'placeholder': 'Confirm your password'
            }),
        }

    # def __init__(self, *args, **kwargs):
    #     is_update = kwargs.pop('is_update', False)
    #     super(CustomUserCreationForm, self).__init__(*args, **kwargs)
    #     self.fields['password1'].disabled = True
    #     self.fields['password2'].disabled = True
    
    # def clean_password1(self):
    #     return self.initial['password1']

    # def clean_password2(self):
    #     return self.initial['password2']





class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input mt-2 block w-full bg-white border border-gray-300 rounded-lg py-2 px-3',
        'placeholder': 'Enter your username',
        'autofocus': True
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input mt-2 block w-full bg-white border border-gray-300 rounded-lg py-2 px-3',
        'placeholder': 'Enter your password',
    }))