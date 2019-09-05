from django.urls import path

from crud.views import list_crud, create_crud, update_crud, delete_crud

urlpatterns =[
    path('list', list_crud, name='list_crud'),
    path('new', create_crud, name='create_crud'),
    path('update/<int:id>/', update_crud, name='update_crud'),
    path('delete/<int:id>', delete_crud,name='delete_crud' )
]