from django.urls import path

from Company.views import index, create, console, view, delete, tools

app_name = 'company'

urlpatterns =[
    path('company/sample', index, name='index'),
    path('company/create', create, name='create'),
    path('company/console/<str:Project_Name>', console, name='console'),
    path('company/<str:Project_Name>', view, name='view'),
    path('company/tools/<str:Project_Name>', tools, name='tools'),
    path('company/delete/<str:Project_Name>', delete, name='delete')
]