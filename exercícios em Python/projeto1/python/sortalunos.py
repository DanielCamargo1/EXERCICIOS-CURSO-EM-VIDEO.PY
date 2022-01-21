'''
sortear quatro alunos para apagar o quadro
'''
import random
alu = str(input('Digite o nome do primeiro alunos: '))
alu2 = str(input('Digite o nome do segundo aluno: '))
alu3 = str(input('Digite o nome do terceiro  aluno: '))
alu4 = str(input('Digite o nome do quarto aluno: '))
lista = [alu,alu2,alu3,alu4]
escol = random.choice(lista)
print("o aluno(a) escolhido foi {} ".format(escol))