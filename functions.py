#CRIEI ESSE ARQUIVO PARA COLOCAR AS FUNCOES DE REQUISICAO PARA O CHECKOUT
from config import *
import requests

#funcao para chamar o pagamento no checkout
def pagamento(dados):
  resposta = requests.post(f'{CHAMADA_PAGAMENTO}', json=dados)

  if resposta.status_code == 200:
    print('\n', resposta.status_code, " - ", resposta.reason,'\n')
  else:
    print('\n', resposta.status_code," - ", resposta.reason,'\n')
    

#funcao para consultar transacao enviada para o checkout
def consulta():
  resposta = requests.get(f'{CHAMADA_CONSULTA}')
  
  if resposta.status_code == 200 or resposta.status_code == 202:
    print('retorno da transacao: ', resposta.json())
  else:
    print(resposta.status_code,' - ', resposta.reason)