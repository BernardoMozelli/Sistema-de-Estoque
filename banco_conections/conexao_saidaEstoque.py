# Query para inserir informações do fornecedor no banco de dados
from tkinter import *
from utils.mensagem_box import *
from banco_conections.conexao import con

#----------------------------------------------------------------------------------------------------

#Query que retorna informações do banco para a combobox produto

global selected_produto
cursor = con.cursor()
sql = 'SELECT produto FROM cadastro_estoque'

cursor = con.cursor()
cursor.execute(sql)

var_resultproduto = cursor.fetchall() # resultado da query
selected_produto = [var_resultproduto[0] for var_resultproduto in var_resultproduto]

#-----------------------------------------------------------------------------------------------------

#Query que retorna informações do banco para a combobox modelo
global selected_modelo
cursor = con.cursor()
sql = 'SELECT modelo FROM cadastro_estoque'

cursor = con.cursor()
cursor.execute(sql)

var_resultmodelo = cursor.fetchall() # resultado da query
selected_modelo = [var_resultmodelo[0] for var_resultmodelo in var_resultmodelo]

#-----------------------------------------------------------------------------------------------------

#Query que retorna informações do banco para a combobox categoria

global selected_entcategoria
cursor = con.cursor()
sql = 'SELECT categoria FROM cadastro_categorias'

cursor = con.cursor()
cursor.execute(sql)

var_resultEntcategoria = cursor.fetchall() # resultado da query
selected_entcategoria = [var_resultEntcategoria[0] for var_resultEntcategoria in var_resultEntcategoria]

#-----------------------------------------------------------------------------------------------------

#Query que retorna informações do banco para a combobox sub-categoria

global selected_Entsubcategoria
cursor = con.cursor()
sql = 'SELECT sub_categoria FROM cadastro_subcategoria'

cursor = con.cursor()
cursor.execute(sql)

var_resultEntSubcategoria = cursor.fetchall() # resultado da query
selected_Entsubcategoria = [var_resultEntSubcategoria[0] for var_resultEntSubcategoria in var_resultEntSubcategoria]

#-----------------------------------------------------------------------------------------------------

#Query que retorna informações do banco para a combobox número de série

global selected_nserie
cursor = con.cursor()
sql = 'SELECT numero_serie FROM cadastro_estoque'

cursor = con.cursor()
cursor.execute(sql)

var_resultnserie = cursor.fetchall() # resultado da query
selected_nserie = [var_resultnserie[0] for var_resultnserie in var_resultnserie]

#-----------------------------------------------------------------------------------------------------

def query_ProdutoEntrada():
    #Inserindo dados do cadastro no banco de dados
    
    
    from menu_paginas.saida_estoque import var_Entquantidade, var_saidaProduto, var_SaidaModelo
    
    global valor_qtd
    
    cursor = con.cursor()
    query_qp = (("SELECT quantidade FROM cadastro_estoque WHERE produto ='{}' and modelo ='{}'".format(var_saidaProduto, var_SaidaModelo)))
    cursor.execute(query_qp)
    result = cursor.fetchall()
    var_resultqtd = [result[0] for result in result]
 
    #########################################################################################################################################################################################################################################################################################################################################################################################################################################################################
    
    #Adiciona a quantidade do produto informado a já existente no banco
    string_quantidade = ",".join(map(str, var_resultqtd))
    string_qtdBanco = int(string_quantidade)
    
    var_qtdSaida = int(var_Entquantidade)
    valor_result = (string_qtdBanco - var_qtdSaida)
    
    val = [(valor_result)]
    
    query_SaidaEstoque1 = (("SELECT quantidade FROM cadastro_estoque WHERE produto ='{}' and modelo ='{}'".format(var_saidaProduto, var_SaidaModelo)))
    query_SaidaEstoque2 = "REPLACE '{}' WITH '{}'".format(var_Entquantidade, val)
    
    cursor.execute(query_SaidaEstoque1, query_SaidaEstoque2)
    con.commit()
    msg_sucessoEntradaestoque()
     
query_ProdutoEntrada
    
    