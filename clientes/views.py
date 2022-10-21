from http import client
from django.http import HttpResponse
from django.shortcuts import render
from .models import Cliente, Carro
import re

# Create your views here.
def clientes(request):
    if request.method == 'GET':
        return render(request, 'clientes/clientes.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobre-nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')
        
        cliente = Cliente.objects.filter(cpf=cpf)
        if cliente.exists():
            return render(request, 'clientes/clientes.html', {'nome':nome, 'sobrenome': sobrenome, 'email':email, 'carros': zip(carros, placas, anos)})
        
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            #TODO: Adicionar mensagens
             return render(request, 'clientes/clientes.html', {'nome':nome, 'sobrenome': sobrenome, 'cpf':cpf, 'carros': zip(carros, placas, anos)})
        
        cliente = Cliente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )
        
        cliente.save()
        
        for carro, placa, ano in zip(carros, placas, anos):
            car = Carro(
                carro = carro,
                placa = placa,
                ano = ano,
                cliente = cliente
            )
            car.save()
    return HttpResponse('teste')