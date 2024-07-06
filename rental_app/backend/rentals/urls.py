# backend/rentals/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.CostumeListView.as_view(), name='costume-list'),
    path('costume/<int:pk>/', views.CostumeDetailView.as_view(), name='costume-detail'),
    path('costume/new/', views.CostumeCreateView.as_view(), name='costume-create'),
    path('costume/<int:pk>/edit/', views.CostumeUpdateView.as_view(), name='costume-update'),
    path('costume/<int:pk>/delete/', views.CostumeDeleteView.as_view(), name='costume-delete'),
    path('rentals/', views.RentalListView.as_view(), name='rental-list'),
    path('rental/<int:pk>/', views.RentalDetailView.as_view(), name='rental-detail'),
    path('rental/new/', views.RentalCreateView.as_view(), name='rental-create'),
    path('rental/<int:pk>/edit/', views.RentalUpdateView.as_view(), name='rental-update'),
    path('rental/<int:pk>/delete/', views.RentalDeleteView.as_view(), name='rental-delete'),
]

