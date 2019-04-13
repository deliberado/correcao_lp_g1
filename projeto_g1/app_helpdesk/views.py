from django.shortcuts import render
from django.views.generic import ListView

from .models import Chamado


class ChamadosPageView(ListView):
    model = Chamado
    template_name = 'app_helpdesk/chamados.html'


class ChamadosAtendidosPageView(ListView):
    model = Chamado
    template_name = 'app_helpdesk/atendidos.html'

