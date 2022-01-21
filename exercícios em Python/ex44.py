'''
 Exercício Python 044: Elabore um programa que calcule o valor a ser pago
  por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''
print('========== LOJA DO CAMARGO =========')
val_prod = float(input("Digite o valor so produto: R$ "))
dinchque = val_prod - (10/100 *  val_prod)
av_no_catao = val_prod - (5/100 * val_prod)
dv_no_cartao = val_prod / 2
print('-='*21)
print('''Qual é a sua forma de pagamento?
[ 1 ] À VISTA NO DINHEIRO/CHEQUE
[ 2 ] À VISTA NO CARTÃO
[ 3 ] EM ATÉ DUAS VEZES NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO''')
print('-='*21)
opc = int(input('Digite a opção do cliente: '))
if opc == 1:
  print("Pagando R${} no dinheiro, terá um desconto de 10%, então pagará R${} ".format(val_prod,dinchque))
elif opc == 2:
  print('Pagando R${} à vista no cartão, terá um desconto de 5%, então pagará R${} '.format(val_prod,av_no_catao))
elif opc == 3:
  print("Pagando R${} em até 2x no cartão, o preço ficará R${} ".format(val_prod,dv_no_cartao))
elif opc == 4:
  total = val_prod + (20/100 * val_prod)
  totprcelas = int(input("Quantas parcelas será?: "))
  parcfinal = total / totprcelas
  print('Sua compra será parcelada em {}, e terá 20%, de juros ficando R${} '.format(totprcelas,parcfinal))

