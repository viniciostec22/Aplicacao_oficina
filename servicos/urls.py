from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('novo_servico/', views.novo_servico, name="novo_servico"),#type:ignore
    path('listar-servicos/', views.listar_servicos, name='listar_servico'),#type:ignore
    path('servico/<str:identificador>', views.servico, name='servico'),
    path('gerar_os<str:identificador>/', views.gerar_os, name='gerar_os')
]