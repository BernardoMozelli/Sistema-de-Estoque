# Query para inserir informações do fornecedor no banco de dados
from tkinter import *
from utils.mensagem_box import *
from banco_conections.conexao import con

#----------------------------------------------------------------------------------------------------
#Query que retorna informações do banco para a combobox segmento

global result_Esegmento, var_resulEsegmento
cursor = con.cursor()
sql = 'SELECT segmento FROM cadastro_categorias'

cursor = con.cursor()
cursor.execute(sql)

result_Esegmento = cursor.fetchall() # resultado da query

var_resulEsegmento = [result_Esegmento[0] for result_Esegmento in result_Esegmento]

#----------------------------------------------------------------------------------------------------

#Query que retorna informações do banco para a combobox fornecedor
global var_resultfornecedor
cursor = con.cursor()
sql = 'SELECT nome_fantasia FROM cadastro_fornecedores'

cursor = con.cursor()
cursor.execute(sql)

var_resultfornecedor = cursor.fetchall() # resultado da query

#var_resultNfantasia = [result_nFantasia[0] for result_nFantasia in result_nFantasia]

#-----------------------------------------------------------------------------------------------------
#Query que retorna informações do banco para a combobox fabricante
global var_resultfabricante
cursor = con.cursor()
sql = 'SELECT nome_fantasia FROM cadastro_fabricante'

cursor = con.cursor()
cursor.execute(sql)

var_resultfabricante = cursor.fetchall() # resultado da query

#var_resultNfantasiaF = [result_nFantasiaF[0] for result_nFantasiaF in result_nFantasiaF]

    
    
    