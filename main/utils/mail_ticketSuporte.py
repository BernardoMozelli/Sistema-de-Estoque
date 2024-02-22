import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from utils.layout.template_mail import template_html
import random

def mail_suporteTicket():
  from reset_senha import rmail
  #Senha para apps gerado no site do google. Serve para que o python consiga autenticar na conta
  #de e-mail informada e faça o envio do e-mail de forma automatica.
  

  numero_aleatorio = random.randint(1,999999)

  #Informações do servidor e da conta de e-mail
  port = 465
  smtp_server = "smtp.gmail.com"
  login = 'bernardommedeiros13@gmail.com' 
  password = 'jdoi ydtx vnyy ilxe'

  sender_email = "bernardommedeiros13@gmail.com"
  receiver_email = rmail
  message = MIMEMultipart("alternative")
  message["Subject"] = "Ticket - " + numero_aleatorio
  message["From"] = sender_email
  message["To"] = receiver_email

  #Recebendo o template html
  part = MIMEText(template_html, "html")
  message.attach(part)

  # Informando o diretorio e o nome do arquivo de imagem
  fp = open('./imagens/template_mail.png', 'rb')
  background_mail = MIMEImage(fp.read())

  # Especificando o ID de acordo com o img src no arquivo HTML
  background_mail.add_header('Content-ID', '<background_image>')
  
  message.attach(background_mail)

  # Enviando o e-mail
  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(login, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
mail_suporteTicket