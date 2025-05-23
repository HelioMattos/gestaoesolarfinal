from django.contrib import admin
from django.urls import path, include
from gestaoescolar.views import GestaoCreateView, GestaoListView, GestaoUpdateview, GestaoDeleteView, HomeView, GerarPdfDisciplinaView, ExportarDisciplinasExcelView
from gestaoescolar import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('disciplinas', GestaoListView.as_view(), name='gestao_list'),
    path('create/', GestaoCreateView.as_view(), name='gestao_create'),
    path('update/<int:pk>/', GestaoUpdateview.as_view(), name='gestao_update'),
    path('delete/<int:pk>/', GestaoDeleteView.as_view(), name='gestao_delete'),
    path('professores/', include('professor.urls')),
    path('gestaoescolar/pdf/', GerarPdfDisciplinaView.as_view(), name='gestao_pdf'),
    path('exportar_disciplinas_excel/', ExportarDisciplinasExcelView.as_view(), name='exportar_disciplinas_excel'),

]

