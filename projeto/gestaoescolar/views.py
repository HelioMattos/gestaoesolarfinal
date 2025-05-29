from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, View
from .models import Gestao
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from openpyxl import Workbook

class HomeView(TemplateView):
    template_name = "gestaoescolar/home.html"


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

class GerarPdfDisciplinaView(View):
    def get(self, request, *args, **kwargs):
        gestao_list = Gestao.objects.all()
        template = get_template("gestaoescolar/gestao_pdf.html")
        html_string = template.render({"gestao_list": gestao_list})
        pdf_file = HTML(string=html_string).write_pdf()

        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="disciplinas.pdf"'
        return response
    
class ExportarDisciplinasExcelView(View):
    def get(self, request, *args, **kwargs):
        wb = Workbook()
        ws = wb.active
        ws.title = "Disciplinas"
        ws.append(['Disciplina', 'Carga Horária'])
        disciplinas = Gestao.objects.all()
        for disc in disciplinas:
            ws.append([disc.disciplina, f"{disc.carga_horaria}"])
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=disciplinas.xlsx'
        wb.save(response)
        return response