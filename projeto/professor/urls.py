from django.urls import path, include
from professor.views import ProfessorCreateView, ProfessorListView, ProfessorUpdateView, ProfessorDeleteView, GerarPdfProfessorView, ExportarProfessoresExcelView
from professor import views

urlpatterns = [
    path('', ProfessorListView.as_view(), name='professor_list'),
    path('create/', ProfessorCreateView.as_view(), name='professor_create'),
    path('update/<int:pk>/', ProfessorUpdateView.as_view(), name='professor_update'),
    path('delete/<int:pk>/', ProfessorDeleteView.as_view(), name='professor_delete'),
    path('professor/professor/pdf/', GerarPdfProfessorView.as_view(), name='professor_pdf'),
    path('exportar_excel/', ExportarProfessoresExcelView.as_view(), name='exportar_excel')
]
