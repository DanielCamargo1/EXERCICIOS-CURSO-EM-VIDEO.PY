# Maior e menor numero
print("Digite alguns valores e o programa mostrará o maior e o menor número: ")
v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
v3 = float(input('Digite o terceiro valor: '))
if v1>v2 and v1>v3:
    maior = v1
if v2>v1 and v2>v3:
    maior = v2
if v3>v1 and v3>v2:
    maior = v3
if v1<v2 and v1<v3:
    menor = v1
if v2<v1 and v2<v3:
    menor = v2
if v3<v2 and v3<v1:
    menor =  v3
print('O  menor número é o {:.1f} e o maior número é o {:.1f} '.format(menor, maior))