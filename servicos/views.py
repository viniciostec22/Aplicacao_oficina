from django.shortcuts import render, redirect
from . forms import FormServico
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

def novo_servico(request):
    if request.method == "GET":
        form = FormServico()
        return render(request, 'servicos/novo_servico.html', {'form': form})
    elif request.method == "POST":
        form = FormServico(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Serviço Salvo com sucesso!')
            return redirect('novo_servico')
        else:
            print('teste')
            return render(request, 'servicos/novo_servico.html', {'form': form})