from banco_conections.conexao import con
from utils.mensagem_box import *
import sys

def query_res():
    from reset_senha import rmail, ruser
    from utils.esqueci_senha.email_send import mail_reset
    
    cursor = con.cursor()
    queryR = (("SELECT email and usuario FROM cadastro WHERE email ='{}' and usuario = '{}'".format(rmail, ruser)))
    cursor.execute(queryR)
    resultadoR = cursor.fetchall()
    
    while (rmail or ruser) == None:
        msg_aviso6()

    if len(resultadoR) == 0:  # Verifica se o retorno contém alguma linha. Se não conter, é exibida mensagem de erro
       msg_aviso6()
    else:
     msg_reset()
     mail_reset()
     
     con.commit()
    
     sys.exit()
    
query_res
           
           
    