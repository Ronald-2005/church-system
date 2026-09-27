from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),

    # Dashboards
    path('member_dashboard/', views.member_dashboard, name='member_dashboard'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
