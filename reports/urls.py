from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('', views.report_home, name='report_home'),
    path('membership/', views.membership_report, name='membership_report'),
    path('membership/download/', views.download_membership_report, name='download_membership_report'),

    path('contributions/', views.contribution_report, name='contribution_report'),
    path('contributions/download/', views.download_contribution_report, name='download_contribution_report'),
]
