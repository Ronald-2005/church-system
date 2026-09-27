from django.urls import path
from .views import (
    AnnouncementListView,
    AnnouncementDetailView,
    AnnouncementCreateView,
    AnnouncementUpdateView,
    AnnouncementDeleteView
)

app_name = 'announcements'

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announcement_list'),
    path('<int:pk>/', AnnouncementDetailView.as_view(), name='announcement_detail'),
    path('add/', AnnouncementCreateView.as_view(), name='announcement_add'),
    path('edit/<int:pk>/', AnnouncementUpdateView.as_view(), name='announcement_edit'),
    path('delete/<int:pk>/', AnnouncementDeleteView.as_view(), name='announcement_delete'),
]
