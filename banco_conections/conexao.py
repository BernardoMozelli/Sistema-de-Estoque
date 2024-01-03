from tkinter import *
import mysql.connector
from utils.mensagem_box import *

#Dados para conexão com o banco de dados
con = mysql.connector.connect(host='localhost', database='inventario_pmsl', user='bernardo', password='250317')

# Valida a conexão com o banco. Caso ocorra algum erro, é exibida uma mensagem na tela.
def conect():
 global con
 global err
 try:
     cursor = con.cursor(buffered=True)
     con.is_connected()
     db_info = con.get_server_info()
     cursor = con.cursor()
     cursor.execute("select database();")
     linha = cursor.fetchall()

 except mysql.connector.Error as err:
     msg_error2()
     msg_error3()
conect

 


    
