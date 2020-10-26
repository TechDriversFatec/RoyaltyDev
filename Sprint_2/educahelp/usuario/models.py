from django.db import models
from django.contrib.auth.models import User


class Permissoes(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=40)

    administrador = models.IntegerField(default=0)
    administrador_super = models.IntegerField(default=0, blank=True, null=True)

    cadastra_colaborador = models.IntegerField(default=0)
    edita_colaborador = models.IntegerField(default=0)
    acessa_cadastro_colaboradores = models.IntegerField(default=0)
    muda_status_colaborador = models.IntegerField(default=0)

    cadastra_usuario = models.IntegerField(default=0)
    edita_usuario = models.IntegerField(default=0)
    acessa_cadastro_usuarios = models.IntegerField(default=0)
    muda_status_usuario = models.IntegerField(default=0)

    cadastra_permissoes_usuario = models.IntegerField(default=0)
    edita_permissoes_usuario = models.IntegerField(default=0)
    acessa_permissoes_usuario = models.IntegerField(default=0)
    muda_status_permissoes_usuario = models.IntegerField(default=0)
    exclui_permissoes_usuario = models.IntegerField(default=0)

    cadastra_cliente = models.IntegerField(default=0)
    edita_cliente = models.IntegerField(default=0)
    acessa_cadastro_cliente = models.IntegerField(default=0)
    muda_status_cliente = models.IntegerField(default=0)

    cadastra_fornecedor = models.IntegerField(default=0)
    edita_fornecedor = models.IntegerField(default=0)
    acessa_cadastro_fornecedor = models.IntegerField(default=0)
    muda_status_fornecedor = models.IntegerField(default=0)

    cadastra_produto = models.IntegerField(default=0)
    edita_produto = models.IntegerField(default=0)
    acessa_cadastro_produto = models.IntegerField(default=0)
    muda_status_produto = models.IntegerField(default=0)
    altera_preco_produto = models.IntegerField(default=0)
    anuncia_produto = models.IntegerField(default=0)

    tabela_preco = models.IntegerField(default=0)
    edita_tabela_de_precos = models.IntegerField(default=0)
    acessa_tabela_de_precos = models.IntegerField(default=0)
    exclui_preco_tabelado = models.IntegerField(default=0)
    muda_status_preco_tabelado = models.IntegerField(default=0)

    registra_venda = models.IntegerField(default=0)
    edita_venda = models.IntegerField(default=0)
    fecha_venda = models.IntegerField(default=0)
    acessa_registro_venda = models.IntegerField(default=0)
    muda_status_venda = models.IntegerField(default=0)
    cancela_venda = models.IntegerField(default=0)
    imprime_cupom_venda = models.IntegerField(default=0)

    registra_compra = models.IntegerField(default=0)
    edita_compra = models.IntegerField(default=0)
    acessa_registro_compra = models.IntegerField(default=0)
    muda_status_compra = models.IntegerField(default=0)
    cancela_compra = models.IntegerField(default=0)
    finaliza_compra = models.IntegerField(default=0)

    edita_contas_pagar = models.IntegerField(default=0)
    acessa_contas_pagar = models.IntegerField(default=0)
    exclui_contas_pagar = models.IntegerField(default=0)
    quita_contas_pagar = models.IntegerField(default=0)

    edita_contas_receber = models.IntegerField(default=0)
    acessa_contas_receber = models.IntegerField(default=0)
    exclui_contas_receber = models.IntegerField(default=0)
    quita_contas_receber = models.IntegerField(default=0)

    registra_pagamento = models.IntegerField(default=0)
    edita_pagamento = models.IntegerField(default=0)
    acessa_pagamento = models.IntegerField(default=0)
    muda_status_pagamento = models.IntegerField(default=0)
    exclui_pagamento = models.IntegerField(default=0)

    registra_recebimento = models.IntegerField(default=0)
    edita_recebimento = models.IntegerField(default=0)
    acessa_recebimento = models.IntegerField(default=0)
    muda_status_recebimento = models.IntegerField(default=0)
    exclui_recebimento = models.IntegerField(default=0)

    registra_entrada_produto = models.IntegerField(default=0)
    edita_entrada_produto = models.IntegerField(default=0)
    acessa_entrada_produto = models.IntegerField(default=0)
    muda_status_entrada_produto = models.IntegerField(default=0)
    cancela_entrada_produto = models.IntegerField(default=0)

    registra_saida_produto = models.IntegerField(default=0)
    edita_saida_produto = models.IntegerField(default=0)
    acessa_saida_produto = models.IntegerField(default=0)
    muda_status_saida_produto = models.IntegerField(default=0)
    cancela_saida_produto = models.IntegerField(default=0)

    publica_conteudo_site = models.IntegerField(default=0)
    edita_conteudo_site = models.IntegerField(default=0)
    exclui_conteudo_site = models.IntegerField(default=0)
    acessa_conteudo_site = models.IntegerField(default=0)
    muda_status_conteudo_site = models.IntegerField(default=0)

    publica_mensagem_site = models.IntegerField(default=0)
    edita_mensagem_site = models.IntegerField(default=0)
    exclui_mensagem_site = models.IntegerField(default=0)
    acessa_mensagem_site = models.IntegerField(default=0)
    muda_status_mensagem_site = models.IntegerField(default=0)

    observacoes = models.TextField(max_length=200, blank=True)
    status = models.CharField('Státus', max_length=10, default='ATIVO')

    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + ', ' + str(self.descricao)

    class Meta:
        db_table = 'permissoes'
        ordering = ('descricao',)


class Usuario(models.Model):
    Nome = models.CharField(max_length=100)
    Cidade = models.CharField(max_length=100)
    CPF = models.CharField(max_length=11)
    Telefone = models.CharField(max_length=11)
    Email = models.EmailField()
    Begin_date = models.DateTimeField(auto_now_add=True)
    Photo = models.ImageField()
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "usuario"
