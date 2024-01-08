import tkinter
import customtkinter as ctk
import customtkinter
from utils.layout.front import *
import os
from banco_conections.conexao import *
from PIL import ImageTk, Image
from banco_conections.conexao_categorias import valida_cadastroCategoria, query_categoria

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
    
        
    label_optionmenucategoria = customtkinter.CTkLabel(master=janela_categoria,
                                             text="SEGMENTO",
                                             font=('Poppins bold', 13),
                                             width=40,
                                             height=20,
                                             fg_color=co4,
                                             bg_color="transparent")
    label_optionmenucategoria.place(x=330, y=150, anchor=tkinter.CENTER)

    #Caixa para selecionar segmento
    global var_optionmenucategoria
    optionmenucategoria = customtkinter.CTkOptionMenu(master=janela_categoria,
                                       values=["Alimentos", "Bebida", "Papelaria", "Informática", "Eletrônicos", "Eletrodomésticos", "Cosmeticos", "Outros"])
    optionmenucategoria.configure(fg_color=co0, width=180, height=30)
    optionmenucategoria.set("Informatica")  # setando valor inicial
    optionmenucategoria.place(x=294, y=168)
    var_optionmenucategoria = optionmenucategoria.get()
    
    label_categoria = customtkinter.CTkLabel(master=janela_categoria,
                                             text="CATEGORIA",
                                             font=('Poppins bold', 13),
                                             width=40,
                                             height=20,
                                             fg_color=co4,
                                             bg_color="transparent")
    label_categoria.place(x=600, y=150, anchor=tkinter.CENTER)
    
    # Criando e configurando a entry categoria
    entry_categoria = customtkinter.CTkEntry(master=janela_categoria,
                                        width=250,
                                        height=30,
                                        font=('Century gothic', 13),
                                        fg_color="transparent",
                                        bg_color="transparent",
                                        border_color=co0,
                                        placeholder_text='Insira o nome da categoria',
                                        justify='center')
    entry_categoria.place(x=687, y=183, anchor=tkinter.CENTER)

    def armazenar_categoria():    
        global var_categoria
        var_categoria = entry_categoria.get()
    armazenar_categoria
    
    def clean_entryc():
        entry_categoria.delete(0, "end")
    clean_entryc
    
    # Criando e configurando o botão cadastrar
    button_cadastrar = customtkinter.CTkButton(master=janela_categoria, text="CADASTRAR",
                                            width=15,
                                            height=15,
                                            font=('Poppins Bold', 15),
                                            fg_color=co4,
                                            hover_color=co2,
                                            bg_color=co4,
                                            cursor='hand2')

    button_cadastrar.place(x=520, y=270, anchor=tkinter.CENTER)

    # Cadastrando as infomações do fornecedor no banco de dados
    button_cadastrar.configure(command=lambda:[armazenar_categoria(), valida_cadastroCategoria(), query_categoria(), clean_entryc()])

    janela_categoria.mainloop()
    
cad_categoria
