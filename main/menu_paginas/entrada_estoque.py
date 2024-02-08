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

def movimentaEstoque_entrada():
    
    from banco_conections.conexao_movimentacaoEntrada import selected, query_ProdutoEntrada, movimenta_entradaEstoque, atualiza_tabela
    janela_EntradaProduto = customtkinter.CTkToplevel()
    janela_EntradaProduto.attributes("-topmost", True)
    janela_EntradaProduto.after(200, lambda: janela_EntradaProduto.iconbitmap("./imagens/logo_icone.ico")) # alterando o icone da janela
    janela_EntradaProduto.title("Movimentação de Entrada/estoque")
    janela_EntradaProduto.geometry("1000x550+250+70")
    janela_EntradaProduto.resizable(False, False)
    janela_EntradaProduto.grid_rowconfigure(0, weight=1)
    janela_EntradaProduto.grid_columnconfigure(1, weight=1)

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
        
    frame_entrada=customtkinter.CTkScrollableFrame(master=janela_EntradaProduto,orientation="vertical",
                      width=1000, height=200,
                      bg_color="transparent",
                      fg_color="transparent",
                      corner_radius=30)
    frame_entrada.pack(pady=40)
    
        
    #Criando a treeview com os dados do banco
    global table_entrada
    table_entrada = CTkTable(master=frame_entrada, column=7, hover_color=co3, justify="center", values=selected)
    table_entrada.edit_column(1, width=250 )
    table_entrada.edit_column(3, width=190 )
    table_entrada.edit_column(4, width=360)
    table_entrada.edit_column(5, width=380 )
    table_entrada.edit_column(6, width=200)
    table_entrada.pack(pady=0.30)

    #Criando e configurando a label ID
    label_id= customtkinter.CTkLabel(master=janela_EntradaProduto,
                                           text="ID",
                                           font=('Poppins bold', 12),
                                           width=25,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_id.place(x=52, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label produto
    label_produto= customtkinter.CTkLabel(master=janela_EntradaProduto,
                                           text="PRODUTO",
                                           font=('Poppins bold', 12),
                                           width=25,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_produto.place(x=142, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label quantidade
    label_quantidade= customtkinter.CTkLabel(master=janela_EntradaProduto,
                                           text="QTD",
                                           font=('Poppins bold', 12),
                                           width=15,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_quantidade.place(x=230, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label segmento
    label_segmento= customtkinter.CTkLabel(master=janela_EntradaProduto,
                                           text="SEGMENTO",
                                           font=('Poppins bold', 12),
                                           width=13,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_segmento.place(x=305, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label fabricante
    label_fabricante= customtkinter.CTkLabel(master=janela_EntradaProduto,
                                           text="FABRICANTE",
                                           font=('Poppins bold', 12),
                                           width=50,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_fabricante.place(x=485, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label fornecedor
    label_fornecedor= customtkinter.CTkLabel(master=janela_EntradaProduto,
                                           text="FORNECEDOR",
                                           font=('Poppins bold', 12),
                                           width=50,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_fornecedor.place(x=750,y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label modelo
    label_modelo= customtkinter.CTkLabel(master=janela_EntradaProduto,
                                           text="MODELO",
                                           font=('Poppins bold', 12),
                                           width=50,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_modelo.place(x=925, y=57, anchor=tkinter.CENTER)
    
    #---------------------------------------------------------------------------------------------------------------------
    
    #Configurando as labels das entrys
    
    
    # Criando e configurando a label id
    label_id = customtkinter.CTkLabel(master=janela_EntradaProduto,
                                           text="ID",
                                           font=('Poppins bold', 12),
                                           width=40,
                                           height=20,
                                           fg_color=co4,
                                           bg_color="transparent")
    label_id.place(x=167, y=310, anchor=tkinter.CENTER)
    
    entry_id = customtkinter.CTkEntry(master=janela_EntradaProduto,
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
    label_produto = customtkinter.CTkLabel(master=janela_EntradaProduto,
                                           text="NOME DO PRODUTO",
                                           font=('Poppins bold', 12),
                                           width=40,
                                           height=20,
                                           fg_color=co4,
                                           bg_color="transparent")
    label_produto.place(x=630, y=310, anchor=tkinter.CENTER)
    
    global entry_produtoEntrada
    entry_produtoEntrada = customtkinter.CTkEntry(master=janela_EntradaProduto,
                                    width=250,
                                    height=20,
                                    font=('Century gothic', 13),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    border_color=co4,
                                    placeholder_text='nome do produto',
                                    justify='center',
                                    corner_radius=10)
    entry_produtoEntrada.place(x=695, y=347, anchor=tkinter.CENTER)
    entry_produtoEntrada.get()
    
    # Criando e configurando a label quantidade
    label_quantidadeEstoque = customtkinter.CTkLabel(master=janela_EntradaProduto,
                                           text="SAÍDA",
                                           font=('Poppins bold', 12),
                                           width=40,
                                           height=20,
                                           fg_color=co4,
                                           bg_color="transparent")
    label_quantidadeEstoque.place(x=592, y=400, anchor=tkinter.CENTER)
    
    global entry_quantidadeEntrada
    entry_quantidadeEntrada = customtkinter.CTkEntry(master=janela_EntradaProduto,
                                    width=250,
                                    height=20,
                                    font=('Century gothic', 13),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    border_color=co4,
                                    placeholder_text='insira a quantidade',
                                    justify='center',
                                    corner_radius=10)
    entry_quantidadeEntrada.place(x=695, y=440, anchor=tkinter.CENTER)
    entry_quantidadeEntrada.get()
    
    # Criando e configurando a label quantidade
    label_modeloestoque = customtkinter.CTkLabel(master=janela_EntradaProduto,
                                           text="MODELO",
                                           font=('Poppins bold', 12),
                                           width=40,
                                           height=20,
                                           fg_color=co4,
                                           bg_color="transparent")
    label_modeloestoque.place(x=170, y=400, anchor=tkinter.CENTER)
    
    global entry_modeloEntrada
    entry_modeloEntrada = customtkinter.CTkEntry(master=janela_EntradaProduto,
                                    width=250,
                                    height=20,
                                    font=('Century gothic', 13),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    border_color=co4,
                                    placeholder_text='modelo do produto',
                                    justify='center',
                                    corner_radius=10)
    entry_modeloEntrada.place(x=270, y=440, anchor=tkinter.CENTER)
    entry_modeloEntrada.get()
    
    def armazenar_id():
        global var_userselectEntrada
        var_userselectEntrada = entry_id.get()
    armazenar_id
    
    def armazenar_qtd():
        global var_quantidadeEntrada
        var_quantidadeEntrada = entry_quantidadeEntrada.get()
    armazenar_qtd
    
    def cleaning_entry():
        entry_id.delete(0, "end")
        entry_produtoEntrada.delete(0, "end")
        entry_modeloEntrada.delete(0, "end")
        entry_quantidadeEntrada.delete(0, "end")
    cleaning_entry
             
    
    # Criando e configurando o botão consultar
    button_consultar = customtkinter.CTkButton(master=janela_EntradaProduto, text="",
                                           width=15,
                                           height=15,
                                           font=('Poppins Bold', 10),
                                           fg_color=co4,
                                           bg_color=co4,
                                           image=vetor_consulta,
                                           cursor='hand2')

    button_consultar.place(x=420, y=345, anchor=tkinter.CENTER)
    button_consultar.configure( command=lambda:[armazenar_id(), query_ProdutoEntrada()])
    
    button_clean = customtkinter.CTkButton(master=janela_EntradaProduto, text="",
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
    button_cadastrar = customtkinter.CTkButton(master=janela_EntradaProduto, text="FINALIZAR",
                                            width=15,
                                            height=15,
                                            font=('Poppins Bold', 14),
                                            fg_color=co4,
                                            hover_color=co2,
                                            bg_color=co4,
                                            cursor='hand2')

    button_cadastrar.place(x=495, y=500, anchor=tkinter.CENTER)

    # Cadastrando as infomações do fornecedor no banco de dados
    button_cadastrar.configure(command=lambda:[armazenar_qtd(), movimenta_entradaEstoque(), atualiza_tabela()])
    
    janela_EntradaProduto.mainloop()
    
movimentaEstoque_entrada