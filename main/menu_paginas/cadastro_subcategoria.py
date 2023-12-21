import tkinter
import customtkinter as ctk
import customtkinter
from utils.layout.front import *
import os
from banco_conections.conexao import *
from PIL import ImageTk, Image
from banco_conections.conexao_subcategorias import var_result, var_resultC

def cad_subcategoria():
    from banco_conections.conexao_subcategorias import query_subcategoria
    janela_subcategoria = customtkinter.CTkToplevel()
    janela_subcategoria.attributes("-topmost", True)
    janela_subcategoria.title("Cadastro de Sub-Categoria")
    janela_subcategoria.after(200, lambda: janela_subcategoria.iconbitmap("./imagens/logo_icone.ico")) # alterando o icone da janela
    janela_subcategoria.geometry("1000x550+250+70")
    janela_subcategoria.resizable(False, False)
    janela_subcategoria.grid_rowconfigure(0, weight=1)
    janela_subcategoria.grid_columnconfigure(1, weight=1)

    # Inserindo as imagens que serão utilizadas
    image_path = os.path.join(os.path.dirname(os.path.realpath(
        __file__)), "C:/sistema_estoque/imagens")

    background_image = customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "background_fornecedor.png")), size=(1000, 550))

    # Inserindo imagem de fundo
    label_background = customtkinter.CTkLabel(master=janela_subcategoria,
                                          text="",
                                          image=background_image)
    label_background.pack()
    
    #Label combobox segmento
    label_combobox = customtkinter.CTkLabel(master=janela_subcategoria,
                                             text="VINCULAR AO SEGMENTO",
                                             font=('Poppins bold', 13),
                                             width=40,
                                             height=20,
                                             fg_color=co4,
                                             bg_color="transparent")
    label_combobox.place(x=376, y=150, anchor=tkinter.CENTER)

    #Caixa para selecionar o segmento
    global var_combobox
    combobox = customtkinter.CTkOptionMenu(master=janela_subcategoria,
                                       values=var_result)
    combobox.configure(fg_color=co0, width=180, height=30)
    combobox.place(x=294, y=168)
    var_combobox = combobox.get()
    
    #Label combobox categoria
    label_combocategoria = customtkinter.CTkLabel(master=janela_subcategoria,
                                             text="VINCULAR A CATEGORIA",
                                             font=('Poppins bold', 13),
                                             width=40,
                                             height=20,
                                             fg_color=co4,
                                             bg_color="transparent")
    label_combocategoria.place(x=678, y=150, anchor=tkinter.CENTER)

    #Caixa para selecionar a categoria
    global var_Ccategoria
    combo_categoria = customtkinter.CTkOptionMenu(master=janela_subcategoria,
                                       values=var_resultC)
    combo_categoria.configure(fg_color=co0, width=180, height=30)
    combo_categoria.place(x=687, y=183, anchor=tkinter.CENTER)
    var_Ccategoria = combobox.get()
    
    #Label sub-categoria
    label_subcategoria = customtkinter.CTkLabel(master=janela_subcategoria,
                                             text="SUB-CATEGORIA",
                                             font=('Poppins bold', 13),
                                             width=40,
                                             height=20,
                                             fg_color=co4,
                                             bg_color="transparent")
    label_subcategoria.place(x=450, y=250, anchor=tkinter.CENTER)
    
    # Criando e configurando a entry sub-categoria
    entry_subcategoria = customtkinter.CTkEntry(master=janela_subcategoria,
                                        width=250,
                                        height=30,
                                        font=('Century gothic', 13),
                                        fg_color="transparent",
                                        bg_color="transparent",
                                        border_color=co0,
                                        placeholder_text='Insira o nome da categoria',
                                        justify='center')
    entry_subcategoria.place(x=520, y=285, anchor=tkinter.CENTER)

    def armazenar_subcategoria():
        
        global var_subcategoria
        var_subcategoria = entry_subcategoria.get()
    armazenar_subcategoria
    
    def clean_entrys():
        entry_subcategoria.delete(0, "end")
    clean_entrys
    
    
    # Criando e configurando o botão cadastrar
    button_cadastrar = customtkinter.CTkButton(master=janela_subcategoria, text="CADASTRAR",
                                            width=15,
                                            height=15,
                                            font=('Poppins Bold', 15),
                                            fg_color=co4,
                                            hover_color=co2,
                                            bg_color=co4,
                                            cursor='hand2')

    button_cadastrar.place(x=520, y=370, anchor=tkinter.CENTER)

    # Cadastrando as infomações do fornecedor no banco de dados
    button_cadastrar.configure(command=lambda:[armazenar_subcategoria(), query_subcategoria(), clean_entrys()])

    janela_subcategoria.mainloop()
    
cad_subcategoria
