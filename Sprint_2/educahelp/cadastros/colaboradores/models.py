from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Colaboradores(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    observacoes = models.TextField(max_length=250, blank=True)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.usuario

    class Meta:
        db_table = 'colaboradores'
        ordering = ('usuario',)