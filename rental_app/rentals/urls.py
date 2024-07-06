from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CostumeViewSet, RentalViewSet
from . import views

router = DefaultRouter()
router.register(r'costumes', CostumeViewSet)
router.register(r'rentals', RentalViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('costumes/', views.CostumeListView.as_view(), name='costume-list'),
    path('costumes/<int:pk>/', views.CostumeDetailView.as_view(), name='costume-detail'),
    path('costumes/new/', views.CostumeCreateView.as_view(), name='costume-create'),
    path('costumes/<int:pk>/edit/', views.CostumeUpdateView.as_view(), name='costume-update'),
    path('costumes/<int:pk>/delete/', views.CostumeDeleteView.as_view(), name='costume-delete'),
    path('rentals/', views.RentalListView.as_view(), name='rental-list'),
    path('rentals/<int:pk>/', views.RentalDetailView.as_view(), name='rental-detail'),
    path('rentals/new/', views.RentalCreateView.as_view(), name='rental-create'),
    path('rentals/<int:pk>/edit/', views.RentalUpdateView.as_view(), name='rental-update'),
    path('rentals/<int:pk>/delete/', views.RentalDeleteView.as_view(), name='rental-delete'),
]

