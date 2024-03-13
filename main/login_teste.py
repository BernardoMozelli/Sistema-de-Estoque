import tkinter
import os
import customtkinter as ctk
import customtkinter
from PIL import ImageTk, Image
from utils.layout.front import *
from utils.functions import *
from utils.mensagem_box import *
from banco_conections.conexao import conect

################### criando a tela de login #################

janela_login = ctk.CTk()  # Criando a janela
janela_login.title("Login")  # Mudando o título da janela
janela_login.wm_iconbitmap(default="./imagens/logo_icone.ico")  # alterando o icone
janela_login.geometry("1000x550+250+70")
janela_login.resizable(False, False)


# Inserindo as imagens que serão utilizadas
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "C:/sistema_estoque/imagens")

background_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "background_login.jpg")), size=(1000, 550))
logo_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "logo_transparent_home.png")), size=(50, 50))

# Inserindo imagem de fundo
label_background = customtkinter.CTkLabel(janela_login,
                                    text="",
                                    image=background_image)
label_background.pack()

# Criando e configurando o frame
frame = customtkinter.CTkFrame(master=janela_login,
                               width=410, height=396,
                               bg_color=co4,
                               fg_color="transparent",
                               corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


janela_login.mainloop()
