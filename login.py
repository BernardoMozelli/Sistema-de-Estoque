import tkinter
import customtkinter as ctk
import customtkinter
from PIL import ImageTk, Image
from utils.layout.front import *
from utils.functions import *
from banco_conections.conexao import conect

################### criando a tela de login #################

# Criando e configurando a Janela login
janela_login = ctk.CTk()  # Criando a janela
janela_login.title("Login")  # Mudando o título da janela
janela_login.wm_iconbitmap(default="./imagens/logo_icone.ico")  # alterando o icone
janela_login.after(0, lambda: janela_login.state('zoomed'))  # Abrindo a janela em tela cheia
janela_login.minsize(900, 650)

janela_login = janela_login

conect()

# Inserindo imagem de fundo
img_logo = ImageTk.PhotoImage(Image.open("./imagens/background.png"))
label_logo = customtkinter.CTkLabel(master=janela_login,
                                    text="",
                                    width=50,
                                    height=70,
                                    image=img_logo)
label_logo.place(x=250, y=10)
label_logo.pack()

# Criando e configurando o frame
frame = customtkinter.CTkFrame(master=janela_login,
                               width=410, height=396,
                               border_width=2,
                               border_color=co4,
                               bg_color="transparent",
                               fg_color="transparent",
                               corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Criando e configurando a label Título
label_titulo = customtkinter.CTkLabel(master=frame,
                                      text="SISTEMA DE INVENTÁRIO",
                                      font=('Poppins bold', 20),
                                      width=150,
                                      height=20,
                                      fg_color=co2,
                                      corner_radius=8)
label_titulo.place(x=210, y=60, anchor=tkinter.CENTER)

# Criando e configurando a entry usuário
entry_user = customtkinter.CTkEntry(master=frame,
                                    width=320,
                                    height=40,
                                    font=('Century gothic', 14),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    placeholder_text='Insira o seu usuário',
                                    justify='center')
entry_user.place(x=200, y=125, anchor=tkinter.CENTER)
entry_user.get()

#Inserindo imagem entry user
img_user=ImageTk.PhotoImage(Image.open("./imagens/usuario.png"))
label_user=customtkinter.CTkLabel(master=frame, 
   text="",
   fg_color="transparent",
   bg_color="transparent",
   image=img_user)
label_user.place(x=46, y=112)

# Campo de digitação senha. Personalizando para quando o usuário digitar as suas credencias, a mesma seja ocultada
global entry_senha
entry_senha = customtkinter.CTkEntry(master=frame,
                                     width=320,
                                     height=40,
                                     font=('Century gothic', 14),
                                     fg_color="transparent",
                                     bg_color="transparent",
                                     placeholder_text='Insira a sua senha',
                                     show="*",
                                     justify='center')
entry_senha.place(x=200, y=200, anchor=tkinter.CENTER)
entry_senha.get()


#Inserindo imagem entry senha
img_senha=ImageTk.PhotoImage(Image.open("./imagens/senha1.png"))
label_senha=customtkinter.CTkLabel(master=frame, 
   text="",
   fg_color="transparent",
   bg_color="transparent",
   image=img_senha)
label_senha.place(x=45, y=185)

exb_pass = customtkinter.IntVar()

# Verifica se a opção mostrar senha esta habilitadaSe sim, ele exibe o conteúdo da entry senha.
# Caso contrário, o conteudo é ocultado por *

def check_pass():
    if exb_pass.get() == 1:
        entry_senha.configure(show='')
    else:
        entry_senha.configure(show='*')
        
check_pass

# Criando e configurando o checkbox
checkbox_senha = customtkinter.CTkCheckBox(master=frame, text="Exibir/Ocultar senha",
                                           variable=exb_pass,
                                           width=7,
                                           height=5,
                                           hover_color=co3,
                                           fg_color=co2,
                                           bg_color=co0,
                                           font=('Poppins', 11))
checkbox_senha.place(x=112, y=243, anchor=tkinter.CENTER)
checkbox_senha.configure(command=check_pass)

# #Criando e configurando o botão esqueceu a senha
button_remember = customtkinter.CTkButton(master=frame, text="Esqueci minha senha",
                                          width=100,
                                          height=15,
                                          font=('Poppins', 11),
                                          fg_color="transparent",
                                          hover_color=co2)

button_remember.place(x=300, y=242.2, anchor=tkinter.CENTER)
button_remember.configure(command=lambda:[reset(), conect()])

# Criando e configurando o botão "Não tem cadastro"
button_ntcad = customtkinter.CTkButton(master=frame, text="Não tem cadastro?. Clique aqui",
                                       width=100,
                                       height=15,
                                       font=('Poppins', 11),
                                       fg_color="transparent",
                                       hover_color=co2,
                                       )

button_ntcad.place(x=208, y=335, anchor=tkinter.CENTER)

button_ntcad.configure(command=lambda:[cad(), conect()])

button_login = customtkinter.CTkButton(master=frame, text="FAZER LOGIN",
                                       width=200,
                                       height=40,
                                       font=('Poppins', 15),
                                       hover_color=co3,
                                       bg_color="transparent",
                                       fg_color=co2)
button_login.place(x=208, y=300, anchor=tkinter.CENTER)

janela_login.mainloop()
