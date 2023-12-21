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
global result_nFantasia, var_resultNfantasia
cursor = con.cursor()
sql = 'SELECT nome_fantasia FROM cadastro_fornecedores'

cursor = con.cursor()
cursor.execute(sql)

result_nFantasia = cursor.fetchall() # resultado da query

var_resultNfantasia = [result_nFantasia[0] for result_nFantasia in result_nFantasia]

#-----------------------------------------------------------------------------------------------------
#Query que retorna informações do banco para a combobox fabricante
global result_nFantasiaF, var_resultNfantasiaF
cursor = con.cursor()
sql = 'SELECT nome_fantasia FROM cadastro_fabricante'

cursor = con.cursor()
cursor.execute(sql)

result_nFantasiaF = cursor.fetchall() # resultado da query

var_resultNfantasiaF = [result_nFantasiaF[0] for result_nFantasiaF in result_nFantasiaF]


#-----------------------------------------------------------------------------------------------------
#Query para atualizar informações cadastradas no banco na combobox fabricante

def atualiza_fabricante():
    global var_atualizar1, retorno_fabricante
    cursor = con.cursor()
    sql = 'SELECT nome_fantasia FROM cadastro_fabricante'

    cursor = con.cursor()
    cursor.execute(sql)

    atualizar1 = cursor.fetchall() # resultado da query

    var_atualizar1 = [atualizar1[0] for atualizar1 in atualizar1]
    var_atualizar1(var_resultNfantasiaF)
atualiza_fabricante

def atualiza_fornecedor():
    global atualizar2, var_atualizar2
    cursor = con.cursor()
    sql = 'SELECT nome_fantasia FROM cadastro_fornecedores'

    cursor = con.cursor()
    cursor.execute(sql)

    atualizar2 = cursor.fetchall() # resultado da query

    var_atualizar2 = [atualizar2[0] for atualizar2 in atualizar2]
atualiza_fornecedor
    
    
    