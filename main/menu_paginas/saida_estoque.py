import tkinter
from tkinter import ttk
import customtkinter as ctk
import customtkinter
from utils.layout.front import *
import os
from CTkTable import *
from PIL import ImageTk, Image
#from banco_conections.conexao_saidaEstoque import selected_produto, selected_modelo, selected_entcategoria, selected_Entsubcategoria,selected_nserie, query_ProdutoEntrada
from .CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown

def movimentaEstoque_saida():
    
    from banco_conections.conexao_saidaEstoque import selected
    janela_SaidaProduto = customtkinter.CTkToplevel()
    janela_SaidaProduto.attributes("-topmost", True)
    janela_SaidaProduto.after(200, lambda: janela_SaidaProduto.iconbitmap("./imagens/logo_icone.ico")) # alterando o icone da janela
    janela_SaidaProduto.title("Movimentação de Saída/estoque")
    janela_SaidaProduto.geometry("1000x550+250+70")
    janela_SaidaProduto.resizable(False, False)
    janela_SaidaProduto.grid_rowconfigure(0, weight=1)
    janela_SaidaProduto.grid_columnconfigure(1, weight=1)

    # Inserindo as imagens que serão utilizadas
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "C:/sistema_estoque/imagens")

    customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "background_fornecedor.png")), size=(1000, 550))
    
    customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "atualizar.png")), size=(17, 17))
    
    #value_titulo = ["ID", "PRODUTO", "QUANTIDADE", "SEGMENTO", "FABRICANTE", "FORNECEDOR", "MODELO"]
    
    frame_saida=customtkinter.CTkScrollableFrame(master=janela_SaidaProduto,orientation="vertical",
                      width=800, height=200,
                      bg_color="transparent",
                      fg_color="transparent",
                      corner_radius=30)
    frame_saida.pack(pady=40)

    #Criando e configurando a label ID
    label_id= customtkinter.CTkLabel(master=janela_SaidaProduto,
                                           text="ID",
                                           font=('Poppins bold', 12),
                                           width=25,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_id.place(x=140, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label produto
    label_produto= customtkinter.CTkLabel(master=janela_SaidaProduto,
                                           text="PRODUTO",
                                           font=('Poppins bold', 12),
                                           width=25,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_produto.place(x=195, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label quantidade
    label_quantidade= customtkinter.CTkLabel(master=janela_SaidaProduto,
                                           text="QTD",
                                           font=('Poppins bold', 12),
                                           width=15,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_quantidade.place(x=250, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label segmento
    label_segmento= customtkinter.CTkLabel(master=janela_SaidaProduto,
                                           text="SEGMENTO",
                                           font=('Poppins bold', 12),
                                           width=13,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_segmento.place(x=305, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label fabricante
    label_fabricante= customtkinter.CTkLabel(master=janela_SaidaProduto,
                                           text="FABRICANTE",
                                           font=('Poppins bold', 12),
                                           width=50,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_fabricante.place(x=460, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label fornecedor
    label_fornecedor= customtkinter.CTkLabel(master=janela_SaidaProduto,
                                           text="FORNECEDOR",
                                           font=('Poppins bold', 12),
                                           width=50,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_fornecedor.place(x=700,y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label modelo
    label_modelo= customtkinter.CTkLabel(master=janela_SaidaProduto,
                                           text="MODELO",
                                           font=('Poppins bold', 12),
                                           width=50,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_modelo.place(x=856, y=57, anchor=tkinter.CENTER)
    
    
    # Criando e configurando a label sub-categoria
    label_id = customtkinter.CTkLabel(master=janela_SaidaProduto,
                                           text="SUB-CATEGORIA",
                                           font=('Poppins bold', 12),
                                           width=40,
                                           height=20,
                                           fg_color=co4,
                                           bg_color="transparent")
    label_id.place(x=165, y=310, anchor=tkinter.CENTER)
    

    #Criando a treeview com os dados do banco
    table = CTkTable(master=frame_saida, column=7, hover_color=co3, values=selected)
    table.configure(width=30,height=30)
    table.pack(pady=0.30)
    table.select_row()
    
    var = table.get(1, 1)
    print(var)
    #table.place(x=470, y=250, anchor=tkinter.CENTER)
    
    janela_SaidaProduto.mainloop()
    
movimentaEstoque_saida