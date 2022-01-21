'''
 • Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" 
 em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.

'''
from random import randint
numero_aleatorio = randint(0,10)
chute = int(input('Tente adivinhar qual o número o computador chutou: '))
cont = 0
#print(numero_aleatorio)
while numero_aleatorio != chute:
    chute = int(input('Ops parece que você não acertou. Chute novamente um número do 0 a 10 e tente adivinhar:'))
    cont = cont + 1
print('Parabens, depois de {} chutes, você acertou o numero {}  '.format(cont,numero_aleatorio))