'''
 Exercício Python 041: A Confederação Nacional de Natação
  precisa de um programa que leia o ano de nascimento de um 
  atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''
from datetime import date
atual = date.today().year
data_nascimento = int(input("Digite sua data de nascimento: "))
idade = atual - data_nascimento
if idade <= 9:
    print('Você tem {} então é considerado MIRIM '.format(idade))
elif idade > 9 and idade <=14:
    print('Você tem {} então é considerado INFANTIL '.format(idade))    
elif 14 < idade <= 19:
    print('Você tem {} então é considerado Júnior '.format(idade))
elif 19 < idade <= 25:
     print('Você tem {} então é considerado SENIOR '.format(idade))    
else:
     print('Você tem {} então é considerado MASTER'.format(idade))    





