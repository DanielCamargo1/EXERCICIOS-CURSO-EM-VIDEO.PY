'''
• Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
from time import sleep
n_i = 0
cont = 0
soma = 0
while n_i != 999:
    n_i = int(input('Digite um número inteiro que não seja [999]: '))
    cont +=1
    soma = soma + n_i 
    sleep(0.5)
print('~'*20)
print("foram usados {} números ".format(cont - 1))
print('~'*20)
sleep(0.5)
print('A soma entre eles foi {} '.format(soma - 999))
sleep(2)
print('FIM DO PROGRAMA')