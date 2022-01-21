'''
 • Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
num = int(input('Digite um número inteiro: '))
if c in range(0,num + 1):
    if num % 1 == num and num % num == 0:
        print('Os números primos de {} são {} '.format(num,))


