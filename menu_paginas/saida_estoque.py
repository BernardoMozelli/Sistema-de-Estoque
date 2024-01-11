import tkinter
from tkinter import ttk
import customtkinter as ctk
import customtkinter
from utils.layout.front import *
import os
import requests
import json
from PIL import ImageTk, Image
from banco_conections.conexao_saidaEstoque import selected_produto, selected_modelo, selected_entcategoria, selected_Entsubcategoria,selected_nserie, query_ProdutoEntrada
from .CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown

def movimentaEstoque_saida():
    
    from utils.validacoes_entestoque import valida_SaidaEstoque
    
    janela_SaidaProduto = customtkinter.CTkToplevel()
    janela_SaidaProduto.attributes("-topmost", True)
    janela_SaidaProduto.after(200, lambda: janela_SaidaProduto.iconbitmap("./imagens/logo_icone.ico")) # alterando o icone da janela
    janela_SaidaProduto.title("Movimentação de Saída/estoque")
    #janela_SaidaProduto.geometry("1000x550+250+70")
    janela_SaidaProduto.resizable(False, False)
    janela_SaidaProduto.grid_rowconfigure(0, weight=1)
    janela_SaidaProduto.grid_columnconfigure(1, weight=1)

    # Inserindo as imagens que serão utilizadas
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "C:/sistema_estoque/imagens")

    background_image = customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "background_fornecedor.png")), size=(1000, 550))
    
    customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "atualizar.png")), size=(17, 17))

    # Inserindo imagem de fundo
    label_background = customtkinter.CTkLabel(master=janela_SaidaProduto,
                                          text="",
                                          image=background_image)
    label_background.pack()

    # Criando e configurando a label nome
    label_produto = customtkinter.CTkLabel(master=janela_SaidaProduto,
                                    text="PRODUTO",
                                    font=('Poppins bold', 12),
                                    width=40,
                                    height=20,
                                    fg_color=co4,
                                    bg_color="transparent")
    label_produto.place(x=193, y=96, anchor=tkinter.CENTER)

    #Caixa para selecionar nome do produto
    global var_saidaProduto
    optionmenu_produto = customtkinter.CTkOptionMenu(master=janela_SaidaProduto)
    optionmenu_produto.set("SELECIONE O PRODUTO")
    optionmenu_produto.configure( 
                                       dynamic_resizing=False,
                                       fg_color=co0,
                                       bg_color=co0)
    optionmenu_produto.configure(width=380, height=30)
    optionmenu_produto.place(x=354, y=125, anchor=tkinter.CENTER)
    CTkScrollableDropdown(optionmenu_produto, values=selected_produto)
    var_saidaProduto = optionmenu_produto.get()
    
    # -----------------------------------------------------------------
    # Criando e configurando a label nome fantasia
    label_quantidade = customtkinter.CTkLabel(master=janela_SaidaProduto,
                                    text="QUANTIDADE",
                                    font=('Poppins bold', 12),
                                    width=40,
                                    height=20,
                                    fg_color=co4,
                                    bg_color="transparent")
    label_quantidade.place(x=626, y=96, anchor=tkinter.CENTER)

    # Criando e configurando a entry nome fantasia
    entry_quantidade = customtkinter.CTkEntry(master=janela_SaidaProduto,
                                    width=250,
                                    height=20,
                                    font=('Century gothic', 13),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    border_color=co0,
                                    placeholder_text='Insira a quantidade',
                                    justify='center',
                                    corner_radius=10)
    entry_quantidade.place(x=710, y=126, anchor=tkinter.CENTER)
    # -----------------------------------------------------------------

    # Criando e configurando a label fabricante
    label_modelo = customtkinter.CTkLabel(master=janela_SaidaProduto,
                                          text="MODELO",
                                          font=('Poppins bold', 12),
                                          width=40,
                                          height=20,
                                          fg_color=co4,
                                          bg_color="transparent")
    label_modelo.place(x=191, y=164, anchor=tkinter.CENTER)
    
    optionmenu_modelo = customtkinter.CTkOptionMenu(master=janela_SaidaProduto)
    optionmenu_modelo.set("SELECIONE O MODELO")
    optionmenu_modelo.configure( width=380, height=30,
                                       dynamic_resizing=False,
                                       fg_color=co0,
                                       bg_color=co0)
    optionmenu_modelo.place(x=355, y=197, anchor=tkinter.CENTER)
    CTkScrollableDropdown(optionmenu_modelo, values=selected_modelo)

    # ----------------------------------------------------------------------------------------------------------------------
    
    label_categoria = customtkinter.CTkLabel(master=janela_SaidaProduto,
                                           text="CATEGORIA",
                                           font=('Poppins bold', 12),
                                           width=40,
                                           height=20,
                                           fg_color=co4,
                                           bg_color="transparent")
    label_categoria.place(x=620, y=242, anchor=tkinter.CENTER)
   
    #Caixa para selecionar nome da categoria
    optionmenu_categoria = customtkinter.CTkOptionMenu(master=janela_SaidaProduto)
    optionmenu_categoria.set("SELECIONE A CATEGORIA")
    optionmenu_categoria.configure( 
                                       dynamic_resizing=False,
                                       fg_color=co0,
                                       bg_color=co0)
    optionmenu_categoria.configure(width=380, height=30)
    optionmenu_categoria.place(x=775, y=274, anchor=tkinter.CENTER)
    CTkScrollableDropdown(optionmenu_categoria, values=selected_entcategoria)
        
    # -----------------------------------------------------------------
    
    # Criando e configurando a label sub-categoria
    label_subcategoria = customtkinter.CTkLabel(master=janela_SaidaProduto,
                                           text="SUB-CATEGORIA",
                                           font=('Poppins bold', 12),
                                           width=40,
                                           height=20,
                                           fg_color=co4,
                                           bg_color="transparent")
    label_subcategoria.place(x=215, y=235, anchor=tkinter.CENTER)

    #Caixa para selecionar nome da sub-categoria
    optionmenu_subcategoria = customtkinter.CTkOptionMenu(master=janela_SaidaProduto)
    optionmenu_subcategoria.set("SELECIONE A SUB-CATEGORIA")
    optionmenu_subcategoria.configure( 
                                       dynamic_resizing=False,
                                       fg_color=co0,
                                       bg_color=co0)
    CTkScrollableDropdown(optionmenu_subcategoria, values=selected_Entsubcategoria)
    optionmenu_subcategoria.configure(width=380, height=30)
    optionmenu_subcategoria.place(x=354, y=270, anchor=tkinter.CENTER)
    
    # -----------------------------------------------------------------
               
    # Criando e configurando a label número de série
    label_nseire = customtkinter.CTkLabel(master=janela_SaidaProduto,
                                      text="Nº DE SÉRIE",
                                      font=('Poppins bold', 12),
                                      width=40,
                                      height=20,
                                      fg_color=co4,
                                      bg_color="transparent")
    label_nseire.place(x=622, y=165, anchor=tkinter.CENTER)
    
    #Criando e configurando o option menu número de série
    optionmenu_nserie = customtkinter.CTkOptionMenu(master=janela_SaidaProduto)
    optionmenu_nserie.set("SELECIONE O Nº DE SÉRIE")
    optionmenu_nserie.configure( 
                                       dynamic_resizing=False,
                                       fg_color=co0,
                                       bg_color=co0)
    optionmenu_nserie.configure(width=380, height=30)
    optionmenu_nserie.place(x=775, y=198, anchor=tkinter.CENTER)
    CTkScrollableDropdown(optionmenu_nserie, values=selected_nserie)
    
    #Armazenando informações em variáveis
    def armazena_SaidaProduto():
        global var_Entquantidade, var_saidaProduto, var_SaidaModelo, varSaida_Categoria, var_SaidaSubcategoria, var_SaidaNSerie
        var_Entquantidade = entry_quantidade.get()
        var_saidaProduto = optionmenu_produto.get()
        var_SaidaModelo = optionmenu_modelo.get()
        var_SaidaModelo = optionmenu_modelo.get()
        varSaida_Categoria = optionmenu_categoria.get()
        var_SaidaSubcategoria = optionmenu_subcategoria.get()
        var_SaidaNSerie = optionmenu_nserie.get()
    armazena_SaidaProduto
    
    # Criando e configurando o botão cadastrar
    button_entradaestoque = customtkinter.CTkButton(master=janela_SaidaProduto, text="CADASTRAR",
                                            width=15,
                                            height=15,
                                            font=('Poppins Bold', 17),
                                            fg_color=co4,
                                            hover_color=co2,
                                            bg_color=co4,
                                            cursor='hand2')

    button_entradaestoque.place(x=527, y=390, anchor=tkinter.CENTER)

    # Cadastrando as infomações do fornecedor no banco de dados
    button_entradaestoque.configure(command=lambda:[armazena_SaidaProduto(), valida_SaidaEstoque(), query_ProdutoEntrada()])


    janela_SaidaProduto.mainloop()
    
movimentaEstoque_saida