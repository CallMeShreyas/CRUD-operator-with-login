from django.contrib import admin
from django.urls import path, include
from superuser import views

urlpatterns = [
    path('', views.superlogin),
    path('superlogin_index', views.superlogin_index),
    path('work_add', views.work_add),
    path('work_add_status', views.work_add_status),
    path('work_edit/<int:id>', views.work_edit),
    path('work_update/<int:id>', views.work_update),
    path('work_delete/<int:id>', views.work_delete),
    path('superlogin_index/updated', views.updated),
    path('superlogin_index/work_delete/<int:id>', views.work_delete),
    path('superlogin_index/work_update/<int:id>', views.work_update),
    path('superlogin_index/work_add/<int:id>', views.work_add),
    path('superlogin_index/work_edit/<int:id>', views.work_edit),
    path('work_addpoint/<int:id>', views.work_addpoint),
    path('work_addpoint_status/<int:id>', views.work_addpoint_status),
    path('work_withdraw/<int:id>', views.work_withdraw),
    path('work_withdraw_status/<int:id>', views.work_withdraw_status),

    path('superlogin_index/work_addpoint/<int:id>', views.work_addpoint),
    path('superlogin_index/work_addpoint_status/<int:id>', views.work_addpoint_status),
    path('superlogin_index/work_withdraw/<int:id>', views.work_withdraw),
    path('superlogin_index/work_withdraw_status/<int:id>', views.work_withdraw_status),
]
