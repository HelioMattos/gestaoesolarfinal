from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Gestao
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML

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

def gerar_pdf_disciplina(request):
    # Pegue os dados do modelo (ou formulário, como preferir)
    from .models import Gestao
    gestao_list = Gestao.objects.all()

    # Renderiza o HTML como string
    template = get_template("gestaoescolar/gestao_pdf.html")  # HTML próprio para PDF
    html_string = template.render({"gestao_list": gestao_list})

    # Gera o PDF
    pdf_file = HTML(string=html_string).write_pdf()

    # Retorna como resposta
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="disciplinas.pdf"'
    return response
