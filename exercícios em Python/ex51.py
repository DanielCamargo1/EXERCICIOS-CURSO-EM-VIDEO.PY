'''
 • Exercício Python 051: Desenvolva um programa que leia o primeiro 
 termo e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão.
'''
print('-='*21)
print('TEMOS DE UMA P.A')
print('-='*21)
p_termo = int(input('Digite o primeiro termo: '))
raz = int(input('Digite  a razão: '))
for c in range(p_termo, 20,raz):
    print(c, end=" ")