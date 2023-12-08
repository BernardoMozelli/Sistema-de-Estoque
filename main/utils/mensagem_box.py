from CTkMessagebox import CTkMessagebox
import sys

def msg_aviso1():
  global show_aviso1
  show_aviso1 = CTkMessagebox(
        title="Cadastro de usuário - Aviso",
        message="Favor verificar as informações fornecidas!!!",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
msg_aviso1

def msg_aviso2():
  global show_aviso2
  show_aviso2 = CTkMessagebox(
        title="Cadastro de usuário - Aviso",
        message="Dados fornecidos para senha não atendem aos requisitos mínimos aceitáveis (min 8, max 15 dígitos, letra, número e caracter especial",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
msg_aviso2


def msg_aviso3():
  global show_aviso3
  show_aviso3 = CTkMessagebox(
        title="Cadastro de usuário - Aviso",
        message="Usuário já cadastrado!!!",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
msg_aviso3

def msg_aviso4():
  global show_aviso4
  show_aviso4 = CTkMessagebox(
        title="Esqueci minha senha - Aviso",
        message="O endereço de e-mail fornecido não é válido!!!",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
  resposta = show_aviso4.get()
  if resposta == "Ok":
       global show_aviso5
       show_aviso5 = CTkMessagebox(
       title="Esqueci minha senha - Aviso",
       message="Informe um endereço válido para que possamos prosseguir com a sua solicitação.",
       icon="warning", option_1="Ok",
       fade_in_duration=(2))
msg_aviso4

def msg_aviso6():
  global show_aviso6
  show_aviso6 = CTkMessagebox(
        title="Esqueci minha senha - Aviso",
        message="Usuário não encontrado em nossa base de dados. Favor verificar as informações fornecidas!!!",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
msg_aviso6

def msg_aviso7():
  global show_aviso7
  show_aviso7 = CTkMessagebox(
        title="Cadastro de usuário - Aviso",
        message="Dados fornecidos no campo (usuário) não atendem aos requisitos mínimos aceitáveis.",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
  resposta = show_aviso7.get()

  if resposta == "Ok":
   global show_aviso8
   show_aviso8 = CTkMessagebox(
        title="Cadastro de usuário - Aviso",
        message = "Minímo de 5 dígitos, máximo de 32 e não pode conter ('espaços' '.' ',')",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
msg_aviso7

def msg_aviso8():
  global show_aviso8
  show_aviso8 = CTkMessagebox(
        title="Cadastro de usuário - Aviso",
        message="Dados fornecidos no campo (nome completo) não atendem aos requisitos mínimos aceitáveis.",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
  resposta = show_aviso8.get()

  if resposta == "Ok":
   global show_aviso9
   show_aviso9 = CTkMessagebox(
        title="Cadastro de usuário - Aviso",
        message = "Favor inserir apenas letras!!!",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
msg_aviso8

def msg_error1():
  global show_error1
  show_error1 = CTkMessagebox(
        title="Connection Timeout",
        message="Não foi possível realizar conexão com o servidor!!!",
        icon="Error", option_1="Ok",
        fade_in_duration=(2))
msg_error1

def msg_error2():
  global show_error2
  show_error2 = CTkMessagebox(
        title="Connection failed",
        message="Não foi possível realizar conexão com o banco de dados!!!",
        icon="Error", option_1="Ok",
        fade_in_duration=(2))
msg_error2

def msg_error3():
  from banco_conections.conexao import err
  global show_error3
  show_error3 = CTkMessagebox(
        title="Connection failed",
        message="Erro: {}".format(err),
        icon="error", option_1="Ok",
        fade_in_duration=(2))
msg_error3

def msg_sucessoCad():
 global show_sucesso
 show_sucesso = CTkMessagebox(
        title="Cadastro de usuário",
        message="O cadastro foi realizado com sucesso",
        icon="check", option_1="Ok",
        fade_in_duration=(2))
 resposta = show_sucesso.get()
 
 if resposta == "Ok":
    sys.exit()
msg_sucessoCad

#Reset pass mensagem
def msg_reset():
    global show_msgmail, show_msgmail2
    show_msgmail = CTkMessagebox(title="Reset de Senha", 
                                 message="Um link de confirmação foi enviado para o e-mail cadastrado.",
                                 fade_in_duration=(2))
    resposta = show_msgmail.get()
    if resposta == "Ok":
       show_msgmail2 = CTkMessagebox(title="Reset de Senha", 
                                  message="Verifique a sua caixa de entrada para prosseguir com a alteração!!!",
                                  fade_in_duration=(2))
msg_reset

def msg_cnpjincorreto():
  global show_avisoCNPJ
  show_avisoCNPJ = CTkMessagebox( 
        title="Consulta de CNPJ - Aviso",
        message="O número de cnpj informado está incorreto. Verifique os números fornecidos e tente novamente!!!",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
msg_cnpjincorreto

def msg_sucessoCadFornecedor():
 global show_sucesso_fornecedor
 show_sucesso_fornecedor = CTkMessagebox(
        title="Cadastro de fornecedor",
        message="Cadastro realizado com sucesso",
        icon="check", option_1="Ok",
        fade_in_duration=(2))
 resposta = show_sucesso_fornecedor.get()
 
 if resposta == "Ok":
    import home
    home
msg_sucessoCadFornecedor