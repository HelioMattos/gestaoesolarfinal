from django.db import models
from gestaoescolar.models import Gestao  # Importa o modelo de disciplina

class Professor(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=50, null=False, blank=False)
    disciplina = models.ForeignKey(Gestao, on_delete=models.CASCADE, related_name='professores')

    def __str__(self):
        return self.nome
