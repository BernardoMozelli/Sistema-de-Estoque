# Query para inserir informações do fornecedor no banco de dados
from tkinter import *
from utils.mensagem_box import *
from banco_conections.conexao import con

def valida_cadastroFabricante():
    from menu_paginas.cadastro_fabricante import var_cnpj
    
    #Valida o módulo cadastro de fabricante
    while var_cnpj == "":
        msgErroCadastrofabricante()
        return var_cnpj
    else:
        msg_sucessoCadFabricante
valida_cadastroFabricante

def query_fabricante():
    from menu_paginas.cadastro_fabricante import var_cnpj, var_nome, var_razao, var_cep, var_logradouro, var_complemento, var_bairro, var_cidade_estado, var_status, var_telefone
    from utils.mensagem_box import msgErroCadastrofabricante, msg_sucessoCadFabricante
    
    cursor = con.cursor()
    query_f = (("SELECT cnpj FROM cadastro_fabricante WHERE cnpj ='{}'".format(var_cnpj)))
    cursor.execute(query_f)
    result = cursor.fetchall()
    con.commit()
 
    #########################################################################################################################################################################################################################################################################################################################################################################################################################################################################
    
    # Verifica se o retorno contém alguma linha
    if len(result) != 0:
        msgErroFabricanteExiste()
    else:
     query_cad_fabricante = ("INSERT INTO cadastro_fabricante (cnpj, nome_fantasia, razao_social, cep, endereco, complemento, bairro, cidade_estado, status, telefone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
     val = (var_cnpj, var_nome, var_razao, var_cep, var_logradouro, var_complemento, var_bairro, var_cidade_estado, var_status, var_telefone)
     cursor.execute(query_cad_fabricante, val)
     con.commit()
     msg_sucessoCadFornecedor()
     
query_fabricante