from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView , UpdateView, DeleteView, View
from .models import Professor
from .forms import ProfessorForm
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from openpyxl import Workbook


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


class GerarPdfProfessorView(View):
    def get(self, request, *args, **kwargs):
        professor_list = Professor.objects.all()
        template = get_template("professor/professor_pdf.html")
        html_string = template.render({"professor_list": professor_list})
        pdf_file = HTML(string=html_string).write_pdf()

        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="disciplinas.pdf"'
        return response


class ExportarProfessoresExcelView(View):
    def get(self, request, *args, **kwargs):
        wb = Workbook()
        ws = wb.active
        ws.title = "Professores"
        ws.append(['Nome', 'Telefone', 'Disciplina'])
        professores = Professor.objects.all()
        for prof in professores:
            ws.append([prof.nome, prof.telefone, prof.disciplina.disciplina])
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=professores.xlsx'
        wb.save(response)
        return response