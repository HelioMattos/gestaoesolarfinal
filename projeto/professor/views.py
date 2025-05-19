from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView , UpdateView, DeleteView
from .models import Professor
from .forms import ProfessorForm
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML

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

def gerar_pdf_professor(request):
    # Pegue os dados do modelo (ou formulário, como preferir)
    from .models import Professor
    professor_list = Professor.objects.all()

    # Renderiza o HTML como string
    template = get_template("professor/professor_pdf.html")  # HTML próprio para PDF
    html_string = template.render({"professor_list": professor_list})

    # Gera o PDF
    pdf_file = HTML(string=html_string).write_pdf()

    # Retorna como resposta
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="disciplinas.pdf"'
    return response
