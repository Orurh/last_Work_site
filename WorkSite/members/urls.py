from django.urls import path, include

from . import admin, views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('addpage/', views.addpage, name='addpage'),
    path('contact/', views.contact, name='contact'),
    path('members/<slug:post_slug>/', views.members, name='members'),
    path('categories/<slug:cat_slug>/', views.categories, name='categories'),
    path('tag/<slug:tag_slug>/', views.tags_list, name='tag'),
]
