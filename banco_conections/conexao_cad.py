# Query para vericar se usuário já esta cadastrado no banco
from tkinter import *
from utils.mensagem_box import *
from banco_conections.conexao import con
import re

def validate_query():
    from cadastro import vnome, vmail, vuser, vsenha
    cursor = con.cursor()
    queryC = (("SELECT email and usuario FROM cadastro WHERE email ='{}' and usuario = '{}'".format(vmail, vuser)))
    cursor.execute(queryC)
    resultado = cursor.fetchall() 

    while (vnome or vmail or vuser or vsenha) == (""):
        
     msg_aviso1()
     return vnome
 
    ########################################################################################################
    
    #Valida o nome informado pelo usuário, avaliando se o mesmo atende os requisitos pré estabelecidos
    patterN = r"^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ'\s]+$"
    re.compile(patterN)
    resultN = re.fullmatch(patterN, vnome)
    while not resultN:
     msg_aviso8()
     return vnome
    
    #Valida nome de usuário informado, avaliando se o mesmo atende os requisitos pré estabelecidos
    pattern2 = r"^(?!.*\s)([A-Za-z1-9]).{5,32}"
    re.compile(pattern2)
    resultU = re.fullmatch(pattern2, vuser)
    
    while not resultU:
     msg_aviso7()
     return vuser
 
    #Valida senha informada pelo usuário, avaliando se o mesmo atende os requisitos pré estabelecidos
    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,15}$"
    re.compile(pattern)
    result = re.fullmatch(pattern, vsenha)
    
    while not result and result != "Insira a sua senha":
     msg_aviso2()
     return vsenha
 
    #########################################################################################################  
    # Verifica se o retorno contém alguma linha
    if len(resultado) != 0:
        msg_aviso3()
    else:
     query = ("INSERT INTO cadastro (nome, email, usuario, senha) values(%s,%s,%s,%s)")
     val = (vnome, vmail, vuser, vsenha)
     cursor.execute(query, val)
     con.commit()
     msg_sucessoCad()
     
validate_query
         