from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView , UpdateView, DeleteView
from .models import Professor
from .forms import ProfessorForm

# Create your views here.

class ProfessorListView(ListView):
    model = Professor
    template_name = 'professor/professor_list.html' 

class ProfessorCreateView(CreateView):
    model = Professor
    form_class = ProfessorForm
    success_url = reverse_lazy('professor_list')
    template_name = 'professor/professor_form.html'

class ProfessorUpdateView(UpdateView):
    model = Professor
    form_class = ProfessorForm
    success_url = reverse_lazy('professor_list')
    template_name = 'professor/professor_form.html'


class ProfessorDeleteView(DeleteView):
    model = Professor
    success_url = reverse_lazy('professor_list')
    template_name = 'professor/professor_confirm_delete.html'
