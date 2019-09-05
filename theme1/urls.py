from django.urls import path

from theme1.views import theme1_view, create_theme1, view_theme1, theme1_console, list_theme

urlpatterns =[
    path('list/core', list_theme, name='list_theme'),
    path('theme1', theme1_view , name='theme1_view'),
    path('theme1/create', create_theme1, name='create_theme1'),
    path('theme1/view/<int:id>', view_theme1, name='view_theme1'),
    path('theme1/console/<int:id>/', theme1_console , name='theme1_console'),
]