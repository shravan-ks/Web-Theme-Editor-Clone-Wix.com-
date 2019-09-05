from django.urls import path
from core.views import indexweb, dashboard, search_themes, notify, updateuser

app_name = 'core'

urlpatterns =[
    path('', indexweb, name='indexweb'),
    path('dashboard', dashboard, name='dashboard'),
    path('search/themes', search_themes, name='search_themes'),
    path('notification', notify, name='notify'),
    path('profile/<str:username>/', updateuser, name='updateuser'),


]