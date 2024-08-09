# employees/urls.py
#imports
from django.urls import path
from . import views

#urls
urlpatterns = [
    #These urls are for the employees
    path('', views.employee_list, name='employee_list'),
    path('employee/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employee/new/', views.employee_create, name='employee_create'),
    path('employee/<int:pk>/edit/', views.employee_update, name='employee_update'),
    path('employee/<int:pk>/delete/', views.employee_delete, name='employee_delete'),


    #These urls are for the departments
    path('departments/', views.department_list, name='department_list'),
    path('departments/new/', views.department_create, name='department_create'),
    path('departments/<int:pk>/edit/', views.department_update, name='department_update'),
    path('departments/<int:pk>/delete/', views.department_delete, name='department_delete'),


    #These urls are for the positions
    path('positions/', views.position_list, name='position_list'),
    path('positions/new/', views.position_create, name='position_create'),
    path('positions/<int:pk>/edit/', views.position_update, name='position_update'),
    path('positions/<int:pk>/delete/', views.position_delete, name='position_delete'),
]
