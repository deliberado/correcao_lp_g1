from django.db import models
from django.contrib.auth.models import User


class Departamento(models.Model):
    nome = models.CharField('Nome Departamento', max_length=255)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=255)
    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nome


class Status(models.Model):
    nome = models.CharField('Nome do status', max_length=20)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField('Nome do categoria', max_length=20)

    def __str__(self):
        return self.nome


class Chamado(models.Model):
    criado_por = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, blank=True, null=True)
    titulo = models.CharField('Titulo', max_length=128)
    descricao = models.TextField()
    telefone = models.CharField('Telefone', max_length=13)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, blank=True, null=True)
    data_abertura = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, blank=True, null=True)
    categoria = models.ManyToManyField(Categoria)

    def get_atendimentos(self):
        return Atendimento.objects.filter(chamado=self)

    def __str__(self):
        return self.titulo


class Atendimento(models.Model):
    chamado = models.ForeignKey(Chamado, on_delete=models.SET_NULL, blank=True, null=True)
    descricao = models.CharField('Descrição', max_length=155)
    funcionario_atendeu = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, blank=True, null=True)
    data_atendimento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Atendimento do chamado: ' + self.chamado.titulo
