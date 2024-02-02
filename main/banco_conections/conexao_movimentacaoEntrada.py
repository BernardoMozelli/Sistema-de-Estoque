# Query para inserir informações do fornecedor no banco de dados
from tkinter import *
from utils.mensagem_box import *
from banco_conections.conexao import con

#----------------------------------------------------------------------------------------------------

#Query que retorna informações do banco para a view(tabela)

global selected
cursor = con.cursor()
sql = 'SELECT ID, produto, quantidade, segmento,fabricante, fornecedor, modelo FROM cadastro_estoque ORDER BY ID'

cursor = con.cursor()
cursor.execute(sql)

selected = cursor.fetchall() # resultado da query
#selected = [var_resul[0] for var_resul in var_resul]

#-----------------------------------------------------------------------------------------------------
def query_ProdutoEntrada():
    
#Query que retorna informações do banco para a entry produto
    from menu_paginas.entrada_estoque import entry_produtoEntrada, entry_modeloEntrada, var_userselectEntrada
    global selected_ID
    cursor = con.cursor()
    sql = "SELECT produto FROM cadastro_estoque WHERE ID ='{}'".format(var_userselectEntrada)
    cursor = con.cursor()
    cursor.execute(sql)
    selected_ID = cursor.fetchall() # resultado da query  
    
    var_result = [selected_ID[0] for selected_ID in selected_ID]
    var_formatproduto = "".join(var_result)
    entry_produtoEntrada.insert(0, var_formatproduto)
    
#-----------------------------------------------------------------------------------------------------
#Query que retorna informações do banco para a entry modelo
    cursor2 = con.cursor()
    sql2 = "SELECT modelo FROM cadastro_estoque WHERE ID ='{}'".format(var_userselectEntrada)
    cursor2 = con.cursor()
    cursor2.execute(sql2)
    selected_ID_modelo = cursor.fetchall() # resultado da query  
    
    var_result2 = [selected_ID_modelo[0] for selected_ID_modelo in selected_ID_modelo]
    var_formatmodelo = "".join(var_result2)
    entry_modeloEntrada.insert(0, var_formatmodelo)
     
query_ProdutoEntrada

def movimenta_entradaEstoque():
    from menu_paginas.entrada_estoque import entry_produtoEntrada,entry_quantidadeEntrada, var_quantidadeEntrada, var_userselectEntrada
    from utils.mensagem_box import msgErroEntradaestoque, msg_sucessoEntradaestoque
    
    cursor3 = con.cursor()
    
    #Subtrair valor informado pelo usuário da quantidade no banco
    sql3 = "SELECT quantidade FROM cadastro_estoque WHERE ID ='{}'".format(var_userselectEntrada)
    cursor3.execute(sql3)
    selected_ID_quantidade = cursor.fetchall() # resultado da query  
    
    var_result3 = [selected_ID_quantidade[0] for selected_ID_quantidade in selected_ID_quantidade]
    string_quantidade = ",".join(map(str, var_result3))
    string_qtdBanco = int(string_quantidade)
    string_qtdusuario = int(var_quantidadeEntrada)
    
    result_quantidade = (string_qtdBanco + string_qtdusuario)
    
    cursor4 = con.cursor()
    sql4 = "UPDATE cadastro_estoque SET quantidade = '{}' WHERE ID = '{}'".format(result_quantidade, var_userselectEntrada)
    cursor4.execute(sql4)
    result_final = cursor4.fetchall()
    con.commit()
    
    
    if result_final is None:
        msgErroEntradaestoque()
    else:
        msg_sucessoEntradaestoque()    
    
        
movimenta_entradaEstoque

def atualiza_tabela():
    from menu_paginas.entrada_estoque import table_entrada
    global selected_atualizaEntrada
    cursor5 = con.cursor()
    sql5 = 'SELECT ID, produto, quantidade, segmento,fabricante, fornecedor, modelo FROM cadastro_estoque ORDER BY ID'

    cursor5 = con.cursor()
    cursor5.execute(sql5)
    selected_atualizaEntrada = cursor5.fetchall() # resultado da query
    
    #Atualizando valor na treeview
    table_entrada.update_values(selected_atualizaEntrada)
atualiza_tabela
    
    