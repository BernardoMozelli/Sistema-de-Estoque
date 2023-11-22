import tkinter
import customtkinter  as ctk
import customtkinter
from banco_conections.conexao import *
from utils.layout.front import *
from utils.functions import *
from PIL import ImageTk,Image

def remember_pass():
  from banco_conections.valid_reset import query_res
  #Criando e configurando a Janela cadastro
  janela_remember = ctk.CTkToplevel()  # Criando a janela
  janela_remember.title("Alterção de Senha") # Mudando o título da janela
  janela_remember.after(250, lambda: janela_remember.iconbitmap("./imagens/logo_icone.ico"))
  janela_remember.after(0, lambda: janela_remember.state('zoomed')) # Abrindo a janela em tela cheia
  janela_remember.minsize(900, 650)
  janela_remember.grab_set()
  janela_remember = janela_remember

  #Inserindo imagem de fundo
  img_logo=ImageTk.PhotoImage(Image.open("./imagens/background.png"))
  label_logo=customtkinter.CTkLabel(master=janela_remember, 
    text="",
    width=50,
    height=70,
    image=img_logo)
  label_logo.place(x=250, y=10)
  label_logo.pack()

  #Criando e configurando o frame 
  frame_remember=customtkinter.CTkFrame(master=janela_remember,
                      width=410, height=396,
                      border_width=2,
                      border_color=co3,
                      bg_color="transparent",
                      fg_color="transparent",
                      corner_radius=30)
  frame_remember.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

  # Criando e configurando a label Título
  label_titl = customtkinter.CTkLabel(frame_remember)
  label_titl.configure(text="ESQUECI MINHA SENHA",
                            font=('Poppins bold', 20),
                            width=150,
                            height=20,
                            fg_color=co2,
                            corner_radius=8)
  label_titl.place(x=215, y=65, anchor=tkinter.CENTER)
  
  #Criando e configurando a entry email
  global entry_mail
  entry_mail = ctk.CTkEntry(master=frame_remember,
                          width=320,
                          height=40,
                          font=('Century gothic', 14),
                          fg_color="transparent",
                          bg_color="transparent",
                          placeholder_text='Insira o seu e-mail',
                          justify='center')
  entry_mail.place(x=208, y=140, anchor=tkinter.CENTER)
  entry_mail.get()
  
  #Inserindo imagem entry mail
  img_mail=ImageTk.PhotoImage(Image.open("./imagens/mail1.png"))
  label_mail=customtkinter.CTkLabel(master=frame_remember, 
   text="",
   fg_color="transparent",
   bg_color="transparent",
   image=img_mail)
  label_mail.place(x=50, y=125)
  
  # Criando e configurando a entry usuário
  global entry_user
  entry_user = ctk.CTkEntry(master=frame_remember,
                          width=320,
                          height=40,
                          font=('Century gothic', 14),
                          fg_color="transparent",
                          bg_color="transparent",
                          placeholder_text='Insira o seu nome de usuário',
                          justify='center')
  entry_user.place(x=208, y=210, anchor=tkinter.CENTER)
  entry_user.get()
  
  #Inserindo imagem entry user
  img_user=ImageTk.PhotoImage(Image.open("./imagens/usuario.png"))
  label_user=customtkinter.CTkLabel(master=frame_remember, 
   text="",
   fg_color="transparent",
   bg_color="transparent",
   image=img_user)
  label_user.place(x=55, y=196)

  #Armazena dados inseridos na entry nas variáveis globais listadas abaixo
  def armazenar_r():
    global rmail, ruser
    rmail = entry_mail.get()  
    ruser = entry_user.get()
  armazenar_r
  

  # Criando e configurando o botão para envio do link
  button_remember = customtkinter.CTkButton(master=frame_remember, 
                                          text="ENVIAR LINK",
                                          width=200,
                                          height=40,
                                          font=('Poppins', 15),
                                          hover_color=co3,
                                          bg_color="transparent",
                                          fg_color=co2)
  button_remember.place(x=213, y=290, anchor=tkinter.CENTER)
  button_remember.configure(command=lambda:[armazenar_r(), query_res()])

  janela_remember.mainloop()
  
remember_pass()

