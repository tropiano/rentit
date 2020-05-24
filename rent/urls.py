from django.urls import path

from . import views

app_name = 'rent'
urlpatterns = [
    path('', views.house_list, name='index'),
]
