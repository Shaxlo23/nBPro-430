from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_view,name='users_view'),
    path('user/create/', views.user_create,name='user_create'),
    path('user/<slug:slug>/', views.user_view,name='user_view'),
    path('user/update/<slug:slug>/', views.user_update,name='user_update'),
    path('user/delete/<slug:slug>/', views.user_delete,name='user_delete'),
]