from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/', views.member_dashboard, name='member_dashboard'),
    path('list/', views.member_list, name='members_list'),
    path('detail/<int:pk>/', views.member_detail, name='member_detail'),
     path('', views.member_list, name='member_list'),
    path('<int:pk>/', views.member_detail, name='member_detail'),
    path('add/', views.member_create, name='member_add'),
    path('<int:pk>/edit/', views.member_edit, name='member_edit'),
    path('<int:pk>/delete/', views.member_delete, name='member_delete'),
]
