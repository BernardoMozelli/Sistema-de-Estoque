# Query para inserir informações do fornecedor no banco de dados
from tkinter import *
from utils.mensagem_box import *
from banco_conections.conexao import con

#----------------------------------------------------------------------------------------------------

#Query que retorna informações do banco para a combobox fornecedor
global selected_fornecedor
cursor = con.cursor()
sql = 'SELECT nome_fantasia FROM cadastro_fornecedores'

cursor = con.cursor()
cursor.execute(sql)

var_resultfornecedor = cursor.fetchall() # resultado da query
selected_fornecedor = [var_resultfornecedor[0] for var_resultfornecedor in var_resultfornecedor]

#var_resultNfantasia = [result_nFantasia[0] for result_nFantasia in result_nFantasia]

#-----------------------------------------------------------------------------------------------------
#Query que retorna informações do banco para a combobox fabricante
global selected_fabricante
cursor = con.cursor()
sql = 'SELECT nome_fantasia FROM cadastro_fabricante'

cursor = con.cursor()
cursor.execute(sql)

var_resultfabricante = cursor.fetchall() # resultado da query
selected_fabricante = [var_resultfabricante[0] for var_resultfabricante in var_resultfabricante]

#-----------------------------------------------------------------------------------------------------
#Query que retorna informações do banco para a combobox categoria

global selected_categoria
cursor = con.cursor()
sql = 'SELECT categoria FROM cadastro_categorias'

cursor = con.cursor()
cursor.execute(sql)

var_resultcategoria = cursor.fetchall() # resultado da query
selected_categoria = [var_resultcategoria[0] for var_resultcategoria in var_resultcategoria]

#-----------------------------------------------------------------------------------------------------

#Query que retorna informações do banco para a combobox sub-categoria

global selected_subcategoria
cursor = con.cursor()
sql = 'SELECT sub_categoria FROM cadastro_subcategoria'

cursor = con.cursor()
cursor.execute(sql)

var_resultSubcategoria = cursor.fetchall() # resultado da query
selected_subcategoria = [var_resultSubcategoria[0] for var_resultSubcategoria in var_resultSubcategoria]

#-----------------------------------------------------------------------------------------------------

def query_EntradaEstoque():
    #Inserindo dados do cadastro no banco de dados
    
    from menu_paginas.estoque_entrada import var_nomevalida, var_validaseg, var_fabri, var_fornec, var_nomevalida, var_validamodelo, var_validadata, var_categoria, var_subcategoria, var_validanserie, var_validanota, var_validaquantidade, var_validavalor
    
    cursor = con.cursor()
    query_f = (("SELECT produto FROM cadastro_estoque WHERE produto ='{}'".format(var_nomevalida)))
    cursor.execute(query_f)
    result = cursor.fetchall()
    con.commit()
 
    #########################################################################################################################################################################################################################################################################################################################################################################################################################################################################
    
    # Verifica se o retorno contém alguma linha
    if len(result) != 0:
        msgErroFabricanteExiste()
    else:
     query_cad_produto = ("INSERT INTO cadastro_estoque (produto, quantidade, segmento, fabricante, modelo, fornecedor, categoria, valor_compra, sub_categoria, numero_notafiscal, data_compra, numero_serie) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
     val = (var_nomevalida, var_validaquantidade, var_validaseg, var_fabri, var_validamodelo, var_fornec, var_categoria, var_validavalor, var_subcategoria, var_validanota, var_validadata, var_validanserie)
     cursor.execute(query_cad_produto, val)
     con.commit()
     msg_sucessoEntradaestoque()
     
query_EntradaEstoque
    
    