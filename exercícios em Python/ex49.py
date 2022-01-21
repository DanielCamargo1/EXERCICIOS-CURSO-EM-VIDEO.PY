'''
Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número
 que o usuário escolher, só que agora utilizando um laço for.
 OBSSS: USAR O MINIMO DE LINHAS POSSÍVEL    
'''
num = int(input('digite um número para ver a sua tabuada: '))
for c in range(1,11):
    print("{} X {} = {} ".format(num,c,num*c))