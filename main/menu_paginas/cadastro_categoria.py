import tkinter
import customtkinter as ctk
import customtkinter
from utils.layout.front import *
import os
from banco_conections.conexao import *
from banco_conections.conexao_forncedores import query_fornecedor
from PIL import ImageTk, Image

def cad_categoria():
    janela_categoria = customtkinter.CTkToplevel()
    janela_categoria.attributes("-topmost", True)
    janela_categoria.title("Cadastro de Categoria")
    janela_categoria.after(200, lambda: janela_categoria.iconbitmap("./imagens/logo_icone.ico")) # alterando o icone da janela
    janela_categoria.geometry("1000x550+250+70")
    janela_categoria.resizable(False, False)
    janela_categoria.grid_rowconfigure(0, weight=1)
    janela_categoria.grid_columnconfigure(1, weight=1)

    # Inserindo as imagens que serão utilizadas
    image_path = os.path.join(os.path.dirname(os.path.realpath(
        __file__)), "C:/sistema_estoque/imagens")

    background_image = customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "background_fornecedor.png")), size=(1000, 550))

    # Inserindo imagem de fundo
    label_background = customtkinter.CTkLabel(master=janela_categoria,
                                          text="",
                                          image=background_image)
    label_background.pack()


    janela_categoria.mainloop()
    
cad_categoria
