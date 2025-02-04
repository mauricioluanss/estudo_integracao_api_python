#estudo de integração com checkout de pagamentos, via API local.

from functions import pagamento, retorno

#essas duas linhas vao capturar o valor e pedir para escolher a forma de pagamento
value = float(input('Digite o valor do produto: '))
opcao = int(input('\nFormas de pagamento:\n1 - CARTÃO\n2 - DINHEIRO\n3 - PIX\n\nDigite a opção:'))

dados = {} #aqui eu vou salvar os campos e os valores que serão enviados em json para o checkout

#funcao de operacao completa de venda
def main(opcao, value, dados):
  if opcao == 1:
    metodo = int(input('\nMétodos de pagamento:\n1 - DEBITO\n2 - CREDITO\n\nDigite a opção: '))

    if metodo == 1: #debito
      dados = {'command': 'PAYMENT','value': value,'paymentMethod': 'CARD','paymentType': 'DEBIT'}
      pagamento(dados)

    elif metodo == 2: #credito
      forma = int(input('1 - A VISTA\n2 - PARCELADO\n\nDigite a opção: '))

      if forma == 1: # Credito a vista
        dados = {'command': 'PAYMENT','value': value,'paymentMethod': 'CARD','paymentType': 'CREDIT','paymentMethodSubType': 'FULL_PAYMENT'}
        pagamento(dados)
      elif forma == 2: # Credito parcelado lojista
        dados = {'command': 'PAYMENT','value': value,'paymentMethod': 'CARD','paymentType': 'CREDIT','paymentMethodSubType': 'FINANCED_NO_FEES'}
        pagamento(dados)
      else:
        print('Opção inválida')
        return

    else:
      print('Opção inválida')
      return

  elif opcao == 2: #dinheiro
    dados = {'command': 'PAYMENT','value': value,'paymentMethod': 'CASH','paymentType': 'CASH'}
    pagamento(dados)

  elif opcao == 3: #pix
    dados = {'command': 'PAYMENT','value': value,'paymentMethod': 'PIX'}
    pagamento(dados)


main(opcao, value, dados)

while True:
  if retorno():
    break