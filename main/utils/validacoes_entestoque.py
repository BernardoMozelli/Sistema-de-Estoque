from CTkMessagebox import CTkMessagebox

#Valida o módulo entrada estoque
def valida_entradaestoque():
    from menu_paginas.estoque_entrada import var_validaseg, var_fabri, var_fornec, var_nomevalida, var_validamodelo, var_validadata, var_validanota, var_validaquantidade, var_validavalor
    from utils.mensagem_box import msgErroEntradaestoque, msg_sucessoEntradaestoque
    #Valida se todos os campos da página foram preenchidos
    
    #Valida os menus de opção
    
    while (var_validaseg or var_fabri or var_fornec) == ("SELECIONE O SEGMENTO" or "SELECIONE O FABRICANTE" or "SELECIONE O FORNECEDOR" or "SELECIONE A CATEGORIA" or "SELECIONE A SUB-CATEGORIA"):
        msgErroEntradaestoque()
        return var_validaseg
    
    #valida as entrys
    while (var_nomevalida or var_validamodelo or var_validadata or var_validanota or var_validaquantidade or var_validavalor) == None:
        msgErroEntradaestoque()
        return var_nomevalida
    else:
        msg_sucessoEntradaestoque()
valida_entradaestoque

    
        