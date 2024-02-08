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

def relatorio_versaocompleta():
    from banco_conections.conexao_relatorioCompleto import selected_relatorioC
    Janela_relatorioCompleto = customtkinter.CTkToplevel()
    Janela_relatorioCompleto.attributes("-topmost", True)
    Janela_relatorioCompleto.after(200, lambda: Janela_relatorioCompleto.iconbitmap("./imagens/logo_icone.ico")) # alterando o icone da janela
    Janela_relatorioCompleto.title("Movimentação de Saída/estoque")
    Janela_relatorioCompleto.geometry("1000x550+250+70")
    Janela_relatorioCompleto.resizable(False, False)
    Janela_relatorioCompleto.grid_rowconfigure(0, weight=1)
    Janela_relatorioCompleto.grid_columnconfigure(1, weight=1)

    # Inserindo as imagens que serão utilizadas
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "C:/sistema_estoque/imagens")

    customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "background_fornecedor.png")), size=(1000, 550))
    
    vetor_folder = customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "folder.png")), size=(17, 17))
    
    customtkinter.CTkImage(dark_image=Image.open(
    os.path.join(image_path, "atualizar.png")), size=(17, 17))
    
    
    frame_relatorioC=customtkinter.CTkScrollableFrame(master=Janela_relatorioCompleto,orientation="vertical",
                      width=1000, height=200,
                      bg_color="transparent",
                      fg_color="transparent",
                      corner_radius=30)
    frame_relatorioC.pack(pady=40)
    
    #---------------------------------------------------------------------------------------------------------------------
        
    #Criando a treeview com os dados do banco

    global table
    table = CTkTable(master=frame_relatorioC, column=7, hover_color=co3, justify="center", values=selected_relatorioC)
    table.edit_column(1, width=250 )
    table.edit_column(3, width=190 )
    table.edit_column(4, width=360)
    table.edit_column(5, width=380 )
    table.edit_column(6, width=200)
    table.pack(pady=0.30)

    #Criando e configurando a label ID
    label_id= customtkinter.CTkLabel(master=Janela_relatorioCompleto,
                                           text="ID",
                                           font=('Poppins bold', 12),
                                           width=25,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_id.place(x=52, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label produto
    label_produto= customtkinter.CTkLabel(master=Janela_relatorioCompleto,
                                           text="PRODUTO",
                                           font=('Poppins bold', 12),
                                           width=25,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_produto.place(x=142, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label quantidade
    label_quantidade= customtkinter.CTkLabel(master=Janela_relatorioCompleto,
                                           text="QTD",
                                           font=('Poppins bold', 12),
                                           width=15,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_quantidade.place(x=230, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label segmento
    label_segmento= customtkinter.CTkLabel(master=Janela_relatorioCompleto,
                                           text="SEGMENTO",
                                           font=('Poppins bold', 12),
                                           width=13,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_segmento.place(x=305, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label fabricante
    label_fabricante= customtkinter.CTkLabel(master=Janela_relatorioCompleto,
                                           text="FABRICANTE",
                                           font=('Poppins bold', 12),
                                           width=50,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_fabricante.place(x=485, y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label fornecedor
    label_fornecedor= customtkinter.CTkLabel(master=Janela_relatorioCompleto,
                                           text="FORNECEDOR",
                                           font=('Poppins bold', 12),
                                           width=50,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_fornecedor.place(x=750,y=57, anchor=tkinter.CENTER)
    
    #Criando e configurando a label modelo
    label_modelo= customtkinter.CTkLabel(master=Janela_relatorioCompleto,
                                           text="MODELO",
                                           font=('Poppins bold', 12),
                                           width=50,
                                           height=20,
                                           fg_color="transparent",
                                           corner_radius=7,
                                           bg_color="transparent")
    label_modelo.place(x=925, y=57, anchor=tkinter.CENTER)
    
    #----------------------------------------------------------------------------------------------------------------------------
    
    # Criando e configurando a label id
    label_pastaDestino = customtkinter.CTkLabel(master=Janela_relatorioCompleto,
                                           text="PASTA DE DESTINO",
                                           font=('Poppins bold', 12),
                                           width=40,
                                           height=20,
                                           fg_color=co4,
                                           bg_color="transparent")
    label_pastaDestino.place(x=202, y=310, anchor=tkinter.CENTER)
        
    entry_destino = customtkinter.CTkEntry(master=Janela_relatorioCompleto,
                                    width=250,
                                    height=20,
                                    font=('Century gothic', 13),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    border_color=co4,
                                    placeholder_text='clique no botão ao lado',
                                    justify='center',
                                    corner_radius=10)
    entry_destino.place(x=270, y=347, anchor=tkinter.CENTER)
    
    def seleciona_localArquivo():
        global nome_pasta
        nome_pasta = filedialog.askdirectory(parent=Janela_relatorioCompleto,
                                  initialdir="",
                                  title="Selecione a pasta de armazenamento")
        entry_destino.insert(0, nome_pasta)
    seleciona_localArquivo
    
    #Cria a label Formato do Arquivo
    label_formatoArquivo = customtkinter.CTkLabel(master=Janela_relatorioCompleto,
                                           text="FORMATO DO ARQUIVO",
                                           font=('Poppins bold', 12),
                                           width=40,
                                           height=20,
                                           fg_color=co4,
                                           bg_color="transparent")
    label_formatoArquivo.place(x=670, y=310, anchor=tkinter.CENTER)
    
    #Cria o radion button para seleção do formato do relatório que será gerado (PDF ou Excel) 
    radio_var = tkinter.IntVar(value=0)
    
    radiobutton_1 = customtkinter.CTkRadioButton(Janela_relatorioCompleto, text="Excel",
                                             variable= radio_var, value=1)
    radiobutton_1.place(x=650, y=347, anchor=tkinter.CENTER)
    
    radiobutton_2 = customtkinter.CTkRadioButton(Janela_relatorioCompleto, text="HTML",
                                             variable= radio_var, value=2)
    radiobutton_2.place(x=750, y=347, anchor=tkinter.CENTER)
    
    def valida_entryRelatorioC():
       from utils.mensagem_box import msgErroRelatorioCompletoEntry
       
       while entry_destino is None:
           msgErroRelatorioCompletoEntry()
           return entry_destino
    valida_entryRelatorioC
    
    def geraRelatCompleto():
       from banco_conections.conexao import con
       from utils.mensagem_box import msg_sucessoRelatorioCompleto, msgErroRelatorioCompleto
       
       df=sql.read_sql('SELECT * from cadastro_estoque ORDER BY ID', con)
       
       radio_var.get()
       
       if radio_var.get() == 1:
            df.to_excel(nome_pasta+'/relatorio_completo.xlsx')
            warnings.filterwarnings('ignore')
       else: 
             df.to_html(nome_pasta+'/relatorio_completo.html')
             warnings.filterwarnings('ignore')
       
       if con.is_connected():
            msg_sucessoRelatorioCompleto()
       else:
           msgErroRelatorioCompleto()
           return geraRelatCompleto
    geraRelatCompleto
        
    button_clean = customtkinter.CTkButton(master=Janela_relatorioCompleto, text="",
                                           width=15,
                                           height=15,
                                           font=('Poppins Bold', 10),
                                           fg_color=co4,
                                           bg_color=co4,
                                           image=vetor_folder,
                                           cursor='hand2')

    button_clean.place(x=420, y=345, anchor=tkinter.CENTER)
    button_clean.configure(command=seleciona_localArquivo)
    
    # Criando e configurando o botão cadastrar
    button_gerarRelatorioC = customtkinter.CTkButton(master=Janela_relatorioCompleto, text="GERAR RELATÓRIO",
                                            width=15,
                                            height=15,
                                            font=('Poppins Bold', 14),
                                            fg_color=co4,
                                            hover_color=co2,
                                            bg_color=co4,
                                            cursor='hand2')

    button_gerarRelatorioC.place(x=495, y=430, anchor=tkinter.CENTER)
    button_gerarRelatorioC.configure(command = geraRelatCompleto)
    

    Janela_relatorioCompleto.mainloop()
    
relatorio_versaocompleta