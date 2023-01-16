from django.urls import path
from EmployeeApp import views

urlpatterns = [
    path('',views.ApiOverview, name="api_overview"),
    path('all/',views.view_depData, name="get_department_data"),
    path('add/',views.add_depData, name="add_department_data"),
    path('update/<int:pk>/',views.update_depData,name="update_department_data"),
    path('delete/<int:pk>/',views.delete_depData,name='delete_department_data'), 

    path('allemp/',views.viewOrAddEmployeeDetail,name='emp_data'),
    path('update/delete/<int:pk>/',views.updateOrDeleteEmployeeDetail,name="update_Employee_data"),
]
