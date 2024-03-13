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
    from utils.mail_ticketSuporte import consulta_mail, mail_suporteTicket, mail_suporteTicketUser
    
    janela_suporte = customtkinter.CTkToplevel()
    janela_suporte.attributes("-topmost", True)
    janela_suporte.after(200, lambda: janela_suporte.iconbitmap("./imagens/logo_icone.ico")) # alterando o icone da janela
    janela_suporte.title("Entrada em estoque")
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

    # Criando e configurando a label titulo
    label_titulo = customtkinter.CTkLabel(master=janela_suporte,
                                    text="TÍTULO",
                                    font=('Poppins bold', 13),
                                    width=40,
                                    height=20,
                                    fg_color=co4,
                                    bg_color="transparent")
    label_titulo.place(x=247, y=76, anchor=tkinter.CENTER)

    # Criando e configurando a entry título
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
    
    #Criando a label e-mail
    label_email= customtkinter.CTkLabel(master=janela_suporte,
                                    text="E-MAIL",
                                    font=('Poppins bold', 13),
                                    width=40,
                                    height=20,
                                    fg_color=co4,
                                    bg_color="transparent")
    label_email.place(x=648, y=75, anchor=tkinter.CENTER)
    
    # Criando e configurando a entry email
    entry_email= customtkinter.CTkEntry(master=janela_suporte,
                                    width=300,
                                    height=25,
                                    font=('Century gothic', 13),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    placeholder_text='Insira o e-mail cadastrado',
                                    border_color=co0,
                                    justify='center',
                                    corner_radius=10)
    entry_email.place(x=775, y=105, anchor=tkinter.CENTER) 
    
    # Criando e configurando a label mensagem
    label_mensagem = customtkinter.CTkLabel(master=janela_suporte,
                                    text="INSIRA A MENSAGEM",
                                    font=('Poppins bold', 13),
                                    width=40,
                                    height=20,
                                    fg_color=co4,
                                    bg_color="transparent")
    label_mensagem.place(x=575, y=190, anchor=tkinter.CENTER)
    
    # Criando o caixa de texto
    mensagem_suporte = ctk.CTkTextbox(janela_suporte, width=420, height=150, activate_scrollbars=True)
    mensagem_suporte.configure(bg_color=co0,
                      fg_color=co0)
    mensagem_suporte.pack()
    mensagem_suporte.place(x=575, y=295, anchor=tkinter.CENTER)
    
    def armazenar_suporte():
        global var_titulo, var_data, var_mail, var_mensagem
        
        var_titulo = entry_título.get()
        var_mail = entry_email.get()
        var_mensagem = mensagem_suporte.get(0.0, 'end')
    armazenar_suporte

    # Criando e configurando o botão cadastrar
    button_suporte = customtkinter.CTkButton(master=janela_suporte, text="ENVIAR MENSAGEM",
                                            width=15,
                                            height=15,
                                            font=('Poppins Bold', 15),
                                            fg_color=co4,
                                            hover_color=co2,
                                            bg_color=co4,
                                            cursor='hand2')

    button_suporte.place(x=585, y=400, anchor=tkinter.CENTER)
    button_suporte.configure(command=lambda:[armazenar_suporte(), consulta_mail(), mail_suporteTicket(), mail_suporteTicketUser()])

    # Cadastrando as infomações do fornecedor no banco de dados
    #button_entradaestoque.configure(command=lambda:[armazenar_estoque(), valida_entradaestoque(), query_EntradaEstoque(), cleaning_entry()])

    janela_suporte.mainloop()
    
suporte_chat