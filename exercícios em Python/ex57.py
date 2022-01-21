'''
• Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = str(input('Digite os eu sexo [M/F]?:  ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Digite novamente o seu sexo usando M ou F: ')).strip().upper()[0]
print("sexo {} registrado ".format(sexo))


