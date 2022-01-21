'''
 • Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))
soma = primeiro_valor + segundo_valor
multiplicação = primeiro_valor * segundo_valor
opcao = 0
while opcao != 5:
    print(''' O que você deseja?
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        print('a soma {} + {} = {} '.format(primeiro_valor, segundo_valor, soma))
    elif opcao == 2:
        print('A mulltiplicaçâo {} x {} = {} '.format(primeiro_valor,segundo_valor,multiplicação))
    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            print("O valor {} é amior que {} ".format(primeiro_valor,segundo_valor))
        else:
            print('O valor {} é maior que o {}  '.format(segundo_valor,primeiro_valor))
    elif opcao == 4:
        print('Digite novos valores!')
        primeiro_valor = int(input('primeiro valor: '))
        segundo_valor = int(input('Segundo valor: ')) 
    elif opcao == 5:
        print('SAINDO...')
    else:
        print('******Dados invalaidos****** digite novamente:')
    print('-='*8)
    sleep(2)
print('FIM DO PROGRAMA!')
