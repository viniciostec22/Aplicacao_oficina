from django.shortcuts import get_object_or_404, render, redirect
from . forms import FormServico
from django.http import FileResponse, HttpResponse
from django.contrib import messages
from .models import Servico
from fpdf import FPDF
from io import BytesIO
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
        
def listar_servicos(request):
    if request.method == "GET":
        servicos = Servico.objects.all()
        return render(request, 'servicos/listar_servico.html', {'servicos':servicos})
    
def servico(request, identificador):
    servico = get_object_or_404(Servico,identificador=identificador)
    return render(request, 'servicos/servico.html', {'servico':servico} )

def gerar_os(request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador)
    
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font('Arial', 'B', 12)
    pdf.set_fill_color(240,240,240)
    pdf.cell(35, 10, 'Cliente:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.cliente.nome}', 1, 1, 'L', 1)
    
    pdf.cell(35, 10, 'Manutenções', 1, 0, 'L', 1)
    
    categorias_manutencao = servico.categoria_manutencao.all()
    
    for i, manutencao in enumerate(categorias_manutencao):
        pdf.cell(0, 10, f'- {manutencao.get_titulo_display()}', 1, 1, 'L', 1)
        if not i == len(categorias_manutencao) -1:
            pdf.cell(35,10, '', 0,0)
        
    pdf.cell(35, 10, 'Data de inicio:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.data_inicio}', 1, 1, 'L', 1)
    
    pdf.cell(35, 10, 'Data de Entrega:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.data_entrega}', 1, 1, 'L', 1)
    
    pdf.cell(35, 10, 'Protocolo:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.protocolo}', 1, 1, 'L', 1)
    
    pdf.cell(35, 10, 'Total R$:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.preco_total}', 1, 1, 'L', 1)
    
    pdf_content = pdf.output(dest='S').encode('latin1')    
    pdf_bytes = BytesIO(pdf_content)
    # se passar o "as_attachmen=True" no file response ele faz o dawnload direto do pdf
    return FileResponse(pdf_bytes, filename=f"os-{servico.protocolo}.pdf")
