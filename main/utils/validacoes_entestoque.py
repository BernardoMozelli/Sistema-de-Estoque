from CTkMessagebox import CTkMessagebox

#Valida o módulo entrada estoque
def valida_entradaestoque():
    from main.menu_paginas.cadastro_produto import var_validaseg, var_fabri, var_fornec, var_nomevalida, var_validamodelo, var_validadata, var_validanota, var_validaquantidade, var_validavalor
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

def valida_SaidaEstoque():
    from menu_paginas.saida_estoque import var_Entquantidade, var_saidaProduto, var_SaidaModelo, varSaida_Categoria, var_SaidaSubcategoria, var_SaidaNSerie
    from utils.mensagem_box import msgErroSaidaEstoque, msg_sucessoSaidaEstoque
    #Valida se todos os campos da página foram preenchidos
    
    #Valida os menus de opção
    
    while (var_saidaProduto or var_SaidaModelo or varSaida_Categoria or var_SaidaSubcategoria or var_SaidaNSerie) == ("SELECIONE O PRODUTO" or "SELECIONE O MODELO" or "SELECIONE A CATEGORIA" or "SELECIONE A SUB-CATEGORIA" or "SELECIONE O Nº DE SÉRIE"):
        msgErroSaidaEstoque()
        return var_saidaProduto
    
    #valida as entrys
    while (var_Entquantidade) == None:
        msgErroSaidaEstoque()
        return var_Entquantidade
    else:
        msg_sucessoSaidaEstoque()
        
valida_SaidaEstoque




    
        