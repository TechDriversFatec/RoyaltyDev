from django.db import models
from django.contrib.auth.models import User
from matplotlib import pyplot as plt
import io
import numpy as np



class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    qtd_total = models.PositiveIntegerField()
    status = models.CharField(
        default="C",
        max_length=1,
        choices=(
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
        )
    )

    def __str__(self):
        return f'Pedido N. {self.pk}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    produto_id = models.PositiveIntegerField()
    variacao = models.CharField(max_length=255)
    variacao_id = models.PositiveIntegerField()
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    quantidade = models.PositiveIntegerField()
    imagem = models.CharField(max_length=2000)

    def __str__(self):
        return f'Item do {self.pedido}'

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'


def relatorio(request):
    dados = 'utils/relatorio.csv'
    x = [1, 4, 6]
    y = [2, 4, 9, 16]

    titulo = "Relatório de Vendas"
    eixox = "Produto"
    eixoy = "Vendas"

    grafico = plt.title(titulo)
    grafico = plt.xlabel(eixox)
    grafico = plt.ylabel(eixoy)
    grafico = plt.plot(x, y)
    grafico = plt.savefig('media/grafico/graficos.png', dpi=1200)
    return render(request, 'perfil/relatorio.html', {'dados': dados, 'grafico': grafico})