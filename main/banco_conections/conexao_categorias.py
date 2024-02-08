# Query para inserir informações do fornecedor no banco de dados
from tkinter import *
from utils.mensagem_box import *
from banco_conections.conexao import con

#Valida o módulo cadastro de categoria
def valida_cadastroCategoria():
    from menu_paginas.cadastro_categoria import var_categoria
    from utils.mensagem_box import msg_sucessoCadCategoria, msgErroCadastroCategoria
    
    while var_categoria == None:
        msgErroCadastroCategoria()
        return var_categoria
    else:
        msg_sucessoCadCategoria()

valida_cadastroCategoria

def query_categoria():
    from menu_paginas.cadastro_categoria import var_optionmenucategoria, var_categoria
    cursor = con.cursor()
    query_c = (("SELECT segmento, categoria FROM cadastro_categorias WHERE segmento ='{}' and categoria ='{}'".format(var_optionmenucategoria, var_categoria)))
    cursor.execute(query_c)
    result = cursor.fetchall() 
 
    #########################################################################################################################################################################################################################################################################################################################################################################################################################################################################
    
    # Verifica se o retorno contém alguma linha
    if len(result) != 0:
        msg_aviso3()
    else:
     #Insere as informações no banco de dados
     query_cad_categoria = ("INSERT INTO cadastro_categorias (segmento, categoria) VALUES (%s, %s)")
     val = (var_optionmenucategoria,var_categoria)
     cursor.execute(query_cad_categoria, val)
     con.commit()

     msg_sucessoCadFornecedor()
     
query_categoria
         