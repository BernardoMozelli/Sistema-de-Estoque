import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from utils.layout.template_mailTicket import template_htmlTicket
import random
from utils.mensagem_box import *


def consulta_mail():
  from banco_conections.conexao import con
  from menu_paginas.suporte import var_mail
                  
  cursor = con.cursor()
  query_mail = (("SELECT email FROM cadastro WHERE email ='{}'".format(var_mail)))
  cursor.execute(query_mail)
  global resultado_ConsultaMail
  resultado_ConsultaMail = cursor.fetchall()
  
  if len(resultado_ConsultaMail)==0:
    erro_email()
  
consulta_mail


def mail_suporteTicket():
  from menu_paginas.suporte import var_titulo,var_mail, var_mensagem
  #Senha para apps gerado no site do google. Serve para que o python consiga autenticar na conta
  #de e-mail informada e faça o envio do e-mail de forma automatica.
  

  numero_aleatorio = random.randint(1,999999)
  numero_aleatorio = str(numero_aleatorio)
  
  global var_ticket
  var_ticket = numero_aleatorio

  #Informações do servidor e da conta de e-mail de envio
  port = 465
  smtp_server = "smtp.gmail.com"
  login = 'bernardommedeiros13@gmail.com' 
  
  #Senha para apps gerado no site do google. Serve para que o python consiga autenticar na conta
  #de e-mail informada e faça o envio do e-mail de forma automatica.
  password = 'jdoi ydtx vnyy ilxe'

  sender_email = "bernardommedeiros13@gmail.com"
  receiver_email = "bernardommedeiros13@gmail.com"
  message = MIMEMultipart("alternative")
  message2 = MIMEMultipart("alternative")
  message["Subject"] = "Ticket " + numero_aleatorio + " - "  + var_titulo
  message["From"] = sender_email
  message["To"] = receiver_email

  #Recebendo o template html
  body = MIMEText("Descrição: " + var_mensagem + "Remetente: " + var_mail)
  #body2 =  MIMEText("Remetente: " + var_mail, "html")
  
  message.attach(body)

  # Enviando o e-mail
  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(login, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
mail_suporteTicket

def consulta_mail():
  from banco_conections.conexao import con
  from menu_paginas.suporte import var_mail
                  
  cursor = con.cursor()
  query_mail = (("SELECT email FROM cadastro WHERE email ='{}'".format(var_mail)))
  cursor.execute(query_mail)
  global resultado_ConsultaMail
  resultado_ConsultaMail = cursor.fetchall()
  
  if len(resultado_ConsultaMail)==0:
    erro_email()
  
consulta_mail


def mail_suporteTicketUser():
  from menu_paginas.suporte import var_titulo,var_mail, var_mensagem
  #Senha para apps gerado no site do google. Serve para que o python consiga autenticar na conta
  #de e-mail informada e faça o envio do e-mail de forma automatica.
  

  numero_aleatorio = random.randint(1,999999)
  numero_aleatorio = str(numero_aleatorio)

  #Informações do servidor e da conta de e-mail de envio
  port = 465
  smtp_server = "smtp.gmail.com"
  login = 'bernardommedeiros13@gmail.com' 
  
  #Senha para apps gerado no site do google. Serve para que o python consiga autenticar na conta
  #de e-mail informada e faça o envio do e-mail de forma automatica.
  password = 'jdoi ydtx vnyy ilxe'

  sender_email = "bernardommedeiros13@gmail.com"
  receiver_email = var_mail
  message = MIMEMultipart("alternative")
  message["Subject"] = "Retorno Ticket - " + var_ticket
  message["From"] = sender_email
  message["To"] = receiver_email

  #Recebendo o template html
  part = MIMEText(template_htmlTicket, "html")
  
  message.attach(part)

  # Informando o diretorio e o nome do arquivo de imagem
  fp = open('./imagens/background_mailTicket.png', 'rb')
  background_mailTicket = MIMEImage(fp.read())

  # Especificando o ID de acordo com o img src no arquivo HTML
  background_mailTicket.add_header('Content-ID', '<background_mailTicket>')
  
  message.attach(background_mailTicket)
  

  # Enviando o e-mail
  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(login, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
mail_suporteTicketUser