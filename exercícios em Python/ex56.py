'''
• Exercício Python 056: Desenvolva um programa que leia o nome, 
idade e sexo de 4 pessoas. No final do programa, mostre: a média 
de idade do grupo, qual é o nome do homem mais velho e quantas
 mulheres têm menos de 20 anos.
'''
somaidade = 0
maior_idade_homem = 0
nome_mais_velho = ''
totmulher = ''
for n in range(1,5):
   print("=="*10)
   print(" {}ª PESSOA ".format(n))
   print("=="*10)
   nome = str(input('Qual é o nome da {}ª pessoa?: '.format(n)))
   idade = int(input("Quantos anos a {}ª pessoa tem?: ".format(n)))
   sexo = str(input('Qual é o sexo da {}ª pessoa?[ M/F ]:  '.format(n)))
   somaidade = somaidade + idade
   if n == 1 and sexo in'Mm':
      nome_mais_velho = nome
      maior_idade_homem += idade
   if sexo in 'Mm' and idade > maior_idade_homem:
      maior_idade_homem = idade
      nome_mais_velho = nome
   if sexo in ' Ff' and idade < 20:
      totmulher += 1
mediaidade = somaidade / 4
print(" A média das idades são:{} ".format(mediaidade))
print('O nome do mais velho é {} e a idade do mais velho {} '.format(nome_mais_velho,maior_idade_homem))
print('Ao todo são {} Mulheres menores de 20 anos '.format(totmulher))


'''if sexo == 'm' and idade > idade:
   print
print(" A média das idades são:{} ".format(média_de_idade))'''
