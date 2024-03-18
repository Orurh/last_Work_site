from django.urls import path, include

from members import admin, views

urlpatterns = [
    path('', views.MemberHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('addpage/', views.AddPage.as_view(), name='addpage'),
    path('contact/', views.contact, name='contact'),
    path('members/<slug:post_slug>/', views.Members.as_view(), name='members'),
    path('categories/<slug:cat_slug>/', views.MemberCategory.as_view(), name='categories'),
    path('tag/<slug:tag_slug>/', views.MemberTag.as_view(), name='tag'),
    path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'),
    path('delete/<slug:slug>/', views.DeletePage.as_view(), name='delete_page'),

]

