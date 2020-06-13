from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from . import views

app_name = 'homePage'

urlpatterns = [
    path('',views.home,name= 'home'),
    path('test/',views.test,name="test"),
    ]
