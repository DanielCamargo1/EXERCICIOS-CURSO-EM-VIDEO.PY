'''
Desenvolva um programa que leia o comprimento de três
 retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
print("-="*21)
print("analisador de triângulos")
print("-="*21)
a = float(input('Digite o valor de um lado: '))
b = float(input('digite o valor deoutro lado: '))
c = float(input('Digite o valor do ultimo lado: '))
if a < b + c and b < a + c and c < a + b:
    print("Esses volores correspondem, então PODE SER UM TRIÂNGULO!!")
else:
    print('OS valores NÃO PODEM SER UM TRIÂNGULO!!!')