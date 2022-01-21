# AUmento de salario
'''
Escreva um programa que pergunte o salário de um funcionário
 e calcule o valor do seu aumento. Para salários superiores a
  R$1250,00, calcule um aumento de 10%. Para os inferiores ou
   iguais, o aumento é de 15%.
'''
salário = float(input('Digite qual é o seu salário: '))
if salário >= 1250:
    aumento = (10/100 * salário) + salário
else:
    aumento = (15/100 * salário) + salário
print("Quem ganhava {} passsa a ganhar {}  ".format(salário,aumento))