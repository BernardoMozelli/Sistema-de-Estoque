import tkinter
import customtkinter  as ctk
import customtkinter
from banco_conections.conexao import *
from banco_conections.conexao_cad import validate_query
from utils.layout.front import *
from utils.functions import *
from PIL import ImageTk,Image

def telade_cadastro():

  #Criando e configurando a Janela cadastro
  janela_cadastro = ctk.CTkToplevel()  # Criando a janela
  janela_cadastro.title("Cadastro") # Mudando o título da janela
  janela_cadastro.after(250, lambda: janela_cadastro.iconbitmap("./imagens/logo_icone.ico"))
  janela_cadastro.after(0, lambda: janela_cadastro.state('zoomed')) # Abrindo a janela em tela cheia
  janela_cadastro.minsize(900, 650)
  janela_cadastro.grab_set()
  janela_cadastro = janela_cadastro

  #Inserindo imagem de fundo
  img_logo=ImageTk.PhotoImage(Image.open("./imagens/background.png"))
  label_logo=customtkinter.CTkLabel(master=janela_cadastro, 
    text="",
    width=50,
    height=70,
    image=img_logo)
  label_logo.place(x=250, y=10)
  label_logo.pack()

  #Criando e configurando o frame 
  frameC=customtkinter.CTkFrame(master=janela_cadastro,
                      width=410, height=396,
                      border_width=2,
                      border_color=co3,
                      bg_color="transparent",
                      fg_color="transparent",
                      corner_radius=30)
  frameC.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

  # Criando e configurando a label Título
  label_titl = customtkinter.CTkLabel(frameC)
  label_titl.configure(text="CADASTRO DE USUÁRIO",
                            font=('Poppins bold', 20),
                            width=150,
                            height=20,
                            fg_color=co2,
                            corner_radius=8)
  label_titl.place(x=215, y=50, anchor=tkinter.CENTER)

  # Criando e configurando a entry nome completo
  entry_nome = customtkinter.CTkEntry(master=frameC,
                            width=320,
                            height=40,
                            font=('Century gothic', 14),
                            fg_color="transparent",
                            bg_color="transparent",
                            placeholder_text='Insira o seu nome completo',
                            justify='center')
  entry_nome.place(x=210, y=110, anchor=tkinter.CENTER)
  entry_nome.get()
  
  #Inserindo imagem entry nome
  img_nome=ImageTk.PhotoImage(Image.open("./imagens/formulario1.png"))
  label_nome=customtkinter.CTkLabel(master=frameC, 
   text="",
   fg_color="transparent",
   bg_color="transparent",
   image=img_nome)
  label_nome.place(x=57, y=96)
        
  global entry_mail
  entry_mail = ctk.CTkEntry(master=frameC,
                          width=320,
                          height=40,
                          font=('Century gothic', 14),
                          fg_color="transparent",
                          bg_color="transparent",
                          placeholder_text='Insira o seu endereço de e-mail',
                          justify='center')
  entry_mail.place(x=208, y=170, anchor=tkinter.CENTER)
  entry_mail.get()
  
  #Inserindo imagem entry mail
  img_mail=ImageTk.PhotoImage(Image.open("./imagens/mail1.png"))
  label_mail=customtkinter.CTkLabel(master=frameC, 
   text="",
   fg_color="transparent",
   bg_color="transparent",
   image=img_mail)
  label_mail.place(x=50, y=155)

# Criando e configurando a entry usuário
  global vuser
  entry_user = ctk.CTkEntry(master=frameC,
                          width=320,
                          height=40,
                          font=('Century gothic', 14),
                          fg_color="transparent",
                          bg_color="transparent",
                          placeholder_text='Insira o seu nome de usuário',
                          justify='center')
  entry_user.place(x=208, y=230, anchor=tkinter.CENTER)
  entry_user.get()
  
  #Inserindo imagem entry user
  img_user=ImageTk.PhotoImage(Image.open("./imagens/usuario.png"))
  label_user=customtkinter.CTkLabel(master=frameC, 
   text="",
   fg_color="transparent",
   bg_color="transparent",
   image=img_user)
  label_user.place(x=55, y=216)

  # Campo de digitação senha. Personalizando para quando o usuário digitar as suas credencias, a mesma seja ocultada
  global entry_senhac, vsenha
  entry_senhac = ctk.CTkEntry(master=frameC,
                           width=320,
                           height=40,
                           font=('Century gothic', 14),
                           fg_color="transparent",
                           bg_color="transparent",
                           placeholder_text='Insira a sua senha',
                           show="*",
                           justify='center')
  entry_senhac.place(x=208, y=290, anchor=tkinter.CENTER)
  entry_senhac.get()
  
  #Inserindo imagem entry senha
  img_senha=ImageTk.PhotoImage(Image.open("./imagens/senha1.png"))
  label_senha=customtkinter.CTkLabel(master=frameC, 
   text="",
   fg_color="transparent",
   bg_color="transparent",
   image=img_senha)
  label_senha.place(x=55, y=276)
  
  # Verifica se a opção mostrar senha esta habilitadaSe sim, ele exibe o conteúdo da entry senha.
  # Caso contrário, o conteudo é ocultado por *
  exb_pass2 = customtkinter.IntVar()
  def check_pass2():
    if exb_pass2.get() == 1:
      entry_senhac.configure(show='')
    else:
     entry_senhac.configure(show='*')
  check_pass2
  
  # Criando e configurando o checkbox
  checkbox_senha2 = customtkinter.CTkCheckBox(master=frameC, text="Exibir/Ocultar senha",
                                           variable=exb_pass2,
                                           width=5,
                                           height=3,
                                           hover_color=co3,
                                           fg_color=co2,
                                           bg_color=co0,
                                           font=('Poppins', 11))
  checkbox_senha2.place(x=125, y=330, anchor=tkinter.CENTER)
  checkbox_senha2.configure(command=check_pass2)

  #Armazena dados inseridos na entry nas variáveis globais listadas abaixo
  def armazenar():
    global vnome, vmail, vuser, vsenha
    vnome = entry_nome.get()
    vmail = entry_mail.get()
    vuser = entry_user.get()
    vsenha= entry_senhac.get()
  armazenar
        
  # Criando e configurando o botão de cadastro
  button_cadastro = customtkinter.CTkButton(master=frameC, 
                                          text="CADASTRAR",
                                          width=200,
                                          height=40,
                                          font=('Poppins', 15),
                                          hover_color=co3,
                                          bg_color="transparent",
                                          fg_color=co2)
  button_cadastro.place(x=213, y=365, anchor=tkinter.CENTER)
  button_cadastro.configure(command=lambda:[armazenar(), validate_query()])

  janela_cadastro.mainloop()
  
telade_cadastro()

