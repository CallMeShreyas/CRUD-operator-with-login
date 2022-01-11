from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    path('login', views.login),
    path('signup', views.signup),
    path('signup_index', views.signup_index),
    path('login_index', views.login_index),
    path('work_add', views.work_add),
    path('work_add_status', views.work_add_status)
]
