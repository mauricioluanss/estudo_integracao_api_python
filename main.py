import requests
import os
from dotenv import load_dotenv #essa lib serve pra carregar o arquivo .env no meu código. Aí eu vou poder importar os endpoints salvos lá.

load_dotenv()
CHAMADA_PAGAMENTO = os.getenv('CHAMADA_PAGAMENTO')

#funcao para chamar o pagamento no checkout
def pagamento(dados):
  resposta = requests.post(f'{CHAMADA_PAGAMENTO}', json=dados)

  if resposta.status_code == 200:
    print('Se essa mesagem aparecer é pq deu certo a requisição. O checkout Payer tem que abrir.')
    print(resposta.json())
  else:
    print('DEU ERRO SEU ANIMAL - verificar se a estrutura do json ta correta')



#funcao de operacao completa de venda
def main(opcao, value, dados):
  if opcao == 1:
    metodo = int(input('Métodos de pagamento:\n1 - DEBITO\n2 - CREDITO\n\nDigite a opção: '))

    if metodo == 1: #debito
      dados['command'] = 'PAYMENT'
      dados['value'] = value
      dados['paymentMethod'] = 'CARD'
      dados['paymentType'] = 'DEBIT'
      pagamento(dados)

    elif metodo == 2: #credito
      forma = int(input('1 - A VISTA\n2 - PARCELADO\n\nDigite a opção: '))

      if forma == 1: # Credito a vista
        dados['command'] = 'PAYMENT'
        dados['value'] = value
        dados['paymentMethod'] = 'CARD'
        dados['paymentType'] = 'CREDIT'
        dados['paymentMethodSubType'] = 'FULL_PAYMENT'
        pagamento(dados)
      elif forma == 2: # Credito parcelado lojista
        dados['command'] = 'PAYMENT'
        dados['value'] = value
        dados['paymentMethod'] = 'CARD'
        dados['paymentType'] = 'CREDIT'
        dados['paymentMethodSubType'] = 'FINANCED_NO_FEES'
        pagamento(dados)
      else:
        print('Opção inválida')
        return

    else:
      print('Opção inválida')
      return

  elif opcao == 2: #dinheiro
    dados['command'] = 'PAYMENT'
    dados['value'] = value
    dados['paymentMethod'] = 'CASH'
    dados['paymentType'] = 'CASH'
    pagamento(dados)

  elif opcao == 3: #pix
    dados['command'] = 'PAYMENT'
    dados['value'] = value
    dados['paymentMethod'] = 'PIX'
    pagamento(dados)


#essas duas linhas vao capturar o valor digitado e pedir para escolher a forma de pagamento
value = int(input('Digite o valor do produto: '))
opcao = int(input('Formas de pagamento:\n1 - CARTÃO\n2 - DINHEIRO\n3 - PIX\n\nDigite a opção:'))

dados = {} #aqui eu vou salvar os campos e os valores que serão enviados em json para o checkout
main(opcao, value, dados)



"""{
  "command": "string",
  "value": 1,
  "idPayer": "string",
  "paymentMethod": "string",
  "paymentType": "string",
  "paymentMethodSubType": "string",
  "installments": 0,
  "documentNumber": "string",
  "service": "string",
  "paymentDate": "yyyy-MM-dd",
  "email": "string",
  "password": "string",
  "remoteOrder": {
    "posId": "string",
    "flow": "string"
  },
  "callbackUrl": "string"
}"""




"""def consulta_transacao(consulta):
  consulta = requests.get("http://localhost:6060/Client/response", json={
    "request": {
      "command": "string",
      "value": 0
    },
    "correlationId": "string",
    "idPayer": "string",
    "statusTransaction": "string",
    "companyId": "string",
    "storeId": "string",
    "terminalId": "string",
    "value": "string",
    "documentNumber": "string",
    "shopPaymentReceipt": "string",
    "customerPaymentReceipt": "string",
    "operationType": "string",
    "paymentMethod": "string",
    "paymenType": "string",
    "paymentSubMethod": "string",
    "installments": "string",
    "paymentDate": "string",
    "transactionDateTime": "2022-01-01T00:00:00.000",
    "acquirer": "string",
    "acquirerCNPJ": "string",
    "flag": "string",
    "thirdPartyId": "string",
    "authorizerId": "string",
    "authorizerUsn": "string",
    "service": {
      "paymentId": "string"
    }
  })
consulta = consulta_transacao()"""