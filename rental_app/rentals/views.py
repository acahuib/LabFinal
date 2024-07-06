# rentals/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Costume, Rental
from .forms import CostumeForm, RentalForm

class CostumeListView(ListView):
    model = Costume

class CostumeDetailView(DetailView):
    model = Costume

class CostumeCreateView(CreateView):
    model = Costume
    template_name = 'rentals/costume_form.html'
    form_class = CostumeForm
    success_url = reverse_lazy('costume-list')

class CostumeUpdateView(UpdateView):
    model = Costume
    template_name = 'rentals/costume_form.html'
    form_class = CostumeForm
    success_url = reverse_lazy('costume-list')

class CostumeDeleteView(DeleteView):
    model = Costume
    success_url = reverse_lazy('costume-list')

class RentalListView(ListView):
    model = Rental

class RentalDetailView(DetailView):
    model = Rental

class RentalCreateView(CreateView):
    model = Rental
    template_name = 'rentals/rental_form.html'
    form_class = RentalForm
    success_url = reverse_lazy('rental-list')

class RentalUpdateView(UpdateView):
    model = Rental
    template_name = 'rentals/rental_form.html'
    form_class = RentalForm
    success_url = reverse_lazy('rental-list')

class RentalDeleteView(DeleteView):
    model = Rental
    success_url = reverse_lazy('rental-list')

