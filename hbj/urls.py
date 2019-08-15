from django.urls import path
from hbj import views

app_name = 'hbj'

urlpatterns = [

    path('hbj/',views.hbj,name='hbj')
]