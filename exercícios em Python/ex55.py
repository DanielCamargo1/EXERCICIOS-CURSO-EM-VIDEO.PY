'''
• Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''
maiorp = 0
menorp = 0
for pes in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(pes)))
    if pes == 1:
        maiorp == peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso
print("o maior peso é {}Kg ". format(maiorp))
print("e o menor peso é {}Kg ".format(menorp))