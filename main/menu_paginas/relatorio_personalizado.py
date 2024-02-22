import tkinter
from tkinter import ttk
import customtkinter as ctk
import customtkinter
from utils.layout.front import *
from customtkinter import filedialog
import os
from CTkTable import *
from PIL import ImageTk, Image
from pymysql import *
import pdfkit as pdf
import pandas.io.sql as sql
import warnings


#from banco_conections.conexao_saidaEstoque import selected_produto, selected_modelo, selected_entcategoria, selected_Entsubcategoria,selected_nserie, query_ProdutoEntrada
from .CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown

def relatorio_versaoPersonalizada():
    from banco_conections.conexao_relatorioCompleto import selected_relatorioC
    Janela_relatorioPersonalizado = customtkinter.CTkToplevel()
    Janela_relatorioPersonalizado.attributes("-topmost", True)
    Janela_relatorioPersonalizado.after(200, lambda: Janela_relatorioPersonalizado.iconbitmap("./imagens/logo_icone.ico")) # alterando o icone da janela
    Janela_relatorioPersonalizado.title("Movimentação de Saída/estoque")
    Janela_relatorioPersonalizado.geometry("1000x550+250+70")
    Janela_relatorioPersonalizado.resizable(False, False)
    Janela_relatorioPersonalizado.grid_rowconfigure(0, weight=1)
    Janela_relatorioPersonalizado.grid_columnconfigure(1, weight=1)

    # Inserindo as imagens que serão utilizadas
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "C:/sistema_estoque/imagens")

    customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "background_fornecedor.png")), size=(1000, 550))
    
    vetor_folder = customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "folder.png")), size=(17, 17))
    
    customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "atualizar.png")), size=(17, 17))
    
    
    frame_relatorioP=customtkinter.CTkScrollableFrame(master=Janela_relatorioPersonalizado,orientation="vertical",
                      width=1000, height=200,
                      bg_color="transparent",
                      fg_color="transparent",
                      corner_radius=30)
    frame_relatorioP.pack(pady=40)
    
    #---------------------------------------------------------------------------------------------------------------------
        
    #Criando a treeview com os dados do banco

    global table
    table = CTkTable(master=frame_relatorioP, column=7, hover_color=co3, justify="center", values=selected_relatorioC)
    table.edit_column(1, width=250 )
    table.edit_column(3, width=190 )
    table.edit_column(4, width=360)
    table.edit_column(5, width=380 )
    table.edit_column(6, width=200)
    table.pack(pady=0.30)
    
     #Criando e configurando a label ID
    label_id= customtkinter.CTkLabel(master=Janela_relatorioPersonalizado,
                                           text="ID",
                                           font=('Poppins bold', 12),
                                           width=25,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_id.place(x=52, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label produto
    label_produto= customtkinter.CTkLabel(master=Janela_relatorioPersonalizado,
                                           text="PRODUTO",
                                           font=('Poppins bold', 12),
                                           width=25,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_produto.place(x=142, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label quantidade
    label_quantidade= customtkinter.CTkLabel(master=Janela_relatorioPersonalizado,
                                           text="QTD",
                                           font=('Poppins bold', 12),
                                           width=15,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_quantidade.place(x=230, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label segmento
    label_segmento= customtkinter.CTkLabel(master=Janela_relatorioPersonalizado,
                                           text="SEGMENTO",
                                           font=('Poppins bold', 12),
                                           width=13,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_segmento.place(x=305, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label fabricante
    label_fabricante= customtkinter.CTkLabel(master=Janela_relatorioPersonalizado,
                                           text="FABRICANTE",
                                           font=('Poppins bold', 12),
                                           width=50,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_fabricante.place(x=485, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label fornecedor
    label_fornecedor= customtkinter.CTkLabel(master=Janela_relatorioPersonalizado,
                                           text="FORNECEDOR",
                                           font=('Poppins bold', 12),
                                           width=50,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_fornecedor.place(x=750,y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label modelo
    label_modelo= customtkinter.CTkLabel(master=Janela_relatorioPersonalizado,
                                           text="MODELO",
                                           font=('Poppins bold', 12),
                                           width=50,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_modelo.place(x=925, y=57, anchor=tkinter.CENTER)
    
    
    
    #----------------------------------------------------------------------------------------------------------------------

    #Criando e configurando a label GERAR RELATÓRIO
    label_GerarRelatorio= customtkinter.CTkLabel(master=Janela_relatorioPersonalizado,
                                           text="GERAR RELATÓRIO EM",
                                           font=('Poppins bold', 12),
                                           width=50,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color=co4)
    label_GerarRelatorio.place(x=110, y=430, anchor=tkinter.CENTER)

    
    #Cria o radion button para seleção do formato do relatório que será gerado (PDF ou Excel)
    radio_var = tkinter.IntVar(value=0)
    
    radiobutton_excel = customtkinter.CTkRadioButton(Janela_relatorioPersonalizado, text="Excel",
                                             variable= radio_var, value=1)
    radiobutton_excel.place(x=190, y=470, anchor=tkinter.CENTER)
    
    radiobutton_HTML = customtkinter.CTkRadioButton(Janela_relatorioPersonalizado, text="HTML",
                                             variable= radio_var, value=2)
    radiobutton_HTML.place(x=90, y=470, anchor=tkinter.CENTER)
    
    #-------------------------------------------------------------------------------------------------------------------------
    
    label_SelecionaOpcoes= customtkinter.CTkLabel(master=Janela_relatorioPersonalizado,
                                           text="SELECIONE AS INFORMAÇÕES QUE DEVERAM SER GERADAS NO RELATÓRIO",
                                           font=('Poppins bold', 12),
                                           width=50,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color=co4)
    label_SelecionaOpcoes.place(x=110, y=430, anchor=tkinter.CENTER)

    
    #Cria o radion button id
    '''radiobutton_ = customtkinter.CTkRadioButton(Janela_relatorioPersonalizado, text="Excel",
                                             variable= radio_var, value=1)
    radiobutton_excel.place(x=190, y=290, anchor=tkinter.CENTER)'''
    

    Janela_relatorioPersonalizado.mainloop()
    
relatorio_versaoPersonalizada