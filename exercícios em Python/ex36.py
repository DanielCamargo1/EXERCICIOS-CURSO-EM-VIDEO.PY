'''
Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal 
 não pode exceder 30% do salário ou então o empréstimo será negado.
'''
print("-="*40)
print('O emprestimo mas para liberarmos, você pecisa responder algumas perguntas!')
print("-="*40)
val_casa = float(input('Qual é o valor da casa?:R$ '))
sal_comprador = float(input('Qual o salário do comprador?:R$'))
anos_pagamento = int(input('Em quantos anos você vai pagar?: '))
prst_mensal = (12 * anos_pagamento) 
val_prest = val_casa / prst_mensal 
minimo = sal_comprador * 30 /100
if val_prest <= minimo:
    print('Commpra APROVADA!')
else:
    print('Infelizmente NÃO PODEMOS aprovar a compra!')