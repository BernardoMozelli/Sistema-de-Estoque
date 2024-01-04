import tkinter
from tkinter import ttk
import customtkinter as ctk
import customtkinter
from utils.layout.front import *
import os
import requests
import json
from PIL import ImageTk, Image
from banco_conections.conexao_entradaestoque import selected_fabricante, selected_fornecedor
from .CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown

def entrada_estoque():
    
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
    label_produto.place(x=193, y=96, anchor=tkinter.CENTER)

    # Criando e configurando a entry nome do produto
    global entry_nome
    entry_nome = customtkinter.CTkEntry(master=janela_entrada,
                                    width=250,
                                    height=20,
                                    font=('Century gothic', 13),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    border_color=co0,
                                    placeholder_text='Insira o produto',
                                    justify='center',
                                    corner_radius=10)
    entry_nome.place(x=290, y=125, anchor=tkinter.CENTER)
    entry_nome.get()
    
    # -----------------------------------------------------------------
    # Criando e configurando a label nome fantasia
    label_quantidade = customtkinter.CTkLabel(master=janela_entrada,
                                    text="QUANTIDADE",
                                    font=('Poppins bold', 12),
                                    width=40,
                                    height=20,
                                    fg_color=co4,
                                    bg_color="transparent")
    label_quantidade.place(x=626, y=96, anchor=tkinter.CENTER)

    # Criando e configurando a entry nome fantasia
    entry_quantidade = customtkinter.CTkEntry(master=janela_entrada,
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
    entry_quantidade.get()
    # -----------------------------------------------------------------

    # Criando e configurando a label setor
    label_segmento = customtkinter.CTkLabel(master=janela_entrada,
                                     text="SEGMENTO",
                                     font=('Poppins bold', 12),
                                     width=40,
                                     height=20,
                                     fg_color=co4,
                                     bg_color="transparent")
    label_segmento.place(x=198, y=164, anchor=tkinter.CENTER)

    #Caixa para selecionar segmento
    optionmenu_segmento = customtkinter.CTkOptionMenu(master=janela_entrada,
                                       dynamic_resizing=False)
    optionmenu_segmento.configure(fg_color=co0, width=200, height=30)
    optionmenu_segmento.set("SELECIONE O SEGMENTO")
    CTkScrollableDropdown(optionmenu_segmento, values=["Alimentos", "Bebida", "Papelaria", "Informática", "Eletrônicos", "Eletrodomésticos", "Cosmeticos", "Outros"])
    optionmenu_segmento.place(x=267, y=197, anchor=tkinter.CENTER)

    # -----------------------------------------------------------------
    
    # Criando e configurando a label descrição
    label_fabricante = customtkinter.CTkLabel(master=janela_entrada,
                                   text="FABRICANTE",
                                   font=('Poppins bold', 12),
                                   width=40,
                                   height=20,
                                   fg_color=co4,
                                   bg_color="transparent")
    label_fabricante.place(x=622, y=165, anchor=tkinter.CENTER)
    
    #Caixa para selecionar nome do fabricante
    optionmenu_fabricante = customtkinter.CTkOptionMenu(master=janela_entrada)
    optionmenu_fabricante.set("SELECIONE O FABRICANTE")
    optionmenu_fabricante.configure( width=380, height=30,
                                       dynamic_resizing=False,
                                       fg_color=co0,
                                       bg_color=co0)
    CTkScrollableDropdown(optionmenu_fabricante, values=[selected_fabricante])
    optionmenu_fabricante.place(x=775, y=198, anchor=tkinter.CENTER)

    # -----------------------------------------------------------------

    # Criando e configurando a label fornecedor
    label_fornecedor = customtkinter.CTkLabel(master=janela_entrada,
                                           text="FORNECEDOR",
                                           font=('Poppins bold', 12),
                                           width=40,
                                           height=20,
                                           fg_color=co4,
                                           bg_color="transparent")
    label_fornecedor.place(x=626, y=242, anchor=tkinter.CENTER)

    #Caixa para selecionar nome do fornecedor
    optionmenu_fornecedor = customtkinter.CTkOptionMenu(master=janela_entrada)
    optionmenu_fornecedor.set("SELECIONE O FORNECEDOR")
    optionmenu_fornecedor.configure( values=selected_fornecedor,
                                       dynamic_resizing=False,
                                       fg_color=co0,
                                       bg_color=co0)
    CTkScrollableDropdown(optionmenu_fornecedor, values=selected_fornecedor)
    optionmenu_fornecedor.configure(width=380, height=30)
    optionmenu_fornecedor.place(x=775, y=274, anchor=tkinter.CENTER)

    # -----------------------------------------------------------------
    # Criando e configurando a label fabricante
    label_modelo = customtkinter.CTkLabel(master=janela_entrada,
                                          text="MODELO",
                                          font=('Poppins bold', 12),
                                          width=40,
                                          height=20,
                                          fg_color=co4,
                                          bg_color="transparent")
    label_modelo.place(x=192, y=240, anchor=tkinter.CENTER)

    # Criando e configurando a caixa de seleção fabricante
    entry_modelo = customtkinter.CTkEntry(master=janela_entrada,
                                          width=250,
                                          height=20,
                                          font=('Century gothic', 13),
                                          fg_color="transparent",
                                          bg_color="transparent",
                                          border_color=co0,
                                          placeholder_text='Modelo',
                                          justify='center')
    entry_modelo.place(x=292, y=270, anchor=tkinter.CENTER)
    
    # -----------------------------------------------------------------
    # Criando e configurando a label data da compra
    label_datacompra = customtkinter.CTkLabel(master=janela_entrada,
                                      text="DATA DA COMPRA",
                                      font=('Poppins bold', 12),
                                      width=40,
                                      height=20,
                                      fg_color=co4,
                                      bg_color="transparent")
    label_datacompra.place(x=220, y=310, anchor=tkinter.CENTER)

    # Criando e configurando a entry data da compra
    entry_datacompra = customtkinter.CTkEntry(master=janela_entrada,
                                      width=250,
                                      height=20,
                                      font=('Century gothic', 13),
                                      fg_color="transparent",
                                      bg_color="transparent",
                                      border_color=co0,
                                      placeholder_text='Data da compra',
                                      justify='center')
    entry_datacompra.place(x=290, y=340, anchor=tkinter.CENTER)
    #formata o campo data da compra
    def format_data(event=None):
        entry_datacompra.get()
        text = entry_datacompra.get().replace("/", "")[:8]
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


            entry_datacompra.delete(0, "end")
            entry_datacompra.insert(0, new_text)
    format_data
    
    entry_datacompra.bind('<KeyRelease>', format_data)
    
    # -----------------------------------------------------------------
    # Criando e configurando a label valor da compra
    label_valor = customtkinter.CTkLabel(master=janela_entrada,
                                             text="VALOR DA COMPRA",
                                             font=('Poppins bold', 12),
                                             width=40,
                                             height=20,
                                             fg_color=co4,
                                             bg_color="transparent")
    label_valor.place(x=643, y=310, anchor=tkinter.CENTER)

    # Criando e configurando a entry valor da compra
    entry_valor = customtkinter.CTkEntry(master=janela_entrada,
                                             width=250,
                                             height=20,
                                             font=('Century gothic', 13),
                                             fg_color="transparent",
                                             bg_color="transparent",
                                             border_color=co0,
                                             placeholder_text='Valor da compra',
                                             justify='center')
    entry_valor.place(x=710, y=342, anchor=tkinter.CENTER)
    
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
    label_nseire.place(x=199, y=385, anchor=tkinter.CENTER)

    # Criando e configurando a entry status
    entry_nserie = customtkinter.CTkEntry(master=janela_entrada,
                                      width=250,
                                      height=20,
                                      font=('Century gothic', 13),
                                      fg_color="transparent",
                                      bg_color="transparent",
                                      border_color=co0,
                                      placeholder_text='Numero de serie',
                                      justify='center')
    entry_nserie.place(x=292, y=415, anchor=tkinter.CENTER)
    # -----------------------------------------------------------------
    
    # Criando e configurando a label telefone
    label_nota = customtkinter.CTkLabel(master=janela_entrada,
                                        text="Nº DA NOTA FISCAL",
                                        font=('Poppins bold', 12),
                                        width=40,
                                        height=20,
                                        fg_color=co4,
                                        bg_color="transparent")
    label_nota.place(x=643, y=390, anchor=tkinter.CENTER)

    # Criando e configurando a entry telefone
    entry_nota = customtkinter.CTkEntry(master=janela_entrada,
                                        width=250,
                                        height=20,
                                        font=('Century gothic', 13),
                                        fg_color="transparent",
                                        bg_color="transparent",
                                        border_color=co0,
                                        placeholder_text='Número da nota fiscal',
                                        justify='center')
    entry_nota.place(x=710, y=420, anchor=tkinter.CENTER)
    
    def cleaning_entry():
        entry_nome.delete(0, "end")
        entry_quantidade.delete(0, "end")
        entry_modelo.delete(0, "end")
        entry_datacompra.delete(0, "end")
        entry_valor.delete(0, "end")
        entry_nserie.delete(0, "end")
        entry_nota.delete(0, "end")
    cleaning_entry
    
     # ---------------------------------------------------------------------------------------
    
    # Quando clicado, as informações presentes nas entrys são apagadas para inserção de novos 
    # dados.
    #button_atualizarfabricante.configure(command=atualiza_ulvalorfabri)
    
    
    # Quando clicado, as informações presentes nas entrys são apagadas para inserção de novos 
    # dados.
    #button_clean.configure(command=cleaning_entry)'''

    #-----------------------------------------------------------------------------------------------------
    # Criando e configurando o botão cadastrar
    '''button_cadastrarF = customtkinter.CTkButton(master=janela_entrada, text="CADASTRAR",
                                            width=15,
                                            height=15,
                                            font=('Poppins Bold', 17),
                                            fg_color=co4,
                                            hover_color=co2,
                                            bg_color=co4,
                                            cursor='hand2')

    button_cadastrarF.place(x=501, y=475, anchor=tkinter.CENTER)

    # Cadastrando as infomações do fornecedor no banco de dados
    button_cadastrarF.configure(command=lambda:[query_fornecedor(), cleaning_entry()])'''


    janela_entrada.mainloop()
    
entrada_estoque