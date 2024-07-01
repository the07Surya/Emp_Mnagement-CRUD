from . import views
from django.urls import path
urlpatterns = [
 path('', views.index, name='index'),
 path('view_emp/', views.all_emp, name='all_emp'),
 path('add_emp/', views.add_emp, name='add_emp'),
 path('filter_emp/', views.filter, name='filter_emp'),
  path('delete_emp/', views.delete_emp, name='delete_emp'),
 path('delete_emp/<int:emp_id>', views.delete_emp, name='delete_emp'),
]