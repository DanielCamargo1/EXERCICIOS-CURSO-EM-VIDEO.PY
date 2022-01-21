'''
 Exercício Python 037: Escreva um programa em Python que leia um número inteiro
  qualquer e peça para o usuário escolher qual será a base de conversão: 1 para 
  binário, 2 para octal e 3 para hexadecimal.
'''
numero = int(input('Digite um número inteiro: '))
print(''' Digite uma das bases para conversão:
[1] para BINÁRIO:
[2] para OCTAL:
[3] para HEXADECIMAL:   ''')
opção = int(input("Sua opção: "))
if opção == 1:
    print("o número {} no sistema bínario é {} ".format(numero,bin(numero)))
elif opção == 2:
    print("o número {} no sistema octal é {} ".format(numero,oct(numero)))
elif opção == 3:
    print('o número {} no sístema hexadecimal é {} '.format(numero,hex(numero)))
else:
    print("Essaopção não existe, tente novament!")