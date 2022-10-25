function add_veiculo(){

    container = document.getElementById("form-carro")

    html = "<br><div class='row'>\
                    <div class='col-md'>\
                        <input type='text' placeholder='Carro' class='form-control' name='carro'>\
                    </div>\
                    <div class='col-md'>\
                        <input type='text' placeholder='Placa' class='form-control'name='placa'>\
                    </div>\
                    <div class='col-md'>\
                        <input type='number' placeholder='Ano' class='form-control' name='ano'>\
                    </div>"

    container.innerHTML += html
}

function exibir_form(tipo){
    add_cliente = document.getElementById('adicionar-cliente')
    att_cliente = document.getElementById('att_cliente')

    if(tipo == "1"){
        att_cliente.style.display = "none"
        add_cliente.style.display = "block"

    } else if(tipo == "2"){
        att_cliente.style.display = "block"
        add_cliente.style.display = "none"
    }

}

function dados_clientes(){
    cliente = document.getElementById('cliente-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_cliente = cliente.value

    data = new FormData()
    data.append('id_cliente', id_cliente)

    fetch("/clientes/atualiza_cliente/",{
        method: "POST", 
        headers: {
            'X-CSRFToken': csrf_token,            
        },
        body: data
    }).then(function(result){
        return result.json()
    }).then(function(data){
       
        document.getElementById('form-att-cliente').style.display = 'block'

        id = document.getElementById('id')
        id.value = data['cliente_id']

        nome = document.getElementById('nome')
        nome.value = data['cliente']['nome']

        sobrenome = document.getElementById('sobrenome')
        sobrenome.value = data['cliente']['sobrenome']

        email = document.getElementById('email')
        email.value = data['cliente']['email']

        cpf = document.getElementById('cpf')
        cpf.value = data['cliente']['cpf']

        div_carros = document.getElementById('carros')
        div_carros.innerHTML=""
        for(i=0; i<data['carros'].length; i++){
           // console.log(data['carros'][i]['fields']['carro'])
            div_carros.innerHTML += "\<form action='/clientes/update_carro/" + data['carros'][i]['id'] +"' method='POST'>\
            <div class='row'>\
                    <div class='col-md'>\
                        <input class='form-control' name='carro' type='text' value='" + data['carros'][i]['fields']['carro'] + "'>\
                    </div>\
                    <div class='col-md'>\
                        <input class='form-control' name='placa' type='text' value='" + data['carros'][i]['fields']['placa'] + "'>\
                    </div>\
                    <div class='col-md'>\
                        <input class='form-control' type='text' name='ano' value='" + data['carros'][i]['fields']['ano'] + "' >\
                    </div>\
                    <div class=''>\
                        <input class='btn btn-lg btn-success botao' type='submit'>\
                    </div>\
                </form>\
                <div class=''>\
                    <a style='margin-left: 10px;' href='/clientes/excluir_carro/"+ data['carros'][i]['id'] +"' class='btn btn-lg btn-danger'>EXCLUIR</a>\
                </div>\
            </div><br>"
        }
    })
}

function update_cliente(){
    nome = document.getElementById('nome').value
    sobrenome = document.getElementById('sobrenome').value
    email = document.getElementById('email').value
    cpf = document.getElementById('cpf').value
    id = document.getElementById('id').value

    fetch('/clientes/update_cliente/' + id, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            nome: nome,
            sobrenome: sobrenome,
            email: email,
            cpf: cpf,
        })

    }).then(function(result){
        return result.json()
    }).then(function(data){

        if(data['status']==200){
            nome = data['nome']
            sobrenome = data['sobrenome']
            email = data['email']
            cpf = data['cpf']
            console.log('Dados alterados com sucesso')
        }else{
            console.log('Ocorreu um erro')
        }
    })
}