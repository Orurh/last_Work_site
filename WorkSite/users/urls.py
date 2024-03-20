from django.urls import path, include
from django.contrib.auth.views import LogoutView

from . import admin, views

app_name = 'users'

urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]