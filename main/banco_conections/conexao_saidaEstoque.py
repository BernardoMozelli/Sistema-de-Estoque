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
    from menu_paginas.saida_estoque import entry_produto, entry_modelo, var_userselect
    global selected_ID
    cursor = con.cursor()
    sql = "SELECT produto FROM cadastro_estoque WHERE ID ='{}'".format(var_userselect)
    cursor = con.cursor()
    cursor.execute(sql)
    selected_ID = cursor.fetchall() # resultado da query  
    
    var_result = [selected_ID[0] for selected_ID in selected_ID]
    var_formatproduto = "".join(var_result)
    entry_produto.insert(0, var_formatproduto)
    
#-----------------------------------------------------------------------------------------------------
#Query que retorna informações do banco para a entry modelo
    cursor2 = con.cursor()
    sql2 = "SELECT modelo FROM cadastro_estoque WHERE ID ='{}'".format(var_userselect)
    cursor2 = con.cursor()
    cursor2.execute(sql2)
    selected_ID_modelo = cursor.fetchall() # resultado da query  
    
    var_result2 = [selected_ID_modelo[0] for selected_ID_modelo in selected_ID_modelo]
    var_formatmodelo = "".join(var_result2)
    entry_modelo.insert(0, var_formatmodelo)
     
query_ProdutoEntrada

def movimenta_saidaEstoque():
    from menu_paginas.saida_estoque import entry_produto,entry_quantidade, var_quantidade, var_userselect
    from utils.mensagem_box import msgErroSaidaEstoque, msg_sucessoSaidaEstoque
    
    cursor3 = con.cursor()
    
    #Subtrair valor informado pelo usuário da quantidade no banco
    sql3 = "SELECT quantidade FROM cadastro_estoque WHERE ID ='{}'".format(var_userselect)
    cursor3.execute(sql3)
    selected_ID_quantidade = cursor.fetchall() # resultado da query  
    
    var_result3 = [selected_ID_quantidade[0] for selected_ID_quantidade in selected_ID_quantidade]
    string_quantidade = ",".join(map(str, var_result3))
    string_qtdBanco = int(string_quantidade)
    string_qtdusuario = int(var_quantidade)
    
    result_quantidade = (string_qtdBanco - string_qtdusuario)
    
    cursor4 = con.cursor()
    sql4 = "UPDATE cadastro_estoque SET quantidade = '{}' WHERE ID = '{}'".format(result_quantidade, var_userselect)
    cursor4.execute(sql4)
    result_final = cursor4.fetchall()
    con.commit()
    
    
    if result_final is None:
        msgErroSaidaEstoque()
    else:
        msg_sucessoSaidaEstoque()    
    
        
movimenta_saidaEstoque

def atualiza_tabela():
    from menu_paginas.saida_estoque import table
    global selected_atualiza
    cursor5 = con.cursor()
    sql5 = 'SELECT ID, produto, quantidade, segmento,fabricante, fornecedor, modelo FROM cadastro_estoque ORDER BY ID'

    cursor5 = con.cursor()
    cursor5.execute(sql5)
    selected_atualiza = cursor5.fetchall() # resultado da query
    
    #Atualizando valor na treeview
    table.update_values(selected_atualiza)
atualiza_tabela
    
    