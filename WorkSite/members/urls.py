from django.urls import path, include

from . import admin, views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('addpage/', views.addpage, name='addpage'),
    path('contact/', views.contact, name='contact'),
    path('members/<int:int_id>/', views.members, name='members'),
    path('categories/<int:cat_id>/', views.categories, name='categories'),
]
