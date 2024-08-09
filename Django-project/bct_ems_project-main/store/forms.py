# employees/forms.py
#💻💻💻🔴
#you will find forms._(..something) in my html pages..that is possible because of forms.py
#look closely that forms is imported from django

from django import forms
from .models import Employee
from .models import Department, Position

class EmployeeForm(forms.ModelForm):
    class Meta:
        #taken from Employee model
        model = Employee
        #all fields are editable
        fields = ['first_name', 'last_name', 'email', 'department', 'position', 'date_hired']
    

class DepartmentForm(forms.ModelForm):
    class Meta:
        #taken from Department model
        model = Department
        #only name is editable
        fields = ['name']

class PositionForm(forms.ModelForm):
    class Meta:
        #taken from Position model
        model = Position
        #only title and department are editable
        fields = ['title', 'department']



#This area is extremly highly syntax dependent ...edit with caution


