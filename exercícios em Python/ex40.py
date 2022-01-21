'''
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''
p_nota = float(input('Digite a primeira: '))
s_nota = float(input("Digite a segunda nota: "))
media = (p_nota + s_nota) / 2
if media < 5:
    print('-='*21)
    print("Você está REPROVADO!")
    print('-='*21)
elif media >= 5 and media <= 7 :
    print('-='*21)
    print("Você ficou de recuperação ")
    print('-='*21)
elif media >=7:
    print('-='*21)
    print("Você está APROVADO")
    print('-='*21)