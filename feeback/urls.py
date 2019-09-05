from django.urls import path

from feeback.views import feedback, thankyou

app_name = 'feedback'

urlpatterns =[
    path('feedback', feedback, name='feedback'),
    path('feedback/thankyou', thankyou, name='thankyou'),


]