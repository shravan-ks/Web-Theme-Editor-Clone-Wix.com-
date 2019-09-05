from django.urls import path

from resume.views import index, create, console, view, delete, tools

app_name = 'resume'

urlpatterns =[
    path('resume/sample', index, name='index'),
    path('resume/create', create, name='create'),
    path('resume/console/<str:Project_Name>', console, name='console'),
    path('resume/<str:Project_Name>', view, name='view'),
    path('resume/tools/<str:Project_Name>', tools, name='tools'),
    path('resume/delete/<str:Project_Name>', delete, name='delete')
]