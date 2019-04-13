from django.contrib import admin

from .models import Categoria, \
    Departamento, Funcionario, Status, Atendimento, Chamado

admin.site.register(Categoria)
admin.site.register(Departamento)
admin.site.register(Funcionario)
admin.site.register(Status)
admin.site.register(Atendimento)
admin.site.register(Chamado)
