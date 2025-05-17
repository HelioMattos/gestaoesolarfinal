from django.db import models

class Gestao(models.Model):
    disciplina = models.CharField(max_length=100)
    carga_horaria = models.CharField(max_length=50)

    def __str__(self):
        return self.disciplina
