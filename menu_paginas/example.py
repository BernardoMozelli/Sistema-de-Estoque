import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector

#Dados para conexão com o banco de dados
con = mysql.connector.connect(host='localhost', database='inventario_pmsl', user='bernardo', password='250317')

root = Tk()

frame = tk.Frame(root, padx=40,pady=40, bg='grey')

cursor = con.cursor()

cursor.execute('SELECT nome_fantasia FROM cadastro_fabricante')
options = cursor.fetchall()
selected = StringVar(root)
selected.set(options[0])

combobox = ttk.Combobox(root, textvariable=selected, values=options,
                               font=('verdana',14))

combobox.pack()
frame.pack()

root.mainloop()

