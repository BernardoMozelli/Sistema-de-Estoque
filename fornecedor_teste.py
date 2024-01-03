import tkinter
import customtkinter as ctk
import customtkinter
from utils.layout.front import *
import os
from banco_conections.conexao import *
from utils.functions import format_cep
from PIL import ImageTk,Image 

janela_cadfornecedor = customtkinter.CTk()  # Criando a janela
janela_cadfornecedor.title("Cadastro de Fornecedor")
janela_cadfornecedor.wm_iconbitmap(default="./imagens/logo_icone.ico")  # alterando o icone
janela_cadfornecedor.geometry("1000x550+250+70")
janela_cadfornecedor.resizable(False, False)

janela_cadfornecedor.grid_rowconfigure(0, weight=1)
janela_cadfornecedor.grid_columnconfigure(1, weight=1)

# Inserindo as imagens que serão utilizadas
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "C:/Users/bernardomedeiros/Desktop/inventario - CTK/imagens")
        
background_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "background.jpg")), size=(1000, 550))
fornecedorMenu_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "fornecedor.png")), size=(16, 16))
image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo_transparent.png")), size=(20, 20))
cadastro_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "formulario.png")), size=(20, 20))
        
        
# Criando o frame de navegação
navigation_frame = customtkinter.CTkFrame(janela_cadfornecedor, corner_radius=0)
navigation_frame.grid(row=0, column=0, sticky="nsew")
navigation_frame.grid_rowconfigure(7, weight=1)

navigation_frame_label = customtkinter.CTkLabel(navigation_frame, 
                                                             text="  FORNECEDOR",
                                                             image=fornecedorMenu_image,
                                                             compound="left",
                                                             font=("Poppins Bold",14) 
                                                             )
navigation_frame_label.grid(row=0, column=0, padx=10, pady=10)

# Criando o frame cadastro de fornecedor
cadFornecedor_frame = customtkinter.CTkFrame(janela_cadfornecedor, corner_radius=0, fg_color="transparent")
cadFornecedor_frame.grid_columnconfigure(0, weight=1)

def cadastroFornecedor_button_event():
    select_frame_by_name(cadFornecedor_frame, name="cadastro de fornecedor")

#Criando o botão cadastro no menu de navegação
cadFornecedor_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Cadastro",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=cadastro_image, anchor="w")
cadFornecedor_button.grid(row=1, column=0, sticky="ew")

def select_frame_by_name(navigation_frame, name):
        cadFornecedor_button.configure(fg_color=("gray75", "gray25") if name == "cadastro de fornecedor" else "transparent")

        # Exibindo o frame quando o mesmo é selecionado
        if name == "cadastro de fornecedor":
            cadFornecedor_frame.grid(row=0, column=1, sticky="nsew")
        else:
            cadFornecedor_frame.grid_forget()
            
cadFornecedor_button.configure(command=cadastroFornecedor_button_event)
            
# selecionando o tema default
select_frame_by_name(cadFornecedor_frame, name="cadastro de fornecedor")

# Criando e configurando a label Título
label_nome = customtkinter.CTkLabel(master=cadFornecedor_frame,
                                      text="NOME",
                                      font=('Poppins bold', 12),
                                      width=40,
                                      height=20,
                                      fg_color=co4,
                                      corner_radius=10)
label_nome.place(x=123, y=78, anchor=tkinter.CENTER)

entry_nome = customtkinter.CTkEntry(master=cadFornecedor_frame,
                                    width=250,
                                    height=20,
                                    font=('Century gothic', 13),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    border_color=co4,
                                    placeholder_text='Nome do fornecedor.',
                                    justify='center')
entry_nome.place(x=220, y=105, anchor=tkinter.CENTER)
entry_nome.get()
        
# Criando e configurando a label Título
label_cep = customtkinter.CTkLabel(master=cadFornecedor_frame,
                                      text="CEP",
                                      font=('Poppins bold', 12),
                                      width=40,
                                      height=20,
                                      fg_color=co4,
                                      corner_radius=10)
label_cep.place(x=500, y=78, anchor=tkinter.CENTER)

# Criando e configurando a entry cep
global entry_cep   
entry_cep = customtkinter.CTkEntry(master=cadFornecedor_frame,
                                    width=250,
                                    height=20,
                                    font=('Century gothic', 13),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    border_color=co4,
                                    placeholder_text='Informe o CEP do seu fornecedor',
                                    justify='center')
entry_cep.place(x=600, y=105.3, anchor=tkinter.CENTER)
entry_cep.bind("<KeyRelease>", format_cep)
entry_cep.get()


if __name__ == "__main__":
    janela_cadfornecedor.mainloop()