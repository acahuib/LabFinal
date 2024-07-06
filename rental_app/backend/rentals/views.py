# backend/rentals/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Costume, Rental
from .forms import CostumeForm, RentalForm

class CostumeListView(ListView):
    model = Costume

class CostumeDetailView(DetailView):
    model = Costume

class CostumeCreateView(CreateView):
    model = Costume
    form_class = CostumeForm
    # Ajusta las redirecciones según tus necesidades
    success_url = '/'

class CostumeUpdateView(UpdateView):
    model = Costume
    form_class = CostumeForm
    # Ajusta las redirecciones según tus necesidades
    success_url = '/'

class CostumeDeleteView(DeleteView):
    model = Costume
    # Ajusta las redirecciones según tus necesidades
    success_url = '/'

class RentalListView(ListView):
    model = Rental

class RentalDetailView(DetailView):
    model = Rental

class RentalCreateView(CreateView):
    model = Rental
    form_class = RentalForm
    # Ajusta las redirecciones según tus necesidades
    success_url = '/'

class RentalUpdateView(UpdateView):
    model = Rental
    form_class = RentalForm
    # Ajusta las redirecciones según tus necesidades
    success_url = '/'

class RentalDeleteView(DeleteView):
    model = Rental
    # Ajusta las redirecciones según tus necesidades
    success_url = '/'

