from django.urls import path, include

from . import admin, views
from .views import FireHome

urlpatterns = [
    path('', views.index, name='fire_home'),
    path('<slug:fire_slug>/', FireHome.as_view(), name='fires')
]