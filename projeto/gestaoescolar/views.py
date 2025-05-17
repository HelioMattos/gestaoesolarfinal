from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Gestao

# Create your views here.

class GestaoListView(ListView):
    model = Gestao
    template_name = 'gestaoescolar/gestao_list.html'

class GestaoCreateView(CreateView):
    model = Gestao
    fields = ['disciplina', 'carga_horaria']
    success_url = reverse_lazy('gestao_list')
    template_name = 'gestaoescolar/gestao_form.html'

class GestaoUpdateview(UpdateView):
    model = Gestao
    fields = ['disciplina', 'carga_horaria']
    success_url = reverse_lazy('gestao_list')
    template_name = 'gestaoescolar/gestao_form.html'


    
class GestaoDeleteView(DeleteView):
    model = Gestao
    success_url = reverse_lazy('gestao_list')
    template_name = 'gestaoescolar/gestao_confirm_delete.html'
