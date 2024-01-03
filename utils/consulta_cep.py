import requests
import json
from utils.mensagem_box import msg_cepincorreto

cep = input("Digite o CEP desejado: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.content)
    cep = ("CEP: ", data["cep"])
    logradouro = ("Logradouro: ", data["logradouro"])
    complemento = ("Complemento: ", data["complemento"])
    bairro = ("Bairro: ", data["bairro"])
    localidade = ("Cidade: ", data["localidade"])
    uf = ("Estado: ", data["uf"])
else:
   msg_cepincorreto
    