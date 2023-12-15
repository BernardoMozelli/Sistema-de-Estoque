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