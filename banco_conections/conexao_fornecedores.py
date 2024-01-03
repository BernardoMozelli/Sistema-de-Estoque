# Query para inserir informações do fornecedor no banco de dados
from tkinter import *
from utils.mensagem_box import *
from banco_conections.conexao import con
import re

def query_fornecedor():
    from menu_paginas.cadastro_fornecedor import var_cnpj, var_nome, var_razao, var_cep, var_logradouro, var_complemento, var_bairro, var_cidade_estado, var_status, var_telefone
    cursor = con.cursor()
    query_f = (("SELECT cnpj FROM cadastro_fornecedores WHERE cnpj ='{}'".format(var_cnpj)))
    cursor.execute(query_f)
    result = cursor.fetchall() 
 
    #########################################################################################################################################################################################################################################################################################################################################################################################################################################################################
    
    # Verifica se o retorno contém alguma linha
    if len(result) != 0:
        msg_aviso3()
    else:
     query_cad_fornecedor = ("INSERT INTO cadastro_fornecedores (cnpj, nome_fantasia, razao_social, cep, endereco, complemento, bairro, cidade_estado, status, telefone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
     val = (var_cnpj, var_nome, var_razao, var_cep, var_logradouro, var_complemento, var_bairro, var_cidade_estado, var_status, var_telefone)
     cursor.execute(query_cad_fornecedor, val)
     con.commit()
     msg_sucessoCadFornecedor()
     
query_fornecedor