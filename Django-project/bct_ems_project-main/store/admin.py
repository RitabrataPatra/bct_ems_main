# employees/admin.py

from django.contrib import admin
from .models import Employee, Department, Position

# Registering the models here to show them in the admin panel
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Position)

