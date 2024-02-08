import tkinter
from tkinter import ttk
import customtkinter as ctk
import customtkinter
from utils.layout.front import *
import os
import requests
import json
from PIL import ImageTk, Image
from .CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown

def entrada_estoque():
    from banco_conections.conexao_entradaestoque import selected_fabricante, selected_fornecedor, selected_categoria, selected_subcategoria, atualizaFabricante_banco, atualizaFornecedor_banco, atualizaCategoria_banco, atualizaSubcategoria_banco, query_EntradaEstoque    
    from utils.validacoes_entestoque import valida_entradaestoque
    
    janela_entrada = customtkinter.CTkToplevel()
    janela_entrada.attributes("-topmost", True)
    janela_entrada.after(200, lambda: janela_entrada.iconbitmap("./imagens/logo_icone.ico")) # alterando o icone da janela
    janela_entrada.title("Entrada em estoque")
    #janela_entrada.geometry("1000x550+250+70")
    janela_entrada.resizable(False, False)
    janela_entrada.grid_rowconfigure(0, weight=1)
    janela_entrada.grid_columnconfigure(1, weight=1)

    # Inserindo as imagens que serão utilizadas
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "C:/sistema_estoque/imagens")

    background_image = customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "background_fornecedor.png")), size=(1000, 550))
    
    vetor_atualizar = customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "atualizar.png")), size=(17, 17))

    # Inserindo imagem de fundo
    label_background = customtkinter.CTkLabel(master=janela_entrada,
                                          text="",
                                          image=background_image)
    label_background.pack()

    # Criando e configurando a label nome
    label_produto = customtkinter.CTkLabel(master=janela_entrada,
                                    text="PRODUTO",
                                    font=('Poppins bold', 12),
                                    width=40,
                                    height=20,
                                    fg_color=co4,
                                    bg_color="transparent")
    label_produto.place(x=193, y=76, anchor=tkinter.CENTER)

    # Criando e configurando a entry nome do produto
    entry_nome = customtkinter.CTkEntry(master=janela_entrada,
                                    width=250,
                                    height=25,
                                    font=('Century gothic', 13),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    border_color=co0,
                                    placeholder_text='Insira o produto',
                                    justify='center',
                                    corner_radius=10)
    entry_nome.place(x=290, y=105, anchor=tkinter.CENTER)
    
    # -----------------------------------------------------------------
    # Criando e configurando a label nome fantasia
    label_quantidade = customtkinter.CTkLabel(master=janela_entrada,
                                    text="QUANTIDADE",
                                    font=('Poppins bold', 12),
                                    width=40,
                                    height=20,
                                    fg_color=co4,
                                    bg_color="transparent")
    label_quantidade.place(x=626, y=76, anchor=tkinter.CENTER)

    # Criando e configurando a entry nome fantasia
    entry_quantidade = customtkinter.CTkEntry(master=janela_entrada,
                                    width=250,
                                    height=25,
                                    font=('Century gothic', 13),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    border_color=co0,
                                    placeholder_text='Insira a quantidade',
                                    justify='center',
                                    corner_radius=10)
    entry_quantidade.place(x=710, y=106, anchor=tkinter.CENTER)
    # -----------------------------------------------------------------
    # Criando e configurando a label setor
    label_segmento = customtkinter.CTkLabel(master=janela_entrada,
                                     text="SEGMENTO",
                                     font=('Poppins bold', 12),
                                     width=40,
                                     height=20,
                                     fg_color=co4,
                                     bg_color="transparent")
    label_segmento.place(x=198, y=144, anchor=tkinter.CENTER)

    #Caixa para selecionar segmento
    global var_validaseg
    optionmenu_segmento = customtkinter.CTkOptionMenu(master=janela_entrada,
                                       dynamic_resizing=False)
    optionmenu_segmento.configure(fg_color=co0, width=250, height=30)
    optionmenu_segmento.set("SELECIONE O SEGMENTO")
    CTkScrollableDropdown(optionmenu_segmento, values=["Alimentos", "Bebida", "Papelaria", "Informática", "Eletrônicos", "Eletrodomésticos", "Cosmeticos", "Outros"])
    optionmenu_segmento.place(x=290, y=177, anchor=tkinter.CENTER)
    var_validaseg = optionmenu_segmento.get()

    # -----------------------------------------------------------------
    
    # Criando e configurando a label descrição
    label_fabricante = customtkinter.CTkLabel(master=janela_entrada,
                                   text="FABRICANTE",
                                   font=('Poppins bold', 12),
                                   width=40,
                                   height=20,
                                   fg_color=co4,
                                   bg_color="transparent")
    label_fabricante.place(x=622, y=145, anchor=tkinter.CENTER)
    
    #Caixa para selecionar nome do fabricante
    global optionmenu_fabricante, var_fabri
    optionmenu_fabricante = customtkinter.CTkOptionMenu(master=janela_entrada)
    optionmenu_fabricante.set("SELECIONE O FABRICANTE")
    optionmenu_fabricante.configure( width=370, height=30,
                                       dynamic_resizing=False,
                                       fg_color=co0,
                                       bg_color=co0)
    CTkScrollableDropdown(optionmenu_fabricante, values=selected_fabricante)
    atualizaFabricante_banco
    optionmenu_fabricante.place(x=770, y=178, anchor=tkinter.CENTER)
    var_fabri = optionmenu_fabricante.get()

    # -----------------------------------------------------------------

    # Criando e configurando a label fabricante
    label_modelo = customtkinter.CTkLabel(master=janela_entrada,
                                          text="MODELO",
                                          font=('Poppins bold', 12),
                                          width=40,
                                          height=20,
                                          fg_color=co4,
                                          bg_color="transparent")
    label_modelo.place(x=192, y=220, anchor=tkinter.CENTER)

    # Criando e configurando a caixa de seleção fabricante
    entry_modelo = customtkinter.CTkEntry(master=janela_entrada,
                                          width=250,
                                          height=25,
                                          font=('Century gothic', 13),
                                          fg_color="transparent",
                                          bg_color="transparent",
                                          border_color=co0,
                                          placeholder_text='Modelo',
                                          justify='center')
    entry_modelo.place(x=292, y=250, anchor=tkinter.CENTER)
    
    # -----------------------------------------------------------------
    # Criando e configurando a label fornecedor
    label_fornecedor = customtkinter.CTkLabel(master=janela_entrada,
                                           text="FORNECEDOR",
                                           font=('Poppins bold', 12),
                                           width=40,
                                           height=20,
                                           fg_color=co4,
                                           bg_color="transparent")
    label_fornecedor.place(x=626, y=222, anchor=tkinter.CENTER)

    #Caixa para selecionar nome da fornecedor
    global optionmenu_fornecedor
    optionmenu_fornecedor = customtkinter.CTkOptionMenu(master=janela_entrada)
    optionmenu_fornecedor.set("SELECIONE O FORNECEDOR")
    optionmenu_fornecedor.configure(   
                                       dynamic_resizing=False,
                                       fg_color=co0,
                                       bg_color=co0)
    CTkScrollableDropdown(optionmenu_fornecedor, values=selected_fornecedor)
    atualizaFornecedor_banco
    optionmenu_fornecedor.configure(width=370, height=30)
    optionmenu_fornecedor.place(x=770, y=254, anchor=tkinter.CENTER)

    # -----------------------------------------------------------------
    # Criando e configurando a label categoria
    label_categoria = customtkinter.CTkLabel(master=janela_entrada,
                                           text="CATEGORIA",
                                           font=('Poppins bold', 12),
                                           width=40,
                                           height=20,
                                           fg_color=co4,
                                           bg_color="transparent")
    label_categoria.place(x=202, y=288, anchor=tkinter.CENTER)

    #Caixa para selecionar nome da categoria
    global optionmenu_categoria
    optionmenu_categoria = customtkinter.CTkOptionMenu(master=janela_entrada)
    optionmenu_categoria.set("SELECIONE A CATEGORIA")
    optionmenu_categoria.configure( 
                                       dynamic_resizing=False,
                                       fg_color=co0,
                                       bg_color=co0)
    CTkScrollableDropdown(optionmenu_categoria, values=selected_categoria)
    atualizaCategoria_banco
    optionmenu_categoria.configure(width=250, height=30)
    optionmenu_categoria.place(x=292, y=320, anchor=tkinter.CENTER)
        
    # -----------------------------------------------------------------
    
    # Criando e configurando a label sub-categoria
    label_subcategoria = customtkinter.CTkLabel(master=janela_entrada,
                                           text="SUB-CATEGORIA",
                                           font=('Poppins bold', 12),
                                           width=40,
                                           height=20,
                                           fg_color=co4,
                                           bg_color="transparent")
    label_subcategoria.place(x=215, y=357, anchor=tkinter.CENTER)

    #Caixa para selecionar nome da sub-categoria
    global optionmenu_subcategoria
    optionmenu_subcategoria = customtkinter.CTkOptionMenu(master=janela_entrada)
    optionmenu_subcategoria.set("SELECIONE A SUB-CATEGORIA")
    optionmenu_subcategoria.configure( 
                                       dynamic_resizing=False,
                                       fg_color=co0,
                                       bg_color=co0)
    CTkScrollableDropdown(optionmenu_subcategoria, values=selected_subcategoria)
    atualizaSubcategoria_banco
    optionmenu_subcategoria.configure(width=250, height=30)
    optionmenu_subcategoria.place(x=292, y=393, anchor=tkinter.CENTER)
    
    # -----------------------------------------------------------------
    
    # Criando e configurando a label data da compra
    label_datacompra = customtkinter.CTkLabel(master=janela_entrada,
                                      text="DATA DO CADASTRO",
                                      font=('Poppins bold', 12),
                                      width=40,
                                      height=20,
                                      fg_color=co4,
                                      bg_color="transparent")
    label_datacompra.place(x=226, y=430, anchor=tkinter.CENTER)

    # Criando e configurando a entry data da compra
    entry_data = customtkinter.CTkEntry(master=janela_entrada,
                                      width=250,
                                      height=25,
                                      font=('Century gothic', 13),
                                      fg_color="transparent",
                                      bg_color="transparent",
                                      border_color=co0,
                                      placeholder_text='Data da compra',
                                      justify='center')
    entry_data.place(x=290, y=460, anchor=tkinter.CENTER)
    
    #formata o campo data da compra
    def format_data(event=None):
        entry_data.get()
        text = entry_data.get().replace("/", "")[:8]
        new_text = ""

        if event.keysym.lower() == "backspace":
            return

        for index in range(len(text)):

            if not text[index] in "0123456789":
                continue
            if index in [1]:
               new_text += text[index] + "/"
            elif index == 3:
                new_text += text[index] + "/"
            else:
               new_text += text[index]


            entry_data.delete(0, "end")
            entry_data.insert(0, new_text)
            
            global var_validadata
            var_validadata = entry_data.get()
    format_data
    
    entry_data.bind('<KeyRelease>', format_data)
    
    # -----------------------------------------------------------------
    # Criando e configurando a label valor da compra
    label_valor = customtkinter.CTkLabel(master=janela_entrada,
                                             text="VALOR TOTAL DA COMPRA",
                                             font=('Poppins bold', 12),
                                             width=40,
                                             height=20,
                                             fg_color=co4,
                                             bg_color="transparent")
    label_valor.place(x=665, y=290, anchor=tkinter.CENTER)

    # Criando e configurando a entry valor da compra
    global var_validavalor
    entry_valor = customtkinter.CTkEntry(master=janela_entrada,
                                             width=250,
                                             height=25,
                                             font=('Century gothic', 13),
                                             fg_color="transparent",
                                             bg_color="transparent",
                                             border_color=co0,
                                             placeholder_text='Valor da compra',
                                             justify='center')
    entry_valor.place(x=710, y=322, anchor=tkinter.CENTER)
    var_validavalor = entry_valor.get()
    
    #Formata valores inseridos na entry valor para formato monetário
    def format_valor(event = None):
        text = entry_valor.get().replace(",", "").replace(".", "")[:100]
        new_text = ""
        
        if event.keysym.lower() == "backspace": return

        for index in range(len(text)):
            cont=len(text)
            #if not text[index] in "0123456789" and text2[index] in entry_valor: continue
            if index in [cont-3]: new_text += text[index] + ","
            elif index in [cont-6,cont-9]: new_text += text[index] + "."
            else: new_text += text[index]
    
        entry_valor.delete(0, "end")
        entry_valor.insert(0, new_text)
               
    format_valor
    
    def cifrao():
        entry_valor.insert(0, "R$")
    cifrao
    
    entry_valor.bind('<KeyRelease>', command=format_valor)
    
    
    # -----------------------------------------------------------------
    # Criando e configurando a label status
    label_nseire = customtkinter.CTkLabel(master=janela_entrada,
                                      text="Nº DE SÉRIE",
                                      font=('Poppins bold', 12),
                                      width=40,
                                      height=20,
                                      fg_color=co4,
                                      bg_color="transparent")
    label_nseire.place(x=618, y=433, anchor=tkinter.CENTER)

    # Criando e configurando a entry status
    entry_nserie = customtkinter.CTkEntry(master=janela_entrada,
                                      width=250,
                                      height=25,
                                      font=('Century gothic', 13),
                                      fg_color="transparent",
                                      bg_color="transparent",
                                      border_color=co0,
                                      placeholder_text='Numero de serie',
                                      justify='center')
    entry_nserie.place(x=710, y=465, anchor=tkinter.CENTER)
    # -----------------------------------------------------------------
    
    # Criando e configurando a label telefone
    label_estado = customtkinter.CTkLabel(master=janela_entrada,
                                        text="CONDIÇÃO",
                                        font=('Poppins bold', 12),
                                        width=40,
                                        height=20,
                                        fg_color=co4,
                                        bg_color="transparent")
    label_estado.place(x=620, y=358, anchor=tkinter.CENTER)

    #Caixa para selecionar nome da sub-categoria
    optionmenu_condicao = customtkinter.CTkOptionMenu(master=janela_entrada)
    optionmenu_condicao.set("SELECIONE A CONDIÇÃO")
    optionmenu_condicao.configure( 
                                       dynamic_resizing=False,
                                       fg_color=co0,
                                       bg_color=co0)
    CTkScrollableDropdown(optionmenu_condicao, values=["NOVO", "USADO"])
    optionmenu_condicao.configure(width=250, height=30)

    optionmenu_condicao.place(x=712, y=392, anchor=tkinter.CENTER)
    
    
    def cleaning_entry():
        entry_nome.delete(0, "end")
        entry_quantidade.delete(0, "end")
        entry_modelo.delete(0, "end")
        entry_data.delete(0, "end")
        entry_valor.delete(0, "end")
        entry_nserie.delete(0, "end")
    cleaning_entry
    
    def armazenar_estoque():
        global var_nomevalida, var_validaquantidade, var_validaseg, var_fabri, var_validamodelo, var_fornec, var_categoria, var_subcategoria, var_validadata, var_validavalor, var_validanserie, var_condicao

        var_nomevalida = entry_nome.get()
        var_validaquantidade = entry_quantidade.get()
        var_validaseg = optionmenu_segmento.get()
        var_fabri = optionmenu_fabricante.get()
        var_validamodelo = entry_modelo.get()
        var_fornec = optionmenu_fornecedor.get()
        var_categoria = optionmenu_categoria.get()
        var_subcategoria = optionmenu_subcategoria.get()
        var_validavalor = entry_valor.get()
        var_validadata = entry_data.get()
        var_validanserie = entry_nserie.get()
        var_condicao = optionmenu_condicao.get()
    armazenar_estoque
        
    #-----------------------------------------------------------------------------------------------------    
    
    # Criando e configurando o botão cadastrar
    button_atualizaBanco = customtkinter.CTkButton(master=janela_entrada, text="ATUALIZAR",
                                            width=15,
                                            height=15,
                                            font=('Poppins Bold', 11),
                                            fg_color=co4,
                                            hover_color=co2,
                                            bg_color=co4,
                                            cursor='hand2')

    button_atualizaBanco.place(x=505, y=480, anchor=tkinter.CENTER)
    button_atualizaBanco.configure(command=lambda:[atualizaFabricante_banco(), atualizaFornecedor_banco(), atualizaCategoria_banco(), atualizaSubcategoria_banco()])
    
    # Criando e configurando o botão cadastrar
    button_entradaestoque = customtkinter.CTkButton(master=janela_entrada, text="CADASTRAR",
                                            width=15,
                                            height=15,
                                            font=('Poppins Bold', 15),
                                            fg_color=co4,
                                            hover_color=co2,
                                            bg_color=co4,
                                            cursor='hand2')

    button_entradaestoque.place(x=505, y=520, anchor=tkinter.CENTER)

    # Cadastrando as infomações do fornecedor no banco de dados
    button_entradaestoque.configure(command=lambda:[armazenar_estoque(), valida_entradaestoque(), query_EntradaEstoque(), cleaning_entry()])

    janela_entrada.mainloop()
    
entrada_estoque