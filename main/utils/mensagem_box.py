from CTkMessagebox import CTkMessagebox
import sys

#Mensagem login
def msg_loginErro():
  global show_LoginErro
  show_LoginErro = CTkMessagebox(
        title="Login - Erro",
        message="Nome do Usuário ou senha incorreto. Tente novamente!!!",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
msg_loginErro

def msg_loginSucesso():
  global show_LoginSucesso
  show_LoginSucesso = CTkMessagebox(
        title="Login",
        message="Login realizado com sucesso !!!",
        icon="check", option_1="Ok",
        fade_in_duration=(2))
msg_loginErro


#Mensagem cadastro de usuário
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

#---------------------------------------------------------------------------------------------------------------------------------
#Mensagens esqueci minha senha

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

#---------------------------------------------------------------------------------------------------------------------------------
#Mensagens erro Banco de dados
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

#---------------------------------------------------------------------------------------------------------------------------------

#Reset de senha mensagem
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

#---------------------------------------------------------------------------------------------------------------------------------

#Mensagens cadastro de fornecedor/fabricante
def msg_cnpjincorreto():
  global show_avisoCNPJ
  show_avisoCNPJ = CTkMessagebox( 
        title="Consulta de CNPJ - Aviso",
        message="O número de cnpj informado está incorreto. Verifique os números fornecidos e tente novamente!!!",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
msg_cnpjincorreto

def msg_sucessoCadCategoria():
 global show_sucesso_categoria
 show_sucesso_categoria = CTkMessagebox(
        title="Cadastro de Categoria",
        message="Cadastro realizado com sucesso",
        icon="check", option_1="Ok",
        fade_in_duration=(2))
msg_sucessoCadCategoria

def msg_sucessoCadFabricante():
 global show_sucesso_fornecedor
 show_sucesso_fornecedor = CTkMessagebox(
        title="Cadastro de Fabricante",
        message="Cadastro realizado com sucesso",
        icon="check", option_1="Ok",
        fade_in_duration=(2))
msg_sucessoCadFabricante

def msg_sucessoCadFornecedor():
 global show_sucesso_fornecedor
 show_sucesso_fornecedor = CTkMessagebox(
        title="Cadastro de Fornecedor",
        message="Cadastro realizado com sucesso",
        icon="check", option_1="Ok",
        fade_in_duration=(2))
msg_sucessoCadFornecedor

def msg_sucessoEntradaestoque():
 global showsucesso_EntradaEstoque
 showsucesso_EntradaEstoque = CTkMessagebox(
        title="Cadastro de Produto",
        message="Cadastro realizado com sucesso!!!",
        icon="check", option_1="Ok",
        fade_in_duration=(2))
msg_sucessoEntradaestoque

def msg_sucessoSaidaEstoque():
 global show_sucesso_SaidaEstoque
 show_sucesso_SaidaEstoque = CTkMessagebox(
        title="Movimentação de Saída de Produto",
        message="Saída de produto do estoque foi realizada com sucesso!!!",
        icon="check", option_1="Ok",
        fade_in_duration=(2))
msg_sucessoSaidaEstoque

def msgErroCadastroCategoria():
 global show_erro_categoria
 show_erro_categoria = CTkMessagebox(
        title="Cadastro de Categoria",
        message="Erro ao realizar cadastro da categoria. Verifique as informações fornecidas e tente novamente!!!",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
msgErroCadastroCategoria

def msgErroCadastrofabricante():
 global show_erro_fabricante
 show_erro_fabricante = CTkMessagebox(
        title="Cadastro de Fabricante",
        message="Erro ao realizar cadastro do fabricante. Verifique as informações fornecidas e tente novamente!!!",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
msgErroCadastrofabricante

def msgErroFabricanteExiste():
  global show_fabricanteexiste
  show_fabricanteexiste = CTkMessagebox(
        title="Aviso - Cadastro de Fabricante",
        message="O fabricante informado já está cadastrado!!!",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
msgErroFabricanteExiste

def msgErroFornecedorExiste():
  global show_fabricanteexiste
  show_fabricanteexiste = CTkMessagebox(
        title="Aviso - Cadastro de Fornecedor",
        message="O fornecedor informado já está cadastrado!!!",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
msgErroFornecedorExiste

def msgErroCadastrofornecedor():
 global show_erro_fornecedor
 show_erro_fornecedor = CTkMessagebox(
        title="Cadastro de Fornecedor",
        message="Erro ao realizar cadastro do fornecedor. Verifique as informações fornecidas e tente novamente!!!",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
msgErroCadastrofornecedor

def msgErroEntradaestoque():
 global show_erro_entradaestoque
 show_erro_entradaestoque = CTkMessagebox(
        title="Erro - Entrada/Estoque",
        message="Erro ao realizar a entrada do produto no estoque. Favor preencher todos os campos!!!",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
msgErroEntradaestoque

def msgErroSaidaEstoque():
 global show_erro_SaidaEstoque
 show_erro_SaidaEstoque = CTkMessagebox(
        title="Erro - Saida/Estoque",
        message="Erro ao realizar a movimentação de saída do produto do estoque.Favor entrar em contato com a equipe de suporte",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
msgErroSaidaEstoque

def msgErroValidaSaidaEstoque():
 global show_erro_validaSaidaEstoque
 show_erro_validaSaidaEstoque = CTkMessagebox(
        title="Saida/Estoque",
        message="Erro ao realizar a movimentação de saída do produto do estoque. Favor preencher todos os campos!!!",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
msgErroValidaSaidaEstoque

def msg_sucessoRelatorioCompleto():
 global show_sucesso_RelatorioCompleto
 show_sucesso_RelatorioCompleto = CTkMessagebox(
        title="Relatório Completo",
        message="Relatório gerado com sucesso!!!",
        icon="check", option_1="Ok",
        fade_in_duration=(2))
msg_sucessoRelatorioCompleto

def msgErroRelatorioCompleto():
 global show_erro_RelatorioCompleto
 show_erro_RelatorioCompleto = CTkMessagebox(
        title="Saida/Estoque",
        message="Ocorreu um erro ao tentar gerar o relatório. Favor entrar em contato com o suporte!!!",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
msgErroRelatorioCompleto

def msgErroRelatorioCompletoEntry():
 global show_erro_RelatorioCompletoEntry
 show_erro_RelatorioCompletoEntry = CTkMessagebox(
        title="Saida/Estoque",
        message="Ocorreu um erro ao tentar gerar o relatório. Verifique as informações fornecidas e tente novamente!!!",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
msgErroRelatorioCompletoEntry

def erro_email():
 global show_errorEmail
 show_errorEmail = CTkMessagebox(
        title="Erro",
        message="O e-mail informado não foi encontrado em nossa base de dados!!",
        icon="warning", option_1="Ok")
erro_email

def erro_Envioemail():
 global show_errorEnvioEmail
 show_errorEnvioEmail = CTkMessagebox(
        title="Erro",
        message="Ocorreu um erro ao tentar realizar o registro do seu chamado. Tente novamente mais tarde.",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
erro_Envioemail

def email_sucessoTicket():
 global show_EmailSucesso
 show_EmailSucesso = CTkMessagebox(
        title="E-mail enviado",
        message="Ticket aberto com sucesso. Favor acompanhar as atualizações de seu atendimento através do e-mail cadastrado.",
        icon="check", option_1="Ok",
        fade_in_duration=(2))
email_sucessoTicket

 
 
    


