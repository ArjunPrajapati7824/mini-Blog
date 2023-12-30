from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name="home"),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
    path('dashboard',dashboard,name="dashboard"),
    path('signup',signup,name="signup"),
    path('login',user_login,name="login"),
    path('logout',user_logout,name="logout"),     
    path('logout',user_logout,name="logout"),     
    path('add',add_post,name="add"),     
    path('update/<int:id>',update_post,name="update"),     
    path('delete/<int:id>',delete,name="delete"),     
]
