import tkinter
import customtkinter as ctk
import customtkinter
from utils.layout.front import *
import os
import requests
import json
from string import ascii_letters
from banco_conections.conexao import *
from banco_conections.conexao_fornecedores import query_fornecedor
from PIL import ImageTk, Image


def cad_fornecedor():
    janela_fornecedor = customtkinter.CTkToplevel()
    janela_fornecedor.attributes("-topmost", True)
    janela_fornecedor.after(200, lambda: janela_fornecedor.iconbitmap("./imagens/logo_icone.ico")) # alterando o icone da janela
    janela_fornecedor.title("Cadastro de Fornecedor")
    janela_fornecedor.geometry("1000x550+250+70")
    janela_fornecedor.resizable(False, False)
    janela_fornecedor.grid_rowconfigure(0, weight=1)
    janela_fornecedor.grid_columnconfigure(1, weight=1)

    # Inserindo as imagens que serão utilizadas
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "C:/sistema_estoque/imagens")


    background_image = customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "background_fornecedor.png")), size=(1000, 550))
    
    vetor_consulta = customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "consulta_cnpj.png")), size=(17, 17))
    
    vetor_clean = customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "clean_entry.png")), size=(17, 17))

    # Inserindo imagem de fundo
    label_background = customtkinter.CTkLabel(master=janela_fornecedor,
                                          text="",
                                          image=background_image)
    label_background.pack()

    # Criando e configurando a label CNPJ
    label_cnpj = customtkinter.CTkLabel(master=janela_fornecedor,
                                    text="CNPJ",
                                    font=('Poppins bold', 12),
                                    width=40,
                                    height=20,
                                    fg_color=co4,
                                    bg_color="transparent")
    label_cnpj.place(x=185, y=76, anchor=tkinter.CENTER)

    # Criando e configurando a entry CNPJ
    global entry_cnpj
    entry_cnpj = customtkinter.CTkEntry(master=janela_fornecedor,
                                    width=250,
                                    height=20,
                                    font=('Century gothic', 13),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    border_color=co0,
                                    placeholder_text='Insira o cnpj',
                                    justify='center',
                                    corner_radius=10)
    entry_cnpj.place(x=290, y=105, anchor=tkinter.CENTER)
    entry_cnpj.get()

    # Formata a entry CNPJ para a normativa padrão
    def mascara_cnpj(event=None):   
        if len(entry_cnpj.get()) == 2:
            entry_cnpj.insert(END, '.')
        if len(entry_cnpj.get()) == 6:
            entry_cnpj.insert(END, '.')
        if len(entry_cnpj.get()) == 10:
            entry_cnpj.insert(END, '/')
        if len(entry_cnpj.get()) == 15:
            entry_cnpj.insert(END, '-')
        if len(entry_cnpj.get()) > 18:
            entry_cnpj.delete(18, "end")
    mascara_cnpj

    entry_cnpj.bind('<KeyRelease>', mascara_cnpj)
    # -----------------------------------------------------------------
    # Criando e configurando a label nome fantasia
    label_nome = customtkinter.CTkLabel(master=janela_fornecedor,
                                    text="NOME FANTASIA",
                                    font=('Poppins bold', 12),
                                    width=40,
                                    height=20,
                                    fg_color=co4,
                                    bg_color="transparent")
    label_nome.place(x=635, y=76.5, anchor=tkinter.CENTER)

    # Criando e configurando a entry nome fantasia
    entry_nome = customtkinter.CTkEntry(master=janela_fornecedor,
                                    width=250,
                                    height=20,
                                    font=('Century gothic', 13),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    border_color=co0,
                                    placeholder_text='Nome fantasia',
                                    justify='center',
                                    corner_radius=10)
    entry_nome.place(x=710, y=106, anchor=tkinter.CENTER)
    entry_nome.get()
    # -----------------------------------------------------------------

    # Criando e configurando a label razão social
    label_razao = customtkinter.CTkLabel(master=janela_fornecedor,
                                     text="RAZÃO SOCIAL",
                                     font=('Poppins bold', 12),
                                     width=40,
                                     height=20,
                                     fg_color=co4,
                                     bg_color="transparent")
    label_razao.place(x=209, y=164, anchor=tkinter.CENTER)

    # Criando e configurando a entry razão social
    entry_razao = customtkinter.CTkEntry(master=janela_fornecedor,
                                     width=250,
                                     height=20,
                                     font=('Century gothic', 13),
                                     fg_color="transparent",
                                     bg_color="transparent",
                                     border_color=co0,
                                     placeholder_text='Razão social',
                                     justify='center',
                                     corner_radius=10)
    entry_razao.place(x=290, y=193, anchor=tkinter.CENTER)
    entry_razao.get()

    # -----------------------------------------------------------------
    # Criando e configurando a label CEP
    label_cep = customtkinter.CTkLabel(master=janela_fornecedor,
                                   text="CEP",
                                   font=('Poppins bold', 12),
                                   width=40,
                                   height=20,
                                   fg_color=co4,
                                   bg_color="transparent")
    label_cep.place(x=605, y=165, anchor=tkinter.CENTER)

    # Criando e configurando a entry cep
    global entry_cep
    entry_cep = customtkinter.CTkEntry(master=janela_fornecedor,
                                   width=250,
                                   height=20,
                                   font=('Century gothic', 13),
                                   fg_color="transparent",
                                   bg_color="transparent",
                                   border_color=co0,
                                   placeholder_text='CEP',
                                   justify='center')
    entry_cep.place(x=710, y=194, anchor=tkinter.CENTER)

    # Formata a entry CEP para a normativa padrão


    def mascara_cep(event=None):
        if len(entry_cep.get()) == 5:
            entry_cep.insert(END, '-')
        if len(entry_cep.get()) > 9:
            entry_cep.delete(9, "end")


    entry_cep.bind('<KeyRelease>', mascara_cep)

    # -----------------------------------------------------------------
    # Criando e configurando a label logradouro
    label_logradouro = customtkinter.CTkLabel(master=janela_fornecedor,
                                          text="ENDEREÇO",
                                          font=('Poppins bold', 12),
                                          width=40,
                                          height=20,
                                          fg_color=co4,
                                          bg_color="transparent")
    label_logradouro.place(x=196, y=240, anchor=tkinter.CENTER)

    # Criando e configurando a entry logradouro
    entry_logradouro = customtkinter.CTkEntry(master=janela_fornecedor,
                                          width=250,
                                          height=20,
                                          font=('Century gothic', 13),
                                          fg_color="transparent",
                                          bg_color="transparent",
                                          border_color=co0,
                                          placeholder_text='Logradouro',
                                          justify='center')
    entry_logradouro.place(x=290, y=270, anchor=tkinter.CENTER)
    # -----------------------------------------------------------------

    # Criando e configurando a label logradouro
    label_complemento = customtkinter.CTkLabel(master=janela_fornecedor,
                                           text="COMPLEMENTO",
                                           font=('Poppins bold', 12),
                                           width=40,
                                           height=20,
                                           fg_color=co4,
                                           bg_color="transparent")
    label_complemento.place(x=630, y=242, anchor=tkinter.CENTER)

    # Criando e configurando a entry logradouro
    entry_complemento = customtkinter.CTkEntry(master=janela_fornecedor,
                                           width=250,
                                           height=20,
                                           font=('Century gothic', 13),
                                           fg_color="transparent",
                                           bg_color="transparent",
                                           border_color=co0,
                                           placeholder_text='Complemento do logradouro',
                                           justify='center')
    entry_complemento.place(x=710, y=272, anchor=tkinter.CENTER)
    # -----------------------------------------------------------------
    # Criando e configurando a label bairro
    label_bairro = customtkinter.CTkLabel(master=janela_fornecedor,
                                      text="BAIRRO",
                                      font=('Poppins bold', 12),
                                      width=40,
                                      height=20,
                                      fg_color=co4,
                                      bg_color="transparent")
    label_bairro.place(x=189, y=310, anchor=tkinter.CENTER)

    # Criando e configurando a entry bairro
    entry_bairro = customtkinter.CTkEntry(master=janela_fornecedor,
                                      width=250,
                                      height=20,
                                      font=('Century gothic', 13),
                                      fg_color="transparent",
                                      bg_color="transparent",
                                      border_color=co0,
                                      placeholder_text='Bairro',
                                      justify='center')
    entry_bairro.place(x=290, y=340, anchor=tkinter.CENTER)
    # -----------------------------------------------------------------
    # Criando e configurando a label bairro
    label_cidade_estado = customtkinter.CTkLabel(master=janela_fornecedor,
                                             text="CIDADE - ESTADO",
                                             font=('Poppins bold', 12),
                                             width=40,
                                             height=20,
                                             fg_color=co4,
                                             bg_color="transparent")
    label_cidade_estado.place(x=639, y=313, anchor=tkinter.CENTER)

    # Criando e configurando a entry bairro
    entry_cidade_estado = customtkinter.CTkEntry(master=janela_fornecedor,
                                             width=250,
                                             height=20,
                                             font=('Century gothic', 13),
                                             fg_color="transparent",
                                             bg_color="transparent",
                                             border_color=co0,
                                             placeholder_text='Cidade - Estado',
                                             justify='center')
    entry_cidade_estado.place(x=710, y=342, anchor=tkinter.CENTER)
    # -----------------------------------------------------------------
    # Criando e configurando a label status
    label_status = customtkinter.CTkLabel(master=janela_fornecedor,
                                      text="STATUS",
                                      font=('Poppins bold', 12),
                                      width=40,
                                      height=20,
                                      fg_color=co4,
                                      bg_color="transparent")
    label_status.place(x=189, y=385, anchor=tkinter.CENTER)

    # Criando e configurando a entry status
    entry_status = customtkinter.CTkEntry(master=janela_fornecedor,
                                      width=250,
                                      height=20,
                                      font=('Century gothic', 13),
                                      fg_color="transparent",
                                      bg_color="transparent",
                                      border_color=co0,
                                      placeholder_text='Status',
                                      justify='center')
    entry_status.place(x=292, y=415, anchor=tkinter.CENTER)
    # -----------------------------------------------------------------
    # Criando e configurando a label telefone
    label_telefone = customtkinter.CTkLabel(master=janela_fornecedor,
                                        text="TELEFONE",
                                        font=('Poppins bold', 12),
                                        width=40,
                                        height=20,
                                        fg_color=co4,
                                        bg_color="transparent")
    label_telefone.place(x=613, y=390, anchor=tkinter.CENTER)

    # Criando e configurando a entry telefone
    entry_telefone = customtkinter.CTkEntry(master=janela_fornecedor,
                                        width=250,
                                        height=20,
                                        font=('Century gothic', 13),
                                        fg_color="transparent",
                                        bg_color="transparent",
                                        border_color=co0,
                                        placeholder_text='Telefone',
                                        justify='center')
    entry_telefone.place(x=710, y=420, anchor=tkinter.CENTER)

    # API Consulta de CNPJ. A mesma insere os dados resultantes da
    # consulta nos respectivos campos
    
    #Valida se o campo cnpj foi preenchido
    def valida_cadastroFornecedor():
        #Valida o módulo cadastro de fabricante
        var_validacnpj = entry_cnpj.get()
        while var_validacnpj == "":
            msgErroCadastrofornecedor()
            return var_validacnpj
        else:
            msg_sucessoCadFornecedor
    valida_cadastroFornecedor

    def consulta_cnpj(event=None):
        cnpj = entry_cnpj.get().replace('.', '').replace('/', '').replace('-', '').strip()
        url = 'https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj)
        req = requests.get(url)
        code = req.status_code
        if code == 200:
            html = req.text
            receita = json.loads(html)
        try:
            entry_nome.insert(INSERT, format(receita['fantasia']))
            entry_razao.insert(INSERT, format(receita['nome']))
            entry_cep.insert(INSERT, format(receita['cep'].replace('.', '')))
            entry_logradouro.insert(INSERT, format(receita['logradouro']))
            entry_logradouro.insert(INSERT, ','*1)
            entry_logradouro.insert(INSERT, ' Nº: '*1)
            entry_logradouro.insert(INSERT, format(receita['numero']))
            entry_complemento.insert(INSERT, format(receita['complemento']))
            entry_bairro.insert(INSERT, format(receita['bairro']))
            entry_cidade_estado.insert(INSERT, format(receita['municipio']))
            entry_cidade_estado.insert(INSERT, ' - '*1)
            entry_cidade_estado.insert(INSERT, format(receita['uf']))
            entry_status.insert(INSERT, format(receita['situacao']))
            entry_telefone.insert(INSERT, format(receita['telefone']))

            global var_cnpj, var_nome, var_razao, var_cep, var_logradouro, var_complemento, var_bairro, var_cidade_estado, var_status, var_telefone
            var_cnpj = entry_cnpj.get()
            var_nome = entry_nome.get()
            var_razao = entry_razao.get()
            var_cep = entry_cep.get()
            var_logradouro = entry_logradouro.get()
            var_complemento = entry_complemento.get()
            var_bairro = entry_bairro.get()
            var_cidade_estado = entry_cidade_estado.get()
            var_status = entry_status.get()
            var_telefone = entry_telefone.get()
            
                    
            if var_nome == "":
                entry_nome.insert(0, var_razao)
                var_nome = entry_nome.get()
            
            if var_complemento == "":
               entry_complemento.insert(0, "NÃO POSSUI")
               var_complemento = entry_complemento.get()
            
        except:
            msg_cnpjincorreto
            
    consulta_cnpj
    
    def cleaning_entry():
        entry_cnpj.delete(0, "end")
        entry_nome.delete(0, "end")
        entry_razao.delete(0, "end")
        entry_cep.delete(0, "end")
        entry_logradouro.delete(0, "end")
        entry_complemento.delete(0, "end")
        entry_bairro.delete(0, "end")
        entry_cidade_estado.delete(0, "end")
        entry_status.delete(0, "end")
        entry_telefone.delete(0, "end")
    cleaning_entry
    
    # ---------------------------------------------------------------------------------------
    # Criando e configurando o botão consultar
    button_consultar = customtkinter.CTkButton(master=janela_fornecedor, text="",
                                           width=15,
                                           height=15,
                                           font=('Poppins Bold', 10),
                                           fg_color=co4,
                                           bg_color=co4,
                                           image=vetor_consulta,
                                           cursor='hand2')

    button_consultar.place(x=434, y=105, anchor=tkinter.CENTER)
    
    # Consultando CNPJ e retornando o resultado da consulta com as informações pertinentes
    button_consultar.configure(command=consulta_cnpj)
    
    # ---------------------------------------------------------------------------------------

    button_clean = customtkinter.CTkButton(master=janela_fornecedor, text="",
                                           width=15,
                                           height=15,
                                           font=('Poppins Bold', 10),
                                           fg_color=co4,
                                           bg_color=co4,
                                           image=vetor_clean,
                                           cursor='hand2')

    button_clean.place(x=475, y=105, anchor=tkinter.CENTER)
    
    # Quando clicado, as informações presentes nas entrys são apagadas para inserção de novos 
    # dados.
    button_clean.configure(command=cleaning_entry)

    # ---------------------------------------------------------------------------------------
    # Criando e configurando o botão consultar
    button_cadastrarF = customtkinter.CTkButton(master=janela_fornecedor, text="CADASTRAR",
                                            width=15,
                                            height=15,
                                            font=('Poppins Bold', 17),
                                            fg_color=co4,
                                            hover_color=co2,
                                            bg_color=co4,
                                            cursor='hand2')

    button_cadastrarF.place(x=501, y=475, anchor=tkinter.CENTER)

    # Cadastrando as infomações do fornecedor no banco de dados
    button_cadastrarF.configure(command=lambda:[query_fornecedor(), cleaning_entry()])


    janela_fornecedor.mainloop()
    
cad_fornecedor
