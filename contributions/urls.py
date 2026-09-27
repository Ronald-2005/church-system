from django.urls import path
from . import views

app_name = 'contributions'

urlpatterns = [
    path('', views.ContributionListView.as_view(), name='list'),
    path('add/', views.ContributionCreateView.as_view(), name='add'),
    path('receipt/<int:contribution_id>/', views.generate_receipt, name='generate_receipt'),
]
