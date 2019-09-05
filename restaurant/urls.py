from django.urls import path

from restaurant.views import index, create, console, view, tools, delete

app_name = 'restaurant'

urlpatterns =[
    path('restaurant/sample', index, name='index'),
    path('restaurant/create', create, name='create'),
    path('restaurant/console/<str:projectname>', console, name='console'),
    path('restaurant/<str:projectname>', view, name='view'),
    path('restaurant/tools/<str:projectname>', tools, name='tools'),
    path('restaurant/delete/<str:projectname>', delete, name='delete')
]