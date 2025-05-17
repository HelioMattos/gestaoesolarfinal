from django import forms
from .models import Professor, Gestao

class ProfessorForm(forms.ModelForm):
    disciplina = forms.ModelChoiceField(queryset=Gestao.objects.all(), empty_label="Selecione a Disciplina")

    class Meta:
        model = Professor
        fields = ['nome', 'telefone', 'disciplina']


