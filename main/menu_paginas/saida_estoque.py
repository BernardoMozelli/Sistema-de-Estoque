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
    
    from banco_conections.conexao_saidaEstoque import selected, query_ProdutoEntrada, movimenta_saidaEstoque, atualiza_tabela
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
    
    vetor_consulta = customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "consulta_cnpj.png")), size=(17, 17))
    
    vetor_clean = customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "clean_entry.png")), size=(19, 19))
    
    customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "atualizar.png")), size=(17, 17))
    
    #value_titulo = ["ID", "PRODUTO", "QUANTIDADE", "SEGMENTO", "FABRICANTE", "FORNECEDOR", "MODELO"]
    
    frame_saida=customtkinter.CTkScrollableFrame(master=janela_SaidaProduto,orientation="vertical",
                      width=1000, height=200,
                      bg_color="transparent",
                      fg_color="transparent",
                      corner_radius=30)
    frame_saida.pack(pady=40)
    
    #Criando a treeview com os dados do banco
    global table_saida
    table_saida = CTkTable(master=frame_saida, column=7, hover_color=co3, justify="center", values=selected)
    table_saida.edit_column(1, width=250 )
    table_saida.edit_column(3, width=190 )
    table_saida.edit_column(4, width=360)
    table_saida.edit_column(5, width=380 )
    table_saida.edit_column(6, width=200)
    table_saida.pack(pady=0.30)

    #Criando e configurando a label ID
    label_id= customtkinter.CTkLabel(master=janela_SaidaProduto,
                                           text="ID",
                                           font=('Poppins bold', 12),
                                           width=25,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_id.place(x=52, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label produto
    label_produto= customtkinter.CTkLabel(master=janela_SaidaProduto,
                                           text="PRODUTO",
                                           font=('Poppins bold', 12),
                                           width=25,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_produto.place(x=142, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label quantidade
    label_quantidade= customtkinter.CTkLabel(master=janela_SaidaProduto,
                                           text="QTD",
                                           font=('Poppins bold', 12),
                                           width=15,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_quantidade.place(x=230, y=57, anchor=tkinter.CENTER)
    
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
    label_fabricante.place(x=485, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label fornecedor
    label_fornecedor= customtkinter.CTkLabel(master=janela_SaidaProduto,
                                           text="FORNECEDOR",
                                           font=('Poppins bold', 12),
                                           width=50,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_fornecedor.place(x=750,y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label modelo
    label_modelo= customtkinter.CTkLabel(master=janela_SaidaProduto,
                                           text="MODELO",
                                           font=('Poppins bold', 12),
                                           width=50,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_modelo.place(x=925, y=57, anchor=tkinter.CENTER)
    
    #----------------------------------------------------------------------------------------------------------
    #Labels das entrys
    
    # Criando e configurando a label id
    label_id = customtkinter.CTkLabel(master=janela_SaidaProduto,
                                           text="ID",
                                           font=('Poppins bold', 12),
                                           width=40,
                                           height=20,
                                           fg_color=co4,
                                           bg_color="transparent")
    label_id.place(x=167, y=310, anchor=tkinter.CENTER)
    
    entry_id = customtkinter.CTkEntry(master=janela_SaidaProduto,
                                    width=250,
                                    height=20,
                                    font=('Century gothic', 13),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    border_color=co4,
                                    placeholder_text='insira o ID',
                                    justify='center',
                                    corner_radius=10)
    entry_id.place(x=270, y=347, anchor=tkinter.CENTER)
    entry_id.get()
    
    # Criando e configurando a label produto
    label_produto = customtkinter.CTkLabel(master=janela_SaidaProduto,
                                           text="NOME DO PRODUTO",
                                           font=('Poppins bold', 12),
                                           width=40,
                                           height=20,
                                           fg_color=co4,
                                           bg_color="transparent")
    label_produto.place(x=630, y=310, anchor=tkinter.CENTER)
    
    global entry_produto
    entry_produto = customtkinter.CTkEntry(master=janela_SaidaProduto,
                                    width=250,
                                    height=20,
                                    font=('Century gothic', 13),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    border_color=co4,
                                    placeholder_text='nome do produto',
                                    justify='center',
                                    corner_radius=10)
    entry_produto.place(x=695, y=347, anchor=tkinter.CENTER)
    entry_produto.get()
    
    # Criando e configurando a label quantidade
    label_quantidadeEstoque = customtkinter.CTkLabel(master=janela_SaidaProduto,
                                           text="SAÍDA",
                                           font=('Poppins bold', 12),
                                           width=40,
                                           height=20,
                                           fg_color=co4,
                                           bg_color="transparent")
    label_quantidadeEstoque.place(x=592, y=400, anchor=tkinter.CENTER)
    
    global entry_quantidade
    entry_quantidade = customtkinter.CTkEntry(master=janela_SaidaProduto,
                                    width=250,
                                    height=20,
                                    font=('Century gothic', 13),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    border_color=co4,
                                    placeholder_text='insira a quantidade',
                                    justify='center',
                                    corner_radius=10)
    entry_quantidade.place(x=695, y=440, anchor=tkinter.CENTER)
    entry_quantidade.get()
    
    # Criando e configurando a label quantidade
    label_modeloestoque = customtkinter.CTkLabel(master=janela_SaidaProduto,
                                           text="MODELO",
                                           font=('Poppins bold', 12),
                                           width=40,
                                           height=20,
                                           fg_color=co4,
                                           bg_color="transparent")
    label_modeloestoque.place(x=170, y=400, anchor=tkinter.CENTER)
    
    global entry_modelo
    entry_modelo = customtkinter.CTkEntry(master=janela_SaidaProduto,
                                    width=250,
                                    height=20,
                                    font=('Century gothic', 13),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    border_color=co4,
                                    placeholder_text='modelo do produto',
                                    justify='center',
                                    corner_radius=10)
    entry_modelo.place(x=270, y=440, anchor=tkinter.CENTER)
    entry_modelo.get()
    
    def armazenar_id():
        global var_userselect, var_quantidade
        var_userselect = entry_id.get()
    armazenar_id
    
    def armazenar_qtd():
        global var_quantidade
        var_quantidade = entry_quantidade.get()
    armazenar_qtd
    
    def cleaning_entry():
        entry_id.delete(0, "end")
        entry_produto.delete(0, "end")
        entry_modelo.delete(0, "end")
        entry_quantidade.delete(0, "end")
    cleaning_entry
             
    
    # Criando e configurando o botão consultar
    button_consultar = customtkinter.CTkButton(master=janela_SaidaProduto, text="",
                                           width=15,
                                           height=15,
                                           font=('Poppins Bold', 10),
                                           fg_color=co4,
                                           bg_color=co4,
                                           image=vetor_consulta,
                                           cursor='hand2')

    button_consultar.place(x=420, y=345, anchor=tkinter.CENTER)
    button_consultar.configure( command=lambda:[armazenar_id(), query_ProdutoEntrada()])
    
    button_clean = customtkinter.CTkButton(master=janela_SaidaProduto, text="",
                                           width=15,
                                           height=15,
                                           font=('Poppins Bold', 10),
                                           fg_color=co4,
                                           bg_color=co4,
                                           image=vetor_clean,
                                           cursor='hand2')

    button_clean.place(x=460, y=345, anchor=tkinter.CENTER)
    button_clean.configure(command=cleaning_entry)
    
    # Criando e configurando o botão cadastrar
    button_cadastrar = customtkinter.CTkButton(master=janela_SaidaProduto, text="FINALIZAR",
                                            width=15,
                                            height=15,
                                            font=('Poppins Bold', 14),
                                            fg_color=co4,
                                            hover_color=co2,
                                            bg_color=co4,
                                            cursor='hand2')

    button_cadastrar.place(x=495, y=500, anchor=tkinter.CENTER)

    # Cadastrando as infomações do fornecedor no banco de dados
    button_cadastrar.configure(command=lambda:[armazenar_qtd(), movimenta_saidaEstoque(), atualiza_tabela()])
    
    janela_SaidaProduto.mainloop()
    
movimentaEstoque_saida