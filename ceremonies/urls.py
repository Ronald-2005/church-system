from django.urls import path
from .views import (
    CeremonyListView,
    CeremonyDetailView,  # ✅ Include this line
    CeremonyCreateView,
    CeremonyUpdateView,
    CeremonyDeleteView,
)

app_name = 'ceremonies'

urlpatterns = [
    path('', CeremonyListView.as_view(), name='ceremony_list'),
    path('add/', CeremonyCreateView.as_view(), name='add_ceremony'),
    path('edit/<int:pk>/', CeremonyUpdateView.as_view(), name='edit_ceremony'),
    path('delete/<int:pk>/', CeremonyDeleteView.as_view(), name='delete_ceremony'),
    path('<int:pk>/', CeremonyDetailView.as_view(), name='ceremony_detail'),  # ✅ Add this
]
