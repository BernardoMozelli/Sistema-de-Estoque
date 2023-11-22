from tkinter import *
from banco_conections.conexao import con
import mysql.connector
from tkinter import messagebox

# Valida a conexão com o banco. Caso ocorra algum erro, é exibida uma mensagem na tela.

def conect():
 try:
     cursor = con.cursor(buffered=True)
     con.is_connected()
     messagebox.showinfo(
         "Banco de dados", "Conexão realizada com sucesso")
     db_info = con.get_server_info()
     cursor = con.cursor()
     cursor.execute("select database();")
     linha = cursor.fetchall()

 except mysql.connector.Error as err:
     messagebox.showerror(
            "Connection failed", "Erro ao realizar a conexão com o banco de dados!!!")
     messagebox.showerror("Connection failed", "Erro: {}".format(err))
conect()
     