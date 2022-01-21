#Chute ao número
import random
print('O computador irá gerar um avlor aleatório de 1 a 10, tente adivinhar...')
valor_aleatorio = random.randint(1,10) 
val_recebido = int(input('Digite um numero:'))
print('-='*21)
if val_recebido == valor_aleatorio:
    print("PARABÉNS!!! VOCÊ ADIVINHOU")
else:
    print("Ops..! Tente novamente.")
print('-='*21)