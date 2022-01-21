'''
Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('Digite em que ano a {}ª nasceu: '.format(pess)))
    idade  = atual - nasc
    if idade < 18:
        totmenor += 1
    elif idade >= 18:
        totmaior += 1
print('Ao todo tivemos {} pessoas maiores de idade '.format(totmaior))
print('E tanbem tivemos {} menor de idade '.format(totmenor))