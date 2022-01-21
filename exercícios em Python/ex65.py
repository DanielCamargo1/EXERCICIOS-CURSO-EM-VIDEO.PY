'''
• Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
'''
num = int(input('DIGITE [1 PARA INICIAR] : '))
cont = 0
soma = 0
media = 0
if num == 1:
    while num != 0:
        num = int(input('DIGITE UM NÉMERO INT QUALQUER: '))
        cont += 1
        soma += num
    media = soma / cont
    print('A média entre os números é {} '.format(media))
    print('Fim do programa')
    #if num >
else:
    print('Digite 1 para iniciar o programa!')
'''
from time import sleep
resp = 'S'
qnt = soma = maior = menor = media = 0
while resp in 'Ss':
    num = int(input('Digite um número inteiro: '))
    sleep(0.5)
    qnt += 1
    soma += num
    media = soma / qnt
    resp = str(input('quer continuar [S/N]: '))
    sleep(0.5)
    if qnt ==1:
        maior = num = menor
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
sleep(0.5)
print('Avaliando...')
sleep(1.5)
print('Você digitou {} números, e a média entre eles é {} '.format(qnt,media))
sleep(1.5)
print('o maior numero  digitado é {} e o menor número digitado é o {}  '.format(maior,menor))