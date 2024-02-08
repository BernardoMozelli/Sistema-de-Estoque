# Query para inserir informações do fornecedor no banco de dados
from tkinter import *
from utils.mensagem_box import *
from banco_conections.conexao import con

#Buscar todas as informações armazenadas na coluna Segmento, localizada na tabela cadastro_categorias armazenar em uma variável
# para que as informações sejam exibidas na combobox.

global result_segmento, var_result
cursor = con.cursor()
sql = 'SELECT segmento FROM cadastro_categorias'

cursor = con.cursor()
cursor.execute(sql)

result_segmento = cursor.fetchall() # resultado da query

var_result = [result_segmento[0] for result_segmento in result_segmento]

#--------------------------------------------------------------------------------------

global result_categoria, var_resultC
cursor = con.cursor()
sql = 'SELECT categoria FROM cadastro_categorias'

cursor = con.cursor()
cursor.execute(sql)

result_categoria = cursor.fetchall() # resultado da query

var_resultC = [result_categoria[0] for result_categoria in result_categoria]
#--------------------------------------------------------------------------------------

def categoriaAtualizaSelect():
    from menu_paginas.cadastro_subcategoria import combo_categoria
    global result_categoria, var_resultC
    cursor = con.cursor()
    sql = 'SELECT categoria FROM cadastro_categorias'

    cursor = con.cursor()
    cursor.execute(sql)

    result_categoria = cursor.fetchall() # resultado da query

    var_resultC = [result_categoria[0] for result_categoria in result_categoria]
    combo_categoria.configure(values=var_resultC)
categoriaAtualizaSelect
    

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def query_subcategoria():
    from menu_paginas.cadastro_subcategoria import var_subcategoria
    cursor = con.cursor()
    query_sc = (("SELECT sub_categoria FROM cadastro_subcategoria WHERE sub_categoria ='{}'".format(var_subcategoria)))
    cursor.execute(query_sc)
    result = cursor.fetchall()
 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    # Verifica se o retorno contém alguma linha
    if len(result) != 0:
        msg_aviso3()
    else:
     
     #Convertendo variaveis do formato listas em String. 
     # Isso deve ser feito para que os valores possam ser inseridos na tabela MySql
     
     string_segmento = " ".join(var_result)
     string_categoria = " ".join(var_resultC)
        
     #Insere as informações no banco de dados
     query_cad_subcategoria = ("INSERT INTO cadastro_subcategoria (segmento, categoria, sub_categoria) VALUES (%s, %s, %s)")
     val = (string_segmento, string_categoria, var_subcategoria)
     cursor.execute(query_cad_subcategoria, val)
     con.commit()

     msg_sucessoCadFornecedor()
     
query_subcategoria