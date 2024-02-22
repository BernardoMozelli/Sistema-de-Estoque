import tkinter
from tkinter import ttk
import customtkinter as ctk
import customtkinter
from utils.layout.front import *
import os
import requests
import json
from PIL import ImageTk, Image
from datetime import date


def suporte_chat():
    
    janela_suporte = customtkinter.CTkToplevel()
    janela_suporte.attributes("-topmost", True)
    janela_suporte.after(200, lambda: janela_suporte.iconbitmap("./imagens/logo_icone.ico")) # alterando o icone da janela
    janela_suporte.title("Entrada em estoque")
    #janela_suporte.geometry("1000x550+250+70")
    janela_suporte.resizable(False, False)
    janela_suporte.grid_rowconfigure(0, weight=1)
    janela_suporte.grid_columnconfigure(1, weight=1)

    # Inserindo as imagens que serão utilizadas
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "C:/sistema_estoque/imagens")

    background_image = customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "background_fornecedor.png")), size=(1000, 550))

    # Inserindo imagem de fundo
    label_background = customtkinter.CTkLabel(master=janela_suporte,
                                          text="",
                                          image=background_image)
    label_background.pack()

    # Criando e configurando a label nome
    label_titulo = customtkinter.CTkLabel(master=janela_suporte,
                                    text="TÍTULO",
                                    font=('Poppins bold', 13),
                                    width=40,
                                    height=20,
                                    fg_color=co4,
                                    bg_color="transparent")
    label_titulo.place(x=247, y=76, anchor=tkinter.CENTER)

    # Criando e configurando a entry nome do produto
    entry_título= customtkinter.CTkEntry(master=janela_suporte,
                                    width=300,
                                    height=25,
                                    font=('Century gothic', 13),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    border_color=co0,
                                    placeholder_text='Insira o título',
                                    justify='center',
                                    corner_radius=10)
    entry_título.place(x=375, y=105, anchor=tkinter.CENTER)
    
    # Criando e configurando a label nome
    label_data = customtkinter.CTkLabel(master=janela_suporte,
                                    text="DATA",
                                    font=('Poppins bold', 13),
                                    width=40,
                                    height=20,
                                    fg_color=co4,
                                    bg_color="transparent")
    label_data.place(x=646, y=75, anchor=tkinter.CENTER)

    # Criando e configurando a entry nome do produto
    entry_data= customtkinter.CTkEntry(master=janela_suporte,
                                    width=300,
                                    height=25,
                                    font=('Century gothic', 13),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    border_color=co0,
                                    justify='center',
                                    corner_radius=10)
    entry_data.place(x=775, y=105, anchor=tkinter.CENTER)
    
    data = date.today()
    dataFormatada = data.strftime('%d/%m/%Y')
    
    entry_data.insert(0, dataFormatada)

    
    # Criando e configurando a label mensagem
    label_mensagem = customtkinter.CTkLabel(master=janela_suporte,
                                    text="INSIRA A MENSAGEM",
                                    font=('Poppins bold', 13),
                                    width=40,
                                    height=20,
                                    fg_color=co4,
                                    bg_color="transparent")
    label_mensagem.place(x=575, y=175, anchor=tkinter.CENTER)
    
    # Criando o caixa de texto
    textbox = ctk.CTkTextbox(janela_suporte, width=620, height=200, activate_scrollbars=True)
    textbox.configure(bg_color=co0,
                      fg_color=co0)
    textbox.pack()
    textbox.place(x=575, y=297, anchor=tkinter.CENTER)

    # Criando e configurando o botão cadastrar
    button_suporte = customtkinter.CTkButton(master=janela_suporte, text="ENVIAR MENSAGEM",
                                            width=15,
                                            height=15,
                                            font=('Poppins Bold', 15),
                                            fg_color=co4,
                                            hover_color=co2,
                                            bg_color=co4,
                                            cursor='hand2')

    button_suporte.place(x=585, y=450, anchor=tkinter.CENTER)

    # Cadastrando as infomações do fornecedor no banco de dados
    #button_entradaestoque.configure(command=lambda:[armazenar_estoque(), valida_entradaestoque(), query_EntradaEstoque(), cleaning_entry()])

    janela_suporte.mainloop()
    
suporte_chat