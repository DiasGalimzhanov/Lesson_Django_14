from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Car
from .forms import CarForm
from django.urls import reverse_lazy

class List(ListView):
    model = Car
    template_name = 'home.html'
    context_object_name = 'cars'

class Create(CreateView):
    model = Car
    template_name = 'create.html'
    form_class = CarForm
    success_url = reverse_lazy('home')

class Detail(DetailView):
    model = Car
    template_name = 'detail.html'

class Update(UpdateView):
    model = Car
    template_name = 'update.html'
    form_class = CarForm
    success_url = reverse_lazy('home')

class Delete(DeleteView):
    model = Car
    template_name = 'delete.html'
    success_url = reverse_lazy('home')




