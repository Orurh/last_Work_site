from django.urls import path, include

from . import admin, views

urlpatterns = [
    path('', views.index, name='fire_home'),
]