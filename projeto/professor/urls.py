from django.urls import path, include
from professor.views import ProfessorCreateView, ProfessorListView, ProfessorUpdateView, ProfessorDeleteView
from professor import views

urlpatterns = [
    path('', ProfessorListView.as_view(), name='professor_list'),
    path('create/', ProfessorCreateView.as_view(), name='professor_create'),
    path('update/<int:pk>/', ProfessorUpdateView.as_view(), name='professor_update'),
    path('delete/<int:pk>/', ProfessorDeleteView.as_view(), name='professor_delete'),
    path('professor/professor/pdf/', views.gerar_pdf_professor, name='professor_pdf'),
    path('exportar_excel/', views.exportar_professores_excel, name='exportar_excel')
]
