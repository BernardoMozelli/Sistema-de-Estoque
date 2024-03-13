import customtkinter
import os
import customtkinter  as ctk
from banco_conections.conexao import *
from banco_conections.conexao_cad import validate_query
from utils.layout.front import *
from PIL import ImageTk,Image
from menu_paginas.cadastro_fornecedor import cad_fornecedor
from menu_paginas.cadastro_fabricante import cad_fabricante
from menu_paginas.cadastro_categoria import cad_categoria
from menu_paginas.cadastro_subcategoria import cad_subcategoria
from menu_paginas.cadastro_produto import entrada_estoque
from menu_paginas.entrada_estoque import movimentaEstoque_entrada
from menu_paginas.saida_estoque import movimentaEstoque_saida
from menu_paginas.relatorio_completo import relatorio_versaocompleta
from menu_paginas.suporte import suporte_chat

def sistema():
 home_janela = Toplevel()
 home_janela.title("Sistema de Inventário")

 # alterando o icone
 home_janela.wm_iconbitmap(default="C://sistema_estoque/imagens/logo_icone.ico")
 home_janela.geometry("1000x550+250+70")
 home_janela.resizable(False, False)

 home_janela.grid_rowconfigure(0, weight=1)
 home_janela.grid_columnconfigure(1, weight=1)

 # Inserindo as imagens que serão utilizadas
 image_path = os.path.join(os.path.dirname(
 os.path.realpath(__file__)), "C:/sistema_estoque/imagens")

 background_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "background2.jpg")), size=(1000, 550))

 menu_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "menu.png")), size=(15, 16))

 home_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))

 cadastro_image = customtkinter.CTkImage(dark_image=Image.open(
 os.path.join(image_path, "formulario.png")), size=(20, 20))

 estoque_image = customtkinter.CTkImage(dark_image=Image.open(
 os.path.join(image_path, "estoque.png")), size=(20, 20))

 relatorio_image = customtkinter.CTkImage(dark_image=Image.open(
 os.path.join(image_path, "relatorio.png")), size=(20, 20))

 chat_image = customtkinter.CTkImage(dark_image=Image.open(
 os.path.join(image_path, "chat_light.png")), size=(20, 20))

 # Criando o frame de navegação
 navigation_frame = customtkinter.CTkFrame(
 master=home_janela, corner_radius=0)
 navigation_frame.grid(row=0, column=0, sticky="nsew")
 navigation_frame.grid_rowconfigure(7, weight=1)

 navigation_frame_label = customtkinter.CTkLabel(master=navigation_frame,
 text="  MENU",
 image=menu_image,
 compound="left",
 font=("Poppins Bold", 15)
  )
 navigation_frame_label.grid(row=0, column=0, padx=10, pady=10)

 def home_button_event():
     select_frame_by_name("home")

 def cadastro_button_event():
     select_frame_by_name("cadastro")

 def estoque_button_event():
     select_frame_by_name("estoque")

 def relatorio_button_event():
     select_frame_by_name("relatorio")

 def suporte_button_event():
     select_frame_by_name("suporte")

 home_button = customtkinter.CTkButton(master=navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
   image=home_image, anchor="w", command=home_button_event)
 home_button.grid(row=1, column=0, sticky="ew")

 cadastro_button = customtkinter.CTkButton(master=navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Cadastro",
   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
   image=cadastro_image, anchor="w", command=cadastro_button_event)
 cadastro_button.grid(row=2, column=0, sticky="ew")

 estoque_button = customtkinter.CTkButton(master=navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Estoque",
  fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
  image=estoque_image, anchor="w", command=estoque_button_event)
 estoque_button.grid(row=4, column=0, sticky="ew")

 relatorio_button = customtkinter.CTkButton(master=navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Relatório",
   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
   image=relatorio_image, anchor="w", command=lambda: [relatorio_button_event(), relatorio_versaocompleta()])
 relatorio_button.grid(row=5, column=0, sticky="ew")

 suporte_button = customtkinter.CTkButton(master=navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Suporte",
 fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
 image=chat_image, anchor="w", command=lambda: [suporte_button_event, suporte_chat()])
 suporte_button.grid(row=6, column=0, sticky="ew")

 # Criando o frame home
 home_frame = customtkinter.CTkFrame(
 master=home_janela, corner_radius=0, fg_color="transparent")
 home_frame.grid_columnconfigure(0, weight=1)

 # Inserindo imagem de fundo
 label_logoH = customtkinter.CTkLabel(master=home_frame,
  text="",
  image=background_image)
 label_logoH.pack()

 # criando o frame cadastro
 cadastro_frame = customtkinter.CTkFrame(
 master=home_janela, corner_radius=0, fg_color="transparent")
 cadastro_frame.grid_columnconfigure(0, weight=1)

 # Inserindo imagem de fundo
 label_logo = customtkinter.CTkLabel(master=cadastro_frame,
 text="",
 image=background_image)
 label_logo.pack()

 # Criando os botões no frame cadastro
 cadastro_frame_Button_Fornecedor = customtkinter.CTkButton(master=cadastro_frame, text="FORNECEDOR",
   width=170,
   height=35,
   font=(
   'Poppins Bold', 14),
   hover_color=co4,
   border_width=2,
   border_color=co0,
   bg_color=co0,
   fg_color=co0,
   cursor='hand2')
 cadastro_frame_Button_Fornecedor.place(x=387, y=170)

 cadastro_frame_Button_Fornecedor.configure(command=cad_fornecedor)

 cadastro_frame_Button_Fabricante = customtkinter.CTkButton(master=cadastro_frame, text="FABRICANTE",
   width=170,
   height=35,
   font=(
   'Poppins Bold', 14),
   hover_color=co4,
   border_width=2,
   border_color=co0,
   bg_color=co0,
   fg_color=co0,
   cursor='hand2')
 cadastro_frame_Button_Fabricante.place(x=387, y=245)

 cadastro_frame_Button_Fabricante.configure(command=cad_fabricante)

 cadastro_frame_Button_Categoria = customtkinter.CTkButton(master=cadastro_frame, text="CATEGORIA",
  width=170,
  height=35,
  font=(
  'Poppins Bold', 14),
  hover_color=co4,
  border_width=2,
  border_color=co0,
  bg_color=co0,
  fg_color=co0,
  cursor='hand2')
 cadastro_frame_Button_Categoria.place(x=387, y=320)
 cadastro_frame_Button_Categoria.configure(command=cad_categoria)

 cadastro_frame_Button_Sub_Categoria = customtkinter.CTkButton(master=cadastro_frame, text="SUB-CATEGORIA",
  width=170,
  height=35,
  font=(
  'Poppins Bold', 14),
  hover_color=co4,
  border_width=2,
  border_color=co0,
  bg_color=co0,
  fg_color=co0,
  cursor='hand2')
 cadastro_frame_Button_Sub_Categoria.place(x=387, y=392)
 cadastro_frame_Button_Sub_Categoria.configure(command=cad_subcategoria)

 # criando o frame estoque
 estoque_frame = customtkinter.CTkFrame(
 master=home_janela, corner_radius=0, fg_color="transparent")

 # Inserindo imagem de fundo
 label_logo = customtkinter.CTkLabel(master=estoque_frame,
 text="",
 image=background_image)
 label_logo.pack()

 # Criando os botões no frame estoque
 estoque_frame_Button_Produto = customtkinter.CTkButton(master=estoque_frame, text="CADASTRO DE PRODUTO",
   width=223,
   height=35,
   font=(
   'Poppins Bold', 14),
   hover_color=co4,
   border_width=2,
   border_color=co0,
   bg_color=co0,
   fg_color=co0,
   cursor='hand2')
 estoque_frame_Button_Produto.place(x=387, y=200)
 estoque_frame_Button_Produto.configure(command=entrada_estoque)

 estoque_frame_Button_Entrada = customtkinter.CTkButton(master=estoque_frame, text="MOVIMENTAÇÃO DE ENTRADA",
   width=170,
   height=35,
   font=(
   'Poppins Bold', 14),
   hover_color=co4,
   border_width=2,
   border_color=co0,
   bg_color=co0,
   fg_color=co0,
   cursor='hand2')
 estoque_frame_Button_Entrada.place(x=387, y=275)
 estoque_frame_Button_Entrada.configure(
 command=movimentaEstoque_entrada)

 estoque_frame_Button_Saida = customtkinter.CTkButton(master=estoque_frame, text="MOVIMENTAÇÃO DE SAÍDA",
  width=223,
  height=35,
  font=(
  'Poppins Bold', 14),
  hover_color=co4,
  border_width=2,
  border_color=co0,
  bg_color=co0,
 fg_color=co0,
 cursor='hand2')
 estoque_frame_Button_Saida.place(x=387, y=350)
 estoque_frame_Button_Saida.configure(command=movimentaEstoque_saida)

 # criando o frame relatorio
 relatorio_frame = customtkinter.CTkFrame(
 master=home_janela, corner_radius=0, fg_color="transparent")
 # Inserindo imagem de fundo relatório
 label_logo = customtkinter.CTkLabel(master=relatorio_frame,
 text="",
 image=background_image)
 label_logo.pack()

 # criando o frame suporte
 suporte_frame = customtkinter.CTkFrame(master=home_janela, corner_radius=0, fg_color="transparent")

 def select_frame_by_name(name):

    # set button color for selected button
    home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
    cadastro_button.configure(fg_color=("gray75", "gray25") if name == "cadastro" else "transparent")
    estoque_button.configure(fg_color=("gray75", "gray25") if name == "estoque" else "transparent")
    relatorio_button.configure(fg_color=("gray75", "gray25") if name == "relatorio" else "transparent")
    suporte_button.configure(fg_color=("gray75", "gray25") if name == "suporte" else "transparent")

    # Exibindo o frame quando o mesmo é selecionado
    if name == "home":
        home_frame.grid(row=0, column=1, sticky="nsew")
    else:
        home_frame.grid_forget()

    if name == "cadastro":
        cadastro_frame.grid(row=0, column=1, sticky="nsew")
    else:
        cadastro_frame.grid_forget()

    if name == "estoque":
        estoque_frame.grid(row=0, column=1, sticky="nsew")
    else:
        estoque_frame.grid_forget()

    if name == "relatorio":
        relatorio_frame.grid(row=0, column=1, sticky="nsew")
    else:
        relatorio_frame.grid_forget()

    if name == "suporte":
        suporte_frame.grid(row=0, column=1, sticky="nsew")
    else:
        suporte_frame.grid_forget()
        
 # selecionando o tema default
 select_frame_by_name("home")

 home_janela.mainloop()
 
sistema

