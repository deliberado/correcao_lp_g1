
from django.urls import path

from .views import ChamadosPageView, ChamadosAtendidosPageView

urlpatterns = [
    path('', ChamadosPageView.as_view()),
    path('atendidos/', ChamadosAtendidosPageView.as_view())
]
