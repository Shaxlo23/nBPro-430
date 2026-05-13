from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view,name='home_view'),
    path('register/', views.register_view,name='register'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
    path('profile/', views.profile_view,name='profile'),
    # path('users/', views.users_view,name='users_view'),
    path('user/create/', views.user_create,name='user_create'),
    path('user/<slug:slug>/', views.user_view,name='user_view'),
    path('user/update/<slug:slug>/', views.user_update,name='user_update'),
    path('user/delete/<slug:slug>/', views.user_delete,name='user_delete'),
]