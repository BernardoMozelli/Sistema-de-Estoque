# Query para inserir informações do fornecedor no banco de dados
from tkinter import *
from utils.mensagem_box import *
from banco_conections.conexao import con

#----------------------------------------------------------------------------------------------------

#Query que retorna informações do banco para a view(tabela)

global selected_relatorioC
cursor = con.cursor()
sql = 'SELECT ID, produto, quantidade, segmento, fabricante, fornecedor, modelo FROM cadastro_estoque ORDER BY ID'

cursor = con.cursor()
cursor.execute(sql)

selected_relatorioC = cursor.fetchall() # resultado da query
