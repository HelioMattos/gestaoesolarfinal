from django.urls import path
from professor.views import ProfessorCreateView, ProfessorListView, ProfessorUpdateView, ProfessorDeleteView

urlpatterns = [
    path('', ProfessorListView.as_view(), name='professor_list'),
    path('create/', ProfessorCreateView.as_view(), name='professor_create'),
    path('update/<int:pk>/', ProfessorUpdateView.as_view(), name='professor_update'),
    path('delete/<int:pk>/', ProfessorDeleteView.as_view(), name='professor_delete')
]
