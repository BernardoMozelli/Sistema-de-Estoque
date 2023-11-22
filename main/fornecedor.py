import tkinter
import customtkinter as ctk
import customtkinter
from utils.layout.front import *
import os
import requests
import json
from banco_conections.conexao import *
import json

import consulta_correios 
#from utils.functions import format_cep
from PIL import ImageTk,Image 

janela_fornecedor = customtkinter.CTk()
janela_fornecedor.title("Cadastro de Fornecedor")
janela_fornecedor.wm_iconbitmap(default="./imagens/logo_icone.ico")  # alterando o icone
janela_fornecedor.geometry("1000x550+250+70")
janela_fornecedor.resizable(False, False)
janela_fornecedor.grid_rowconfigure(0, weight=1)
janela_fornecedor.grid_columnconfigure(1, weight=1)

# Inserindo as imagens que serão utilizadas
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "C:/Users/bernardomedeiros/Desktop/inventario - CTK/imagens")

background_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "teste.png")), size=(1000, 550))
vetor_consultCNPJ = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "consulta_cnpj.png")), size=(17, 17))

# Inserindo imagem de fundo
label_logo = customtkinter.CTkLabel(janela_fornecedor,
                                    text="",
                                    image=background_image)
label_logo.pack()

#Criando e configurando a label CNPJ
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

#Formata a entry CNPJ para a normativa padrão
def mascara_cnpj(event=None):
        if len(entry_cnpj.get()) == 2:
            entry_cnpj.insert(END, '.')
        if len(entry_cnpj.get()) == 6:
            entry_cnpj.insert(END, '.')
        if len(entry_cnpj.get()) == 10:
            entry_cnpj.insert(END, '/')
        if len(entry_cnpj.get()) == 15:
            entry_cnpj.insert(END, '-')
entry_cnpj.bind('<KeyRelease>', mascara_cnpj)
#-----------------------------------------------------------------
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
#-----------------------------------------------------------------

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

#-----------------------------------------------------------------
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

#Formata a entry CEP para a normativa padrão
def mascara_cep(event=None):
        if len(entry_cep.get()) == 5:
            entry_cep.insert(END, '-')
        if len(entry_cep.get()) > 9:
            entry_cep.delete(9, "end")
entry_cep.bind('<KeyRelease>', mascara_cep)

#-----------------------------------------------------------------
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
#-----------------------------------------------------------------

#-----------------------------------------------------------------
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
#-----------------------------------------------------------------
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
#-----------------------------------------------------------------
# Criando e configurando a label bairro
label_cidade_estado = customtkinter.CTkLabel(master=janela_fornecedor,
      text="CIDADE - ESTADO",
      font=('Poppins bold', 12),
      width=40,
      height=20,
      fg_color=co4,
      bg_color="transparent")
label_cidade_estado.place(x=639, y=310, anchor=tkinter.CENTER)

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
#-----------------------------------------------------------------

#API Consulta de CNPJ. A mesma insere os dados resultantes da 
# consulta nos respectivos campos
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
                entry_logradouro.insert(INSERT,format(receita['logradouro']))
                entry_logradouro.insert(INSERT, ','*1)
                entry_logradouro.insert(INSERT, ' Nº: '*1)
                entry_logradouro.insert(INSERT,format(receita['numero']))
                entry_complemento.insert(INSERT,format(receita['complemento']))
                entry_bairro.insert(INSERT,format(receita['bairro']))
                entry_cidade_estado.insert(INSERT,format(receita['municipio']))
                entry_cidade_estado.insert(INSERT, ' - '*1)
                entry_cidade_estado.insert(INSERT,format(receita['uf']))

                #entry_compleEndereco.insert(INSERT,format(receita['complemento']))
                #cnpj_txt.insert(INSERT, '-'*138)
                #entry_bairro.insert(INSERT,format(receita['bairro']))
                #entry_cidade.insert(INSERT,format(receita['municipio']))
                #entry_uf.insert(INSERT,format(receita['uf']))
            
            except KeyError:
                print('Erro ao buscar as informações!!!')
                #cnpj_txt.insert(INSERT, 'ERRO: {}'.format(receita['message']))
consulta_cnpj

#---------------------------------------------------------------------------------------
# Criando e configurando o botão esqueceu a senha
button_consultar = customtkinter.CTkButton(master=janela_fornecedor, text="",
                                           width=15,
                                           height=15,
                                           font=('Poppins Bold', 10),
                                           fg_color=co4,
                                           bg_color=co4,
                                           image=vetor_consultCNPJ)

button_consultar.place(x=434, y=105, anchor=tkinter.CENTER)

#Consultando usuário e retornando a ultima informação salva no log no momento da execução
button_consultar.configure(command=consulta_cnpj)


janela_fornecedor.mainloop()