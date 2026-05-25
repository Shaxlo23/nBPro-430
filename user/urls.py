from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)
from .forms import LoginForm
from . import views

urlpatterns = [
    path('', views.home_view,name='home_view'),
    path('register/', views.register_view,name='register'),
    path('login/',LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('user/create/', views.user_create,name='user_create'),
    path('user/<slug:slug>/', views.user_view,name='user_view'),
    path('user/update/<slug:slug>/', views.user_update,name='user_update'),
    path('user/delete/<slug:slug>/', views.user_delete,name='user_delete'),
    path('profile/', views.profile_view,name='profile'),
    path('profile/edit/', views.profile_edit_view,name='profile_edit'),
    path('profile/delete/', views.profile_delete_view,name='profile_delete'),
]