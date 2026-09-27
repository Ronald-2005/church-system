from django.urls import path
from . import views

app_name = 'ministries'

urlpatterns = [
    path('', views.ministry_list, name='ministry_list'),
    path('add/', views.ministry_create, name='ministry_add'),
    path('edit/<int:pk>/', views.ministry_edit, name='ministry_edit'),
    path('delete/<int:pk>/', views.ministry_delete, name='ministry_delete'),
    path('request-join/<int:pk>/', views.request_join_ministry, name='request_join'),
    path('pending-requests/', views.pending_requests, name="pending_requests"),
    path('approve-request/<int:req_pk>/', views.approve_request, name='approve_request'),
    path('reject-request/<int:req_pk>/', views.reject_request, name='reject_request'),


    # ✅ SLUG MUST ALWAYS BE LAST
    path('<slug:slug>/', views.ministry_detail, name='ministry_detail'),
]