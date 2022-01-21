'''
Aumento de 15% de um salario de um funcionario
'''
salario = float(input("Qual é o seu salário?: "))
au = salario + (salario * 15 / 100)
print('seu salario era {} e com um aumento de 15%, passou a ser {}'.format(salario,au))
