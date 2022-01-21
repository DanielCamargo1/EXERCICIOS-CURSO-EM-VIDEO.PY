'''
• Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
from time import sleep
from math import factorial
print('=='*20)
print('BEM VINDO A CALCULADORA DE FATORIAIS')
print('=='*20)
primeiro = int(input('Digite o número que deseja ver o fatorial: '))
cont = 1
c = primeiro
f = 1
fa = factorial(c)
sleep(1.5)
print('CALCULANDO...')
sleep(2)
while c > 0:    
    print(' {} '.format(c), end='')
    print(' X ' if c > 1 else ' = ',end='')
    c -= 1
    #f = f * c
print('{} '.format(fa))
   





