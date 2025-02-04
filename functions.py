#CRIEI ESSE ARQUIVO PARA COLOCAR AS FUNCOES DE REQUISICAO PARA O CHECKOUT
from config import *
import requests
import time

#funcao para chamar o pagamento no checkout
def pagamento(dados):
  resposta = requests.post(f'{CHAMADA_PAGAMENTO}', json=dados)

  if resposta.status_code != 200:
    print('\n', 'retorno do post: ',resposta.status_code, " - ", resposta.reason,'\n')


def retorno():
  resposta = requests.get(f'{CHAMADA_CONSULTA}')
  
  if resposta.status_code == 200:
    print(resposta.json())
    return True
  else:
    print(resposta.json())
    time.sleep(3)
    return False