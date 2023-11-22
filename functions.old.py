# Formata os dados inseridos pelo usuário, aplicano o padrão de data dia/mês/ano.
def format_data(event=None):
    from cadastro import entry_data

    text = entry_data.get().replace("/", "")[:8]
    new_text = ""

    if event.keysym.lower() == "backspace":
        return

    for index in range(len(text)):

         if not text[index] in "0123456789":
                continue
         if index in [1]:
               new_text += text[index] + "/"
         elif index == 3:
                new_text += text[index] + "/"
         else:
               new_text += text[index]

         entry_data.delete(0, "end")
         entry_data.insert(0, new_text)
format_data    

def cad(*args):
 import cadastro
 cadastro
cad