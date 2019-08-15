from django.urls import path
from zhouzhengyang import views

app_name = 'zhouzhengyang'

urlpatterns = [
    path('index/', views.index, name='index')
]