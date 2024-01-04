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
    
    
    