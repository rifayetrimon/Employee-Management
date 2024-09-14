from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'address', 'phone_number', 'salary', 'designation', 'description']

        # Adding custom widgets to form fields
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
            self.fields['designation'].widget.attrs['disabled'] = True



