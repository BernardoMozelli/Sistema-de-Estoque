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

class Home(customtkinter.CTk):
    def __init__(self):        
        super().__init__()

        self.title("Sistema de Inventário")
        self.wm_iconbitmap(default="C://sistema_estoque/imagens/logo_icone.ico")  # alterando o icone
        self.geometry("1000x550+250+70")
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Inserindo as imagens que serão utilizadas
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "C:/sistema_estoque/imagens")
        
        self.background_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "background2.jpg")), size=(1000, 550))
        self.background_image2 = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "background.jpg")), size=(1000, 550))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo_transparent.png")), size=(20, 20))
        self.menu_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "menu.png")), size=(15, 16))
        self.home_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.cadastro_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "formulario.png")), size=(20, 20))
        self.exclusao_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "lixeira.png")), size=(20, 20))
        self.estoque_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "estoque.png")), size=(20, 20))
        self.relatorio_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "relatorio.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        
        # Criando o frame de navegação
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(7, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, 
                                                             text="  MENU",
                                                             image=self.menu_image,
                                                             compound="left",
                                                             font=("Poppins Bold",15) 
                                                             )
        self.navigation_frame_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")
        

        self.cadastro_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Cadastro",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.cadastro_image, anchor="w", command=self.cadastro_button_event)
        self.cadastro_button.grid(row=2, column=0, sticky="ew")
        
        
        self.estoque_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Estoque",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.estoque_image, anchor="w", command=self.estoque_button_event)
        self.estoque_button.grid(row=4, column=0, sticky="ew")
        
        self.relatorio_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Relatório",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.relatorio_image, anchor="w", command=lambda:[self.relatorio_button_event(), relatorio_versaocompleta()])
        self.relatorio_button.grid(row=5, column=0, sticky="ew")
        
        self.suporte_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Suporte",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=lambda:[self.suporte_button_event, suporte_chat()])
        self.suporte_button.grid(row=6, column=0, sticky="ew")
        

        # Criando o frame home
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        
        # Inserindo imagem de fundo
        label_logoH = customtkinter.CTkLabel(self.home_frame,
                                    text="",
                                    image=self.background_image)
        label_logoH.pack()

        # criando o frame cadastro
        self.cadastro_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.cadastro_frame.grid_columnconfigure(0, weight=1)
        
        # Inserindo imagem de fundo
        label_logo = customtkinter.CTkLabel(self.cadastro_frame,
                                    text="",
                                    image=self.background_image)
        label_logo.pack()

        #Criando os botões no frame cadastro
        self.cadastro_frame_Button_Fornecedor = customtkinter.CTkButton(self.cadastro_frame, text="FORNECEDOR",
                                                                        width=170,
                                                                        height=35,
                                                                        font=('Poppins Bold', 14),
                                                                        hover_color=co4,
                                                                        border_width=2,
                                                                        border_color=co0,
                                                                        bg_color=co0,
                                                                        fg_color=co0,
                                                                        cursor='hand2')
        self.cadastro_frame_Button_Fornecedor.place(x=387, y=170)
        
        self.cadastro_frame_Button_Fornecedor.configure(command = cad_fornecedor)
        
        self.cadastro_frame_Button_Fabricante = customtkinter.CTkButton(self.cadastro_frame, text="FABRICANTE",
                                                                        width=170,
                                                                        height=35,
                                                                        font=('Poppins Bold', 14),
                                                                        hover_color=co4,
                                                                        border_width=2,
                                                                        border_color=co0,
                                                                        bg_color=co0,
                                                                        fg_color=co0,
                                                                        cursor='hand2')
        self.cadastro_frame_Button_Fabricante.place(x=387, y=245)
        
        self.cadastro_frame_Button_Fabricante.configure(command = cad_fabricante)
        
        self.cadastro_frame_Button_Categoria = customtkinter.CTkButton(self.cadastro_frame, text="CATEGORIA",
                                                                      width=170,
                                                                      height=35,
                                                                      font=('Poppins Bold', 14),
                                                                      hover_color=co4,
                                                                      border_width=2,
                                                                      border_color=co0,
                                                                      bg_color=co0,
                                                                      fg_color=co0,
                                                                      cursor='hand2')
        self.cadastro_frame_Button_Categoria.place(x=387, y=320)
        self.cadastro_frame_Button_Categoria.configure(command = cad_categoria)

        self.cadastro_frame_Button_Sub_Categoria = customtkinter.CTkButton(self.cadastro_frame, text="SUB-CATEGORIA",
                                                                          width=170,
                                                                          height=35,
                                                                          font=('Poppins Bold', 14),
                                                                          hover_color=co4,
                                                                          border_width=2,
                                                                          border_color=co0,
                                                                          bg_color=co0,
                                                                          fg_color=co0,
                                                                          cursor='hand2')
        self.cadastro_frame_Button_Sub_Categoria.place(x=387, y=392)
        self.cadastro_frame_Button_Sub_Categoria.configure(command = cad_subcategoria)
        
        # criando o frame estoque
        self.estoque_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # Inserindo imagem de fundo
        label_logo = customtkinter.CTkLabel(self.estoque_frame,
                                    text="",
                                    image=self.background_image)
        label_logo.pack()
        
        #Criando os botões no frame estoque
        self.estoque_frame_Button_Produto = customtkinter.CTkButton(self.estoque_frame, text="CADASTRO DE PRODUTO",
                                                                        width=223,
                                                                        height=35,
                                                                        font=('Poppins Bold', 14),
                                                                        hover_color=co4,
                                                                        border_width=2,
                                                                        border_color=co0,
                                                                        bg_color=co0,
                                                                        fg_color=co0,
                                                                        cursor='hand2')
        self.estoque_frame_Button_Produto.place(x=387, y=200)
        self.estoque_frame_Button_Produto.configure(command = entrada_estoque)
        
        self.estoque_frame_Button_Entrada = customtkinter.CTkButton(self.estoque_frame, text="MOVIMENTAÇÃO DE ENTRADA",
                                                                          width=170,
                                                                          height=35,
                                                                          font=('Poppins Bold', 14),
                                                                          hover_color=co4,
                                                                          border_width=2,
                                                                          border_color=co0,
                                                                          bg_color=co0,
                                                                          fg_color=co0,
                                                                          cursor='hand2')
        self.estoque_frame_Button_Entrada.place(x=387, y=275)
        self.estoque_frame_Button_Entrada.configure(command = movimentaEstoque_entrada )
        
        self.estoque_frame_Button_Saida = customtkinter.CTkButton(self.estoque_frame, text="MOVIMENTAÇÃO DE SAÍDA",
                                                                          width=223,
                                                                          height=35,
                                                                          font=('Poppins Bold', 14),
                                                                          hover_color=co4,
                                                                          border_width=2,
                                                                          border_color=co0,
                                                                          bg_color=co0,
                                                                          fg_color=co0,
                                                                          cursor='hand2')
        self.estoque_frame_Button_Saida.place(x=387, y=350)
        self.estoque_frame_Button_Saida.configure(command = movimentaEstoque_saida )
        
        # criando o frame relatorio
        self.relatorio_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        # Inserindo imagem de fundo relatório
        label_logo = customtkinter.CTkLabel(self.relatorio_frame,
                                    text="",
                                    image=self.background_image)
        label_logo.pack()
        
        # criando o frame suporte
        self.suporte_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # selecionando o tema default
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.cadastro_button.configure(fg_color=("gray75", "gray25") if name == "cadastro" else "transparent")
        self.estoque_button.configure(fg_color=("gray75", "gray25") if name == "estoque" else "transparent")
        self.relatorio_button.configure(fg_color=("gray75", "gray25") if name == "relatorio" else "transparent")
        self.suporte_button.configure(fg_color=("gray75", "gray25") if name == "suporte" else "transparent")

        # Exibindo o frame quando o mesmo é selecionado
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
            
        if name == "cadastro":
            self.cadastro_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.cadastro_frame.grid_forget()
            
        if name == "estoque":
            self.estoque_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.estoque_frame.grid_forget()
            
        if name == "relatorio":
            self.relatorio_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.relatorio_frame.grid_forget()
            
        if name == "suporte":
            self.suporte_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.suporte_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def cadastro_button_event(self):
        self.select_frame_by_name("cadastro")

    def exclusao_button_event(self):
        self.select_frame_by_name("exclusao")
        
        
    def estoque_button_event(self):
        self.select_frame_by_name("estoque")
        
    def relatorio_button_event(self):
        self.select_frame_by_name("relatorio")
        
    def suporte_button_event(self):
        self.select_frame_by_name("suporte")

if __name__ == "__main__":
    home = Home()
    home.mainloop()