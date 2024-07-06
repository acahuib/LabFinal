from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Costume, Rental

class CostumeListView(ListView):
    model = Costume
    template_name = 'rentals/costume_list.html'  # Crear esta plantilla luego
    context_object_name = 'costumes'

class CostumeDetailView(DetailView):
    model = Costume
    template_name = 'rentals/costume_detail.html'  # Crear esta plantilla luego
    context_object_name = 'costume'

class CostumeCreateView(CreateView):
    model = Costume
    template_name = 'rentals/costume_form.html'  # Crear esta plantilla luego
    fields = ['name', 'description', 'available']
    success_url = reverse_lazy('costume-list')

class CostumeUpdateView(UpdateView):
    model = Costume
    template_name = 'rentals/costume_form.html'  # Crear esta plantilla luego
    fields = ['name', 'description', 'available']
    success_url = reverse_lazy('costume-list')

class CostumeDeleteView(DeleteView):
    model = Costume
    template_name = 'rentals/costume_confirm_delete.html'  # Crear esta plantilla luego
    success_url = reverse_lazy('costume-list')

class RentalListView(ListView):
    model = Rental
    template_name = 'rentals/rental_list.html'  # Crear esta plantilla luego
    context_object_name = 'rentals'

class RentalDetailView(DetailView):
    model = Rental
    template_name = 'rentals/rental_detail.html'  # Crear esta plantilla luego
    context_object_name = 'rental'

class RentalCreateView(CreateView):
    model = Rental
    template_name = 'rentals/rental_form.html'  # Crear esta plantilla luego
    fields = ['costume', 'customer_name', 'rental_date', 'return_date', 'returned']
    success_url = reverse_lazy('rental-list')

class RentalUpdateView(UpdateView):
    model = Rental
    template_name = 'rentals/rental_form.html'  # Crear esta plantilla luego
    fields = ['costume', 'customer_name', 'rental_date', 'return_date', 'returned']
    success_url = reverse_lazy('rental-list')

class RentalDeleteView(DeleteView):
    model = Rental
    template_name = 'rentals/rental_confirm_delete.html'  # Crear esta plantilla luego
    success_url = reverse_lazy('rental-list')

