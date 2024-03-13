# Query para vericar se usuário já esta cadastrado no banco
from tkinter import *
from utils.mensagem_box import *

def validate_login():
    from banco_conections.conexao import con
    import home
    from login import var_usuario, var_senha
    
    cursor = con.cursor()
    query_login = (("SELECT usuario and senha FROM cadastro WHERE usuario ='{}' and senha = '{}'".format(var_usuario, var_senha)))
    cursor.execute(query_login)
    resultado_login = cursor.fetchall()
    
    while len(resultado_login) != 0:
        home
        
        from login import janela_login
        janela_login.destroy()
    
    while var_usuario or var_senha == (""):
        msg_loginErro()
        return var_usuario     
 
validate_login