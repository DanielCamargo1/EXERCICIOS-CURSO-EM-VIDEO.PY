'''
 Exercício Python 039: Faça um programa que leia
o ano de nascimento de um jovem e informe, de
acordo com a sua idade, se ele ainda vai se 
alistar ao serviço militar, se é a hora exata 
de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou
que passou do prazo.
'''
from datetime import date
atual = date.today().year
ano_nascimento = int(input('Digite a sua data de nascimento: '))
idade = atual - ano_nascimento
ainda_vai = 18 - idade
passou = idade - 18
print("""Qual é o seu sexo?
[ 1 ] MASCULINO
[ 2 ] FEMININO  """)
sexo = int(input('digite aqui: '))
if idade < 18 and sexo == 2 :
    print('Você ainda tem {}, ainda falta {} para se alistar e NÃO PODERÁ SERVIR POR SER DO SEXO FEMININO'.format(idade,ainda_vai))
elif idade < 18 and sexo == 1:
    print('Você ainda tem {}, ainda falta {} para se alistar'.format(idade,ainda_vai))
elif idade == 18 and sexo == 1:
    print('É hora de se alistar, entre no nosso site e junte-se ao exército Brasileiro')
elif idade == 18 and sexo == 2:
    print('Você não poderá servivr pois é do sexo feminino')
elif idade > 18 and sexo == 1:
    print("Você ja passou da idade de alistamento, você deveria ter se alistado há {} anos !".format(passou))
elif  idade > 18 and sexo == 2:
    print("Você não poderá servir pois você é do sexo feminino")
















    